# Wednesday Assignment (Week 8)

This folder contains starter setup for the Wednesday assignment:
- social media sentiment dataset (Twitter + Reddit)
- MNIST dataset

## 1) Install dependencies

```bash
pip install kagglehub pandas numpy matplotlib scikit-learn torch torchvision sentence-transformers
```

## 2) Download datasets

Run from the `wednesday` folder:

```bash
python download_datasets.py
```

Optional:

```bash
python download_datasets.py --only social
python download_datasets.py --only mnist
```

## 3) Kaggle authentication

`kagglehub` needs your Kaggle credentials configured.
Set up your Kaggle token (`kaggle.json`) if downloads fail with authentication errors.

## 4) Dataset sources

- Social media sentiment: [cosmos98/twitter-and-reddit-sentimental-analysis-dataset](https://www.kaggle.com/datasets/cosmos98/twitter-and-reddit-sentimental-analysis-dataset)
- MNIST: [hojjatk/mnist-dataset](https://www.kaggle.com/datasets/hojjatk/mnist-dataset)
