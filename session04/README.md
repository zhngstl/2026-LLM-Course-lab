# Session 04 — Fine-tuning a pretrained model

In this lab we adapt pretrained DistilBERT to classify YouTube videos from their titles and descriptions. The main path compares **full fine-tuning**, **head-only training**, and **LoRA** on the same data.

Start with [session04_finetuning.ipynb](session04_finetuning.ipynb). A completed version is in [session04_finetuning_correction.ipynb](session04_finetuning_correction.ipynb).

## Learning goals

- Identify the pretrained body and newly initialized classification head.
- Complete a fine-tuning loop and evaluate on held-out videos.
- Freeze parameters and count those still trainable.
- Build a small LoRA layer, then train adapters with PEFT.
- Compare validation accuracy, parameter counts, and training time.

The final `Trainer` exercise is optional. It repeats full fine-tuning through the Hugging Face API.

## Setup

Use Python 3 in a virtual environment:

```bash
python -m pip install torch transformers peft accelerate pandas matplotlib jupyter
```

A GPU is recommended. For Google Colab, choose a GPU runtime and upload the notebook together with [youtube_us.csv](youtube_us.csv) and [US_category_id.json](US_category_id.json). Run locally from this folder so the notebook finds the data files. The first model load downloads `distilbert-base-uncased` from Hugging Face; later loads use its local cache.

On CPU or Apple MPS, the notebook uses fewer videos and shorter token sequences. There are three core training runs, so CPU execution may take a while.

## Data and lab flow

The included data comes from the US portion of [Trending YouTube Video Statistics](https://www.kaggle.com/datasets/datasnaek/youtube-new). The CSV has one row per video. This avoids placing a video's repeated trending-day records in both training and validation.

1. Prepare eight balanced categories and a stratified train/validation split.
2. Inspect DistilBERT tokenization and measure the untrained classifier baseline.
3. Complete the manual training loop and fine-tune the whole model.
4. Freeze the body and train only the head.
5. Explore LoRA in one layer, then train LoRA adapters with PEFT.
6. Compare results. Optionally repeat full fine-tuning with `Trainer`.

## Main takeaway

The update loop is the same one used in Session 03. Full fine-tuning, head-only training, and LoRA differ in which parameters can change. The lab measures how that choice affects accuracy, training time, and the number of weights saved.

## Further reading

- [Hugging Face course: fine-tuning a pretrained model](https://huggingface.co/learn/llm-course/chapter3/1)
- [LoRA paper](https://arxiv.org/abs/2106.09685)
- [PEFT documentation](https://huggingface.co/docs/peft)
