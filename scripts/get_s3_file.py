import boto3
import os
from botocore.exceptions import NoCredentialsError


def get_s3_file(file_key, bucket, region):
    session = boto3.Session(
        aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
        aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
        region_name=region  # e.g., us-west-2
    )

    s3s = session.client('s3')

    try:
        obj = s3s.get_object(Bucket=bucket, Key=file_key)
        content = obj['Body'].read().decode('utf-8')

    except NoCredentialsError:
        print("Credentials not available")
    except Exception as e:
        print(f"An error occurred: {e}")

    return (content)

# if __name__ = "__main__":
#     get_s3_file(
#             file_key =
#             )

