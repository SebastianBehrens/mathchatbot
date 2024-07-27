import boto3
import os
import logging

import boto3.session
from botocore.exceptions import NoCredentialsError
from pathlib import Path


def put_s3_file(file_path: Path, file_key: str, bucket: str, region: str) -> None:

    print("Creating Session.")
    session = boto3.Session(
        aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
        aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
        region_name=region  # e.g., us-west-2
    )

    s3s = session.client('s3')

    print("Uploading file to S3.")
    try:
        with open(file_path, "rb") as file:
            s3s.upload_fileobj(file, bucket, file_key)

        print("File successfully uploaded.")
    except NoCredentialsError:
        print("Credentials not available")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    put_s3_file(
        file_path=Path().cwd() / "cache" / "exercise_cache.pickle",
        file_key="/cache/exercise_cache.pickle",
        bucket="mathchatbot-eu-west-1",
        region="eu-west-1"

    )

