"""세포수 기반 라벨 파생."""
import numpy as np

ALERT_LEVELS = ["해제", "관심", "경계", "대발생"]
ALERT_BINS = [1_000, 10_000, 1_000_000]  # 상수원 구간, cells/mL
GENERA = ["microcystis", "anabaena", "aphanizomenon", "oscillatoria"]


def alert_level(cells) -> np.ndarray:
    """세포수 → 경보단계 인덱스(0~3)."""
    return np.digitize(np.asarray(cells, dtype=float), ALERT_BINS)


def dominant_genus(df) -> "pd.Series":
    """4개 속 세포수 컬럼 중 최댓값 속 이름."""
    return df[GENERA].idxmax(axis=1)
