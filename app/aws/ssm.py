import boto3
from botocore.exceptions import NoCredentialsError
from os import getenv


class SSMHandler:
    def __init__(self):
        region_name = getenv("AWS_REGION")
        self.ssm_client = boto3.client('ssm', region_name=region_name)

    def get_parameter(self, parameter_name):
        try:
            response = self.ssm_client.get_parameter(
                Name=parameter_name,
                WithDecryption=True
            )
            return response['Parameter']['Value']
        except NoCredentialsError:
            raise Exception("AWS credentials not available.")
