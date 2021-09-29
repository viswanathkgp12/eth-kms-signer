import os

from web3 import Web3

from eth_kms_signer import EthKmsClient

region = os.environ.get("AWS_KMS_REGION", "us-east-2")
key_id = os.environ.get("AWS_KMS_KEY_ID")
rpc_url = os.environ.get("RINKEBY_RPC_URL")

client = EthKmsClient(region)
from_address = client.get_address(key_id)
w3 = Web3(Web3.HTTPProvider(endpoint_uri=rpc_url))
nonce = w3.eth.get_transaction_count(from_address)

tx = {
    "nonce": nonce,
    "to": "0x7EeD368F105a6eaC9Ac645bC3440fEa9A6C3D531",
    "value": w3.toWei(12, "wei"),
    "gas": 21000,
    "gasPrice": w3.toWei(1, "gwei"),
    "chainId": "0x4",
}
signed_tx = client.sign_legacy_transaction(tx, key_id)
tx_hash = w3.eth.sendRawTransaction(signed_tx)
print(f"Transaction Hash: {tx_hash.hex()}")
