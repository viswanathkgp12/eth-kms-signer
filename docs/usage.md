## Usage

- Instantiate KMS Signer Client
- Getting the public key
- Getting the checksummed address
- Signing legacy transaction
- Signing EIP1559 transaction

Here are some common things you might want to do with eth kms signer.

### Instantiate KMS Signer Client

KMS Signer Client can be instantited by providong the region in which the KMS service is located on AWS.

```python
from eth_kms_signer import EthKmsClient

client = EthKmsClient(region_name="aws-kms-region")
```

### Getting the public key

You can retrieve the public key using

```python
pub_key = client.get_public_key(key_id)
```

### Getting the checksummed address

You can also retrieve the checksummed address corresponding to a key id using

```python
checksummed_address = client.get_address(key_id)
```

### Signing legacy transaction

Sign a **EIP 155** transaction using:

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

### Signing EIP1559 transaction

Sign a **EIP 1559** Dynamic Fee transaction using:

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
