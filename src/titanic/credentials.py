import os

import boto3
from dotenv import load_dotenv


def load() -> None:
    load_dotenv()

    boto3.setup_default_session(
        aws_access_key_id=os.getenv("AWS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_ACCESS_KEY"),
    )
