"""대회 평가지표."""
import numpy as np
from sklearn.metrics import f1_score

from src.labels import alert_level


def nse(obs, pred) -> float:
    obs, pred = np.asarray(obs, float), np.asarray(pred, float)
    return 1 - np.sum((obs - pred) ** 2) / np.sum((obs - obs.mean()) ** 2)


def evaluate(obs_cells, pred_cells) -> dict:
    obs, pred = np.asarray(obs_cells, float), np.clip(np.asarray(pred_cells, float), 0, None)
    lo, lp = np.log10(obs + 1), np.log10(pred + 1)
    return {
        "log_rmse": float(np.sqrt(np.mean((lo - lp) ** 2))),
        "log_mae": float(np.mean(np.abs(lo - lp))),
        "r2": float(np.corrcoef(obs, pred)[0, 1] ** 2),  # 원단위 결정계수(상관² 기준)
        "nse": float(nse(obs, pred)),
        "macro_f1": float(f1_score(alert_level(obs), alert_level(pred), average="macro")),
    }
