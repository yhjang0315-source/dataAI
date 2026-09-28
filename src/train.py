"""베이스라인 학습 스크립트 (문제 확정 후 수정)."""
import argparse


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True, help="data/processed 내 파일명")
    parser.add_argument("--target", required=True, help="타깃 컬럼명")
    args = parser.parse_args()
    raise NotImplementedError(f"문제 확정 후 구현: {args.data}, {args.target}")


if __name__ == "__main__":
    main()
