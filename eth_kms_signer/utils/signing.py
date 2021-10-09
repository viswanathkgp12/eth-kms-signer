from typing import Tuple

from ecdsa import ecdsa, util
from eth_keys.backends.native.ecdsa import compress_public_key
from py_ecc.secp256k1 import ecdsa_raw_recover

# Order of elliptic curve secp256k1 from py_ecc
# ref: https://github.com/ethereum/py_ecc/blob/master/py_ecc/secp256k1/secp256k1.py#L31
N = 115792089237316195423570985008687907852837564279074904382605163141518161494337


def to_v_r_s(
    msghash: bytes,
    expected_compressed_pub_key: bytes,
    sig_der: bytes,
) -> Tuple[int, int, int]:
    """Canonicalize r, s and calculate recovery parameter"""
    rs = util.sigdecode_der(sig_der, ecdsa.generator_secp256k1.order())
    rs = _to_low_s(rs)
    return _recovery_param(msghash, expected_compressed_pub_key, rs)


# these enforce low S values, by negating the value (modulo the order) if
# above order/2
# ref: https://github.com/ethereum/py_ecc/blob/master/py_ecc/secp256k1/secp256k1.py#L150
def _to_low_s(rs: Tuple[int, int]) -> Tuple[int, int]:
    r, s = rs
    r, s = r, s if s * 2 < N else N - s
    return r, s


def _recovery_param(
    msghash: bytes,
    expected_compressed_pub_key: bytes,
    rs: Tuple[int, int],
) -> Tuple[int, int, int]:
    """Given a r, s and msghash, there can be two possible values of recovery param 0, 1

    Extract public key for each and compare with actual to find out the actual recovery parameter
    """
    for i in range(0, 2):
        v = 27 + i
        r, s = rs

        x, y = ecdsa_raw_recover(msghash, (v, r, s))
        actual_pub_key = _encode_int32(x) + _encode_int32(y)
        actual_pub_key = compress_public_key(actual_pub_key)

        if actual_pub_key == expected_compressed_pub_key:
            return i, r, s
    raise Exception("Cannot find recovery param for the signature, pub key")


def _encode_int32(v: int) -> bytes:
    return v.to_bytes(32, byteorder="big")
