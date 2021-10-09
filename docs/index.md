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
- Choose

  1. `Asymmetric` key option for the `Key type`
  2. `Sign and verify` option for the`Key usage`
  3. `ECC_SECG_P256K1` option for the`Key spec`

- Provide an `Alias` and `Description` for the key and click on `Next` to continue.

- Choose the IAM Users or roles who can administer the key.
- Select Next.
- Similarly, choose the IAM users and roles that will use the CMK. Click Next
- Review the policy and click Finish

With the assymetric key created, you need to import token key id into ETH KMS Signer.

### 2. Using terraform

CloudPosse has a [terraform Module](https://github.com/cloudposse/terraform-aws-kms-key/tree/0.11.0) to provision the AWS KMS Key. A reference example of how to provision the key has been included in the project examples folder.

For generating a ECC SECP256K1 Key, it takes the following inputs:

| Name | Description | Type | Required |
|------|-------------|------|:--------:|
| alias | The display name of the alias. The name must start with the word `alias` followed by a forward slash. If not specified, the alias name will be auto-generated. | `string` | no |
| customer\_master\_key\_spec | Set this to `ECC_SECG_P256K1`. | `string` | yes |
| deletion\_window\_in\_days | Duration in days after which the key is deleted after destruction of the resource | `number` | no |
| description | The description of the key as viewed in AWS console | `string` | no |
| enable\_key\_rotation | Specifies whether key rotation is enabled. Key rotation is only supported for encrypt decrypt key types. As such, always setthis to `false` | `bool` | | yes |
| key\_usage | Set this to `SIGN_VERIFY`. | `string` | yes |
| name | ID element. Usually the component or solution name, e.g. 'app' or 'jenkins'.<br>This is the only ID element not also included as a `tag`.<br>The "name" tag is set to the full `id` string. There is no tag with the value of the `name` input. | `string` | no |
| namespace | ID element. Usually an abbreviation of your organization name, e.g. 'eg' or 'cp', to help ensure generated IDs are globally unique | `string` | no |
| policy | A valid KMS policy JSON document. Note that if the policy document is not specific enough (but still valid), Terraform may view the policy as constantly changing in a terraform plan. In this case, please make sure you use the verbose/specific version of the policy. | `string` | no |

Once the key is generated with the above mentioned inputs, save the key id for later use in the KMS Signer.


## Quick start

See the project's [README](https://github.com/viswanathkgp12/eth_kms_signer/blob/master/README.md) for an
example of eth kms signer use.
