import awswrangler as wr
import pandas as pd


class Storage:
    def __init__(self, bucket: str):
        self.bucket = bucket

    def _resolve(self, path: str) -> str:
        return f"s3://{self.bucket}/{path}"

    def read_csv(self, path: str) -> pd.DataFrame:
        return wr.s3.read_csv(path=self._resolve(path))

    def write_csv(self, data: pd.DataFrame, path: str) -> None:
        wr.s3.to_csv(data, path=self._resolve(path), index=False)
