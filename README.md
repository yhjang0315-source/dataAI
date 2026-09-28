# dataAI — 2026 DATA·AI 분석 경진대회 (문제해결 부문)

주최: KISTI 외 · 공모 사이트: https://dataon.kr/competition

## 일정
| 단계 | 기간 |
|---|---|
| 채택 문제 공개 | 09.15 |
| 문제 해결 (모델 개발·제출) | 09.15 ~ 11.06 |
| 문제별 후보 선정 (서류) | 11.09 ~ 11.13 |
| 최종 발표평가 / 시상 | 11.25 (KISTI 대전본원) |

## 폴더 구조
```
data/raw/         원본 데이터 (git 제외)
data/processed/   전처리 데이터 (git 제외)
notebooks/        EDA·실험 노트북 (01_eda.ipynb 형식)
src/              재사용 코드 (config, data, train)
outputs/          모델·예측·그림 (git 제외)
docs/             전략·보고서 문서
```

## 시작하기
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

참가 전략: [docs/strategy.md](docs/strategy.md) · 문제 정의: [docs/problem.md](docs/problem.md)
