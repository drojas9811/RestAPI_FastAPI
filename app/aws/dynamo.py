
import boto3
from botocore.exceptions import NoCredentialsError
from os import getenv
class DynamoDBHandler:
    def __init__(self):
        region_name=  getenv("AWS_REGION")
        self.dynamodb_client = boto3.client('dynamodb', region_name=region_name)

    def get_item(self, table_name, key):
        try:
            response = self.dynamodb_client.get_item(
                TableName=table_name,
                Key=key
            )
            return response.get('Item')
        except NoCredentialsError:
            raise Exception("AWS credentials not available.")
