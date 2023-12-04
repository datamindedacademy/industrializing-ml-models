import argparse
from dataclasses import dataclass


@dataclass
class Config:
    bucket: str
    train_path: str
    test_path: str
    output_path: str


def parse() -> Config:
    parser = argparse.ArgumentParser(description="Titanic survival predictor")
    parser.add_argument(
        "--bucket",
        dest="bucket",
        help="The AWS S3 bucket name where the data can be found",
        required=True,
    )
    parser.add_argument(
        "--train",
        dest="train_path",
        help="The path to the training data set csv file in the S3 bucket",
        required=True,
    )
    parser.add_argument(
        "--test",
        dest="test_path",
        help="The path to the new passengers data set csv file in the S3 bucket",
        required=True,
    )
    parser.add_argument(
        "--output",
        dest="output_path",
        help="The path where to output the new passengers survival predictions csv file in the S3 bucket",
        required=True,
    )
    args = parser.parse_args()

    return Config(
        bucket=args.bucket,
        train_path=args.train_path,
        test_path=args.test_path,
        output_path=args.output_path,
    )
