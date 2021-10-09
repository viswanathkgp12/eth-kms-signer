import boto3


class Client:
    def __init__(
        self,
        aws_access_key_id=None,
        aws_secret_access_key=None,
        region_name=None,
        boto_kms_client=None,
    ):
        """Client allows you to interact with AWS KMS resources.

        Args:
            aws_access_key_id (str, optional): AWS access key ID
            aws_secret_access_key (str, optional): AWS secret access key
            region_name (str, optional): Default region when creating new connections
            boto_kms_client (Any, optional): Use this client instead of creating new one
        """
        if boto_kms_client is not None:
            self.client = boto_kms_client
        else:
            self.client = boto3.client(
                "kms",
                aws_access_key_id=aws_access_key_id,
                aws_secret_access_key=aws_secret_access_key,
                region_name=region_name,
            )
