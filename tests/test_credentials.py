import os

from titanic import credentials


def test_load_credentials():
    credentials.load()

    assert os.getenv("AWS_KEY_ID")
    assert os.getenv("AWS_ACCESS_KEY")
