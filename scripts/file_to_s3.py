import boto3
from pathlib import Path
from botocore.client import Config
import os


def file_to_s3(path, run_id) -> str:
    file_png: Path = path / f"run_{run_id}.png"
    # file_png= Path().cwd()/"test.png"
    file_s3: str = f"run_{run_id}.png"
    # file_s3: str = "test.png"
    s3_client = boto3.client(
        's3',
        region_name='eu-west-1',
        aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
        aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
        config=Config(signature_version='s3v4'),
        endpoint_url='https://s3.eu-west-1.amazonaws.com'
    )

    # Upload the file
    try:
        s3_client.upload_file(
            file_png,
            'mathchatbot-eu-west-1',
            f'images/{file_s3}',
            ExtraArgs={'ContentType': "image/png"}
            )
        print(f"File uploaded successfully to s3://mathchatbot-eu-west-1/{file_s3}")
    except Exception as e:
        print(f"Error uploading file: {e}")

    url = s3_client.generate_presigned_url(
        ClientMethod='get_object',
        Params={
            'Bucket': 'mathchatbot-eu-west-1',
            'Key': f'images/{file_s3}'
            # 'ResponseContentType': 'image/png'
            },
        ExpiresIn=600
    )
    print(f"Url at S3: {url}")
    return(url)