from __future__ import annotations

import argparse
from pathlib import Path

import kagglehub


SOCIAL_MEDIA_DATASET = "cosmos98/twitter-and-reddit-sentimental-analysis-dataset"
MNIST_DATASET = "hojjatk/mnist-dataset"


def download_dataset(dataset_id: str) -> Path:
    """Download a Kaggle dataset and return its local path."""
    local_path = kagglehub.dataset_download(dataset_id)
    return Path(local_path)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Download Wednesday assignment datasets with kagglehub."
    )
    parser.add_argument(
        "--only",
        choices=["social", "mnist"],
        help="Download only one dataset instead of both.",
    )
    args = parser.parse_args()

    downloads = []
    if args.only == "social":
        downloads = [("Social media sentiment dataset", SOCIAL_MEDIA_DATASET)]
    elif args.only == "mnist":
        downloads = [("MNIST dataset", MNIST_DATASET)]
    else:
        downloads = [
            ("Social media sentiment dataset", SOCIAL_MEDIA_DATASET),
            ("MNIST dataset", MNIST_DATASET),
        ]

    for label, dataset_id in downloads:
        path = download_dataset(dataset_id)
        print(f"{label} downloaded to: {path}")


if __name__ == "__main__":
    main()
