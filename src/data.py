"""데이터 로드/전처리."""
import pandas as pd

from src.config import PROCESSED_DIR, RAW_DIR


def load_raw(name: str) -> pd.DataFrame:
    return pd.read_csv(RAW_DIR / name)


def save_processed(df: pd.DataFrame, name: str) -> None:
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_DIR / name, index=False)
