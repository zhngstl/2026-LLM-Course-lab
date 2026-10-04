# Session 03 — Training a tiny Transformer

In this practical, we keep the tiny character-level Transformer from Session 02 and focus on **how models learn**. The model and dataset are deliberately small enough to train on a laptop CPU.

Start with [session03_training.ipynb](session03_training.ipynb) and complete the TODOs. A completed version is provided in [session03_training_correction.ipynb](session03_training_correction.ipynb).

The model architecture is defined in [`tiny_transformer.py`](tiny_transformer.py) and imported by both notebooks. This keeps the practical focused on training while retaining the Transformer built in Session 02 as ordinary reusable Python code.

## Learning objectives

By the end of the session, you should be able to:

- understand training loop
- its difference from evaluation / val loss
- overfit and underfit a model and understand the difference between the two
- (optinal) know how to tune hyperparameters and the effect of learning rate and batch size on training and validation loss
J

## Requirements

- Python 3
- PyTorch
- Matplotlib
- Jupyter

Install the dependencies in a virtual environment:

```bash
python -m pip install torch matplotlib jupyter
```

No GPU is required. The notebook limits the dataset, context length, model size, and number of evaluation batches so that all core experiments run on a normal laptop.

The notebook uses the included [`frnews.txt`](frnews.txt); no download is needed.

## Session outline

1. Prepare next-token training and validation batches.
2. Revisit the tiny causal Transformer.
3. Perform one optimization step by hand.
4. Complete a full train/evaluate/log loop using SGD.
5. Plot training and validation loss.
6. deliberately produce underfitting and overfitting.
7. Compare learning rates and batch sizes while keeping the optimizer fixed to SGD.

## Suggested timing

| Part | Time |
| --- | ---: |
| Data, model recap, and one update | 30 min |
| Complete the training loop | 35 min |
| Validation and learning curves | 25 min |
| Underfitting and overfitting experiments | 30 min |
| Hyperparameter challenge and synthesis | 25 min |

## Main takeaway

A low training loss is not the objective by itself. A useful model is one whose performance transfers to data that was not used to update its parameters. Always record and plot both training and validation metrics.
