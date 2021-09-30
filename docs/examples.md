# ETH Transfer using KMS Signer

Here is an example of how one can use the eth kms signer, web3.py to perform ether transfer.

To install needed dependencies you can use:

```sh
pip install eth-kms-signer
```

Once you have an environment set up, import your required libraries:

```python
from eth_kms_signer import EthKmsClient
from web3 import Web3
```

Instantiate the kms signer client

```python
client = EthKmsClient(region_name=region_name)
```

Initialize a web3 instance with an Infura node

```python
w3 = Web3(Web3.HTTPProvider(endpoint_uri=rpc_url))
```

Retrieve the address of the key id

```
from_address = client.get_address(key_id)
```

Find the current nonce from RPC using `get_transaction_count` method

```python
nonce = w3.eth.get_transaction_count(from_address)
```

Create a transaction dictionary with the required parameters

```python
tx = {
    "nonce": nonce,
    "to": "0x7EeD368F105a6eaC9Ac645bC3440fEa9A6C3D531",
    "value": w3.toWei(12, "wei"),
    "gas": 21000,
    "gasPrice": w3.toWei(1, "gwei"),
    "chainId": "0x4",
}
```

If you want the EIP 1559 dynamic fee transaction, omit the `gasPrice` and add `maxFeePerGas`, `maxPriorityFeePerGas` in the transaction dictionary.

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
```

Create a signed transaction of the tx dictionary

```python
signed_tx = client.sign_transaction(tx, key_id)
```

Broadcast the signed transaction using RPC's `sendRawTransaction` method

```python
tx_hash = w3.eth.sendRawTransaction(signed_tx)
```

More detailed examples can be found in the project's example folder.
