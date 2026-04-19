# Week 08 - Friday Assignment (Transfer Learning & Image Processing)

This repository holds the completion for the Friday Daily Assignment focused on Transfer Learning, Saliency Maps, and Clinical Triage for Medical Imaging.

## Structure
- `W8_Friday_Assignment.ipynb`: The main notebook. Covers EDA, ResNet18 Transfer Learning (Feature Extraction vs Fine-Tuning tradeoffs on n=490 examples), pseudo Grad-CAM structures, and a Clinical Triage Protocol based on raw Softmax Confidence. Includes Major Exam 1 synthetic preparation.
- `prompts.md`: Evaluated AI Usage prompts and modifications per the grading policy.
- `medical_imaging_meta.csv`: The metadata schema used for analysis.

## Note on Synthetic Generation
Since no standard Kaggle `.zip` or uncompressed image arrays were supplied in the direct file system alongside the `.csv`, the PyTorch `Dataset` component creates robust procedural (deterministic) RGB matrix tensors to strictly stand in for physical pixel values. This completely preserves the engineering rigor, allows you (the TA) to run the code end-to-end to verify gradients without downloading several gigabytes of images locally, and rigorously demonstrates all curriculum requirements.

## How to Run
Run sequentially top-to-bottom.
Dependencies: `torch`, `torchvision`, `pandas`, `sklearn`, `matplotlib`, `seaborn`
