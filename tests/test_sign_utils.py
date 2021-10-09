import unittest

from ecdsa import SigningKey, curves
from ecdsa.util import sha256, sigdecode_der, sigencode_der

from eth_kms_signer.utils import to_v_r_s


class TestSignUtils(unittest.TestCase):
    def test_signing(self):
        priv_key = SigningKey.generate(curve=curves.SECP256k1)
        pub_key = priv_key.verifying_key.to_string(encoding="compressed").hex()

        message = b"This is a test message"
        message_digest = sha256(b"This is a test message").digest()
        sig_der = priv_key.sign(message, hashfunc=sha256, sigencode=sigencode_der)
        expected_rs = sigdecode_der(sig_der, curves.SECP256k1.order)

        (v, r, s) = to_v_r_s(message_digest, bytes.fromhex(pub_key), sig_der)
        assert (r, s) == expected_rs
