# eth_kms_signer

AWS KMS Signer for ETH transactions

## Dependencies

- Python 3.5+

## QuickStart

This library is available on PyPI. Install via pip as:

```sh
  pip install eth-kms-signer
```

## Usage

1. Instantiate eth kms signer client

```python
from eth_kms_signer import EthKmsClient

client = EthKmsClient("{aws-kms-region}")
```

2. Initailize web3

```python
from web3 import Web3

w3 = Web3(Web3.HTTPProvider(endpoint_uri="{rpc_url}"))
```

3. Sign a EIP 155 transaction

```python
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
```

4. Sign a EIP 1559 Dynamic Fee transaction

```python
tx = {
    "nonce": nonce,
    "to": "0x7EeD368F105a6eaC9Ac645bC3440fEa9A6C3D531",
    "value": w3.toWei(12, "wei"),
    "gas": 21000,
    "maxFeePerGas": w3.toWei(1, "gwei"),
    "maxPriorityFeePerGas": w3.toWei(1, "gwei"),
    "type": "0x2",
    "chainId": "0x4",
}
signed_tx = client.sign_dynamic_fee_transaction(tx, key_id)
tx_hash = w3.eth.sendRawTransaction(signed_tx)
```

## Examples

Choose one of the following for a fully detailed example:

- [EIP 155 legacy transfer transaction](./examples/legacy/transfer.py)
- [EIP 155 legacy contract invocation](./examples/legacy/contract_invoke.py)
- [EIP 1559 transfer transaction](./examples/eip1559/transfer.py)
- [EIP 1559 contract invocation](./examples/eip1559/contract_invoke.py)

## Terraform to provision AWS KMS Key

[Detailed Example](./examples/terraform/main.tf)
