import base64
from typing import Dict, Tuple

from cytoolz import merge, partial, pipe
from ecdsa import VerifyingKey
from eth_account._utils.legacy_transactions import (
    TRANSACTION_DEFAULTS,
    encode_transaction,
    serializable_unsigned_transaction_from_dict,
)
from eth_account._utils.signing import to_eth_v
from eth_account._utils.typed_transactions import TypedTransaction
from eth_account._utils.validation import LEGACY_TRANSACTION_FORMATTERS
from eth_typing import ChecksumAddress
from eth_utils import to_int
from eth_utils.curried import apply_formatters_to_dict, hexstr_if_str

from eth_kms_signer.client import Client
from eth_kms_signer.utils import get_address_from_pub, get_compressed_public_key, to_v_r_s


class EthKmsClient(Client):
    def sign_transaction(self, tx: Dict, key_id: str) -> bytes:
        """Sign an ETH transaction using the Key ID in AWS KMS

        Args:
            tx (Dict): Dictionary representing the tx
            key_id (str): KeyID to be used for signing

        Returns:
            bytes: Signed transaction
        """
        if "type" in tx and hexstr_if_str(to_int)(tx["type"]) != "0x0":
            return self._sign_typed_transaction(tx, key_id)
        return self._sign_legacy_transaction(tx, key_id)

    def _sign_typed_transaction(self, tx: Dict, key_id: str) -> bytes:
        """Sign EIP 1559 Dynamic Fee/ EIP 2930 Access List Transaction"""
        transaction = TypedTransaction.from_dict(tx)
        raw_transaction = transaction.hash()
        v, r, s = self._raw_sign(raw_transaction, key_id)
        signed_transaction = {
            **transaction.as_dict(),
            "v": v,
            "r": r,
            "s": s,
        }
        return TypedTransaction.from_dict(signed_transaction).encode()

    def _sign_legacy_transaction(self, tx: Dict, key_id: str) -> bytes:
        """Sign Legacy EIP 155 Transaction"""
        sanitized_dictionary = pipe(
            tx,
            dict,
            partial(merge, TRANSACTION_DEFAULTS),
            apply_formatters_to_dict(LEGACY_TRANSACTION_FORMATTERS),
        )
        unsigned_transaction = serializable_unsigned_transaction_from_dict(
            sanitized_dictionary,
        )
        raw_transaction = unsigned_transaction.hash()
        vrs = self._raw_sign(raw_transaction, key_id)
        v, r, s = vrs
        chain_id = tx["chainId"]
        chain_id = hexstr_if_str(to_int)(chain_id)
        v = to_eth_v(v, chain_id)
        return encode_transaction(unsigned_transaction, (v, r, s))

    def get_public_key(self, key_id: str) -> bytes:
        """Get public key for a key id in AWS KMS

        Args:
            key_id (str): KeyID for which the public key needs to be retrieved

        Returns:
            bytes: Uncompressed public key
        """
        response = self.client.get_public_key(KeyId=key_id)
        pem = base64.b64encode((response.get("PublicKey")))
        key = VerifyingKey.from_pem(pem).to_string()
        return key

    def get_address(self, key_id: str) -> ChecksumAddress:
        """Get checksummed address for a KMS KeyId

        Args:
            key_id (str): KeyID for which the address needs to be retrieved

        Returns:
            ChecksumAddress: Checksummed address
        """
        return get_address_from_pub(self.get_public_key(key_id))

    def _raw_sign(self, msghash: bytes, key_id: str) -> Tuple[int, int, int]:
        """Generate v, r, s for a msg digest against a key id in AWS KMS

        Args:
            msghash (bytes): SHA256 Digest to be signed using AWS KMS
            key_id (str): KeyID to be used for signing

        Returns:
            Tuple[int, int, int]: v, r, s signature parameters
        """
        response = self.client.sign(
            KeyId=key_id,
            Message=msghash,
            MessageType="DIGEST",
            SigningAlgorithm="ECDSA_SHA_256",
        )
        sig_der = response.get("Signature")

        pub_key = get_compressed_public_key(self.get_public_key(key_id))
        return to_v_r_s(msghash, pub_key, sig_der)
