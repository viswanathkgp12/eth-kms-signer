from eth_keys.backends.native.ecdsa import compress_public_key
from eth_typing import ChecksumAddress
from eth_utils import keccak, to_checksum_address


def public_key_bytes_to_address(public_key_bytes: bytes) -> bytes:
    """Covert public key to address using first 20 bytes of keccak hash"""
    return keccak(public_key_bytes)[-20:]


def get_address_from_pub(uncompressed_public_key: bytes) -> ChecksumAddress:
    """Get checksummed address for an uncompressed public key"""
    return to_checksum_address(public_key_bytes_to_address(uncompressed_public_key))


def get_compressed_public_key(uncompressed_public_key: bytes) -> bytes:
    """Get public key in compressed format"""
    return compress_public_key(uncompressed_public_key)
