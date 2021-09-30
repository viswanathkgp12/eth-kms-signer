# Welcome to ETH KMS Signer's documentation!

GitHub (code repository, issues): [https://github.com/viswanathkgp12/eth_kms_signer](https://github.com/viswanathkgp12/eth_kms_signer)

PyPI (installable, stable distributions): [https://pypi.org/project/eth-kms-signer](https://pypi.org/project/eth-kms-signer). You can install ETH KMS Signer using pip::

    pip install eth-kms-signer

ETH KMS Signer works with Python 3.5+.

## Introduction

AWS Key Management Service provides APIs to securely sign the application data using APIs via boto3 sdk. These private keys never leaves the KMS service and are designed so that no one, including AWS employees, can access the plaintext key material.

KMS Signer helps signing ETH transactions with a securely stored private key in AWS.

## Creating signing keys and setting up key policy permissions

To start, an assymetric ECDSA SECP256K1 Key needs to generated using KMS. This can be done using the AWS web console or through terraform or any such methods.

### 1. Using the web console

- Navigate to the [KMS console](https://console.aws.amazon.com/kms/home) and choose **Create key**.
- Choose the Asymmetric key option for the Key type. Provide an Alias like DocumentDB-MasterKey and Description for the key and click on Next to continue.
- Choose the IAM Users or roles who can administer the key. If you are running this lab using an AWS provided Event Engine account choose TeamRole, which may be on the 2nd page.
- Select Next.
- Similarly, choose the IAM users and roles that will use the CMK. Click Next
- Review the policy and click Finish

With the CMK ID created, you need to import token key id into ETH KMS Signer.

### 2. Using terraform

CloudPosse has a [terraform Module](https://github.com/cloudposse/terraform-aws-kms-key/tree/0.11.0) to provision the AWS KMS Key. A reference example of how to provision the key has been included in the project examples folder.

## Quick start

See `the project's [README](https://github.com/viswanathkgp12/eth_kms_signer/blob/master/README.md) for an
example of eth kms signer use.
