import boto3


class Client:
    def __init__(self, region: str) -> None:
        """Constructor of the parent class of the KMS services.

        Args:
            region (str): Region in which to make queries and operations.
        """
        self.client = boto3.client("kms", region)
