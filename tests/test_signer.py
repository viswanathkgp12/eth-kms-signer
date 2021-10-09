import unittest
from unittest import mock

from hexbytes import HexBytes

from eth_kms_signer import EthKmsClient

# Test case from https://github.com/ethereum/web3.py/blob/7f53f5d9d4001c0f54a732b9455dbeb3b1ad79d8/tests/core/eth-module/test_accounts.py
TEST_CASES = [
    {
        "transaction": {
            "to": "0xF0109fC8DF283027b6285cc889F5aA624EaC1F55",
            "value": 1000000000,
            "gas": 2000000,
            "gasPrice": 234567897654321,
            "nonce": 0,
            "chainId": 1,
        },
        "expected_raw_tx_hash": HexBytes(
            "0x6893a6ee8df79b0f5d64a180cd1ef35d030f3e296a5361cf04d02ce720d32ec5"
        ),
    },
]


class TestEthKmsClient(unittest.TestCase):
    def test_sign_transaction(self):
        # Fake key_id
        key_id = "8459385b-bc65-4222-966d-7efbfd8be447"

        # Fake signature
        v = 28
        r = int("5897c2c7c7412b0a555fb6f053ddb6047c59666bbebc6f5573134e074992d841", 16)
        s = int("1c71d1c62b74caff8695a186e2a24dd701070ba9946748318135e3ac0950b1d4", 16)

        for test_case in TEST_CASES:
            cli = EthKmsClient(boto_kms_client=object())
            with mock.patch(
                "eth_kms_signer.signer.EthKmsClient._raw_sign", return_value=(v, r, s)
            ) as patcher:
                cli.sign_transaction(test_case["transaction"], key_id)
                # assert signed message creation
                patcher.assert_called_with(test_case["expected_raw_tx_hash"], key_id)
