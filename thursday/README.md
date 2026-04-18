# Week 08 - Thursday Assignment (RNNs + Sequential Data)

This repository contains the Jupyter Notebook for Thursday's Daily Assignment focused on LSTMs, and sequence models.

## Structure
- `W8_Thursday_Assignment.ipynb`: The main notebook containing the implementation of Next-day stock prediction using PyTorch (LSTM) and an Autoregressive baseline, along with manual BPTT implementations (Sub-steps 1, 3, 6, 7).
- `prompts.md`: Contains the prompts used for AI generation during the notebook development.
- `Day 47 stock_prices.csv`: The dataset used for sub-step 1.

**Note:** `chat_logs.csv` is missing from the environment, so Sub-steps 2, 4, 5 (Churn Prediction) are structurally outlined but not executed.

## Setup & Running
This project requires Python 3.9+ and standard data science libraries, notably **PyTorch**.
No external `requirements.txt` was enforced, but here are the core requirements:
- `pandas`
- `numpy`
- `torch`
- `matplotlib`
- `scikit-learn`

Run the notebook linearly from cell 1 to the end using Jupyter or VSCode Jupyter extension.

## Engineering Standards Included
* Clean separation of functions, avoiding giant code cells.
* Extensive Try/Except blocks for file I/O and Model Training blocks for defensive resilience.
* Constant usage extracted to the top (e.g. `WINDOW_SIZE`, `BATCH_SIZE`).
* Proper Time Series chronological splitting methodology.
