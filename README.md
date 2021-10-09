# eth_kms_signer

[![codecov](https://codecov.io/gh/viswanathkgp12/eth_kms_signer/branch/master/graph/badge.svg?token=EZELOBPE0S)](https://codecov.io/gh/viswanathkgp12/eth_kms_signer)
[![PyPI](https://img.shields.io/pypi/v/eth-kms-signer)](https://pypi.org/project/eth-kms-signer/)
[![Downloads](https://pepy.tech/badge/eth-kms-signer)](https://pepy.tech/project/eth-kms-signer)
[![PyPI - License](https://img.shields.io/pypi/l/eth-kms-signer)](https://github.com/viswanathkgp12/eth_kms_signer/blob/master/LICENSE)
[![Documentation Status](https://readthedocs.org/projects/eth-kms-signer/badge/?version=latest)](https://eth-kms-signer.readthedocs.io/en/latest/?badge=latest)

AWS KMS Signer for ETH transactions(EIP 155/EIP 1559/ EIP 2930)

[>> Go to documentation](https://eth-kms-signer.readthedocs.io/en/latest/)

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

client = EthKmsClient(region_name="{aws-kms-region}")
```

2. Initailize web3

```python
from web3 import Web3

w3 = Web3(Web3.HTTPProvider(endpoint_uri="{rpc_url}"))
```

3. Sign a **EIP 155** transaction

```python
tx = {
    "nonce": nonce,
    "to": "0x7EeD368F105a6eaC9Ac645bC3440fEa9A6C3D531",
    "value": w3.toWei(12, "wei"),
    "gas": 21000,
    "gasPrice": w3.toWei(1, "gwei"),
    "chainId": "0x4",
}
signed_tx = client.sign_transaction(tx, key_id)
tx_hash = w3.eth.sendRawTransaction(signed_tx)
```

4. Sign a **EIP 1559** Dynamic Fee transaction

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
signed_tx = client.sign_transaction(tx, key_id)
tx_hash = w3.eth.sendRawTransaction(signed_tx)
```

## Examples

Choose one of the following for a fully detailed example:

- [EIP 155 legacy transfer transaction](./examples/legacy/transfer.py)
- [EIP 155 legacy contract invocation](./examples/legacy/contract_invoke.py)
- [EIP 1559 transfer transaction](./examples/eip1559/transfer.py)
- [EIP 1559 contract invocation](./examples/eip1559/contract_invoke.py)

## Terraform to provision AWS KMS Key

The following example makes use of the [CloudPosse Terraform Module](https://github.com/cloudposse/terraform-aws-kms-key/tree/0.11.0):

[Detailed Example](./examples/terraform/main.tf)
