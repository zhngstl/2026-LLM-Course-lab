# Session 02 - Attention and Transformers

In this session, we will implement attention and a small decoder-only Transformer from scratch using PyTorch.

Start with [session02_attention.ipynb](session02_attention.ipynb) and complete the TODOs.

## Requirements and installation
About the installation, always do it via a virtual environment (venv) or conda environment. This will avoid conflicts with other packages you may have installed. (or even `uv` for a faster venv)

You only need **Python 3** and **PyTorch (`torch`)** and **numpy**. 
**No GPU is required** for the main exercises; training is optional.

Install PyTorch and numpy locally:

```bash
python -m pip install torch numpy
```
For people with GPU, you can install the CUDA version of PyTorch. See the [PyTorch installation guide](https://pytorch.org/get-started/locally/) for platform-specific instructions.

You can also upload the notebook to [Google Colab](https://colab.research.google.com/) and run it there. A CPU runtime is enough. If needed, install PyTorch in a cell with `%pip install torch`.

## 1. Attention mechanism

- Understand queries, keys, and values (Q, K, V).
- Compute attention scores and weights step by step.
- Implement scaled dot-product attention and multi-head self-attention.

## 2. Transformer architecture (decoder)

- Build a Transformer block with attention, a feed-forward network, residual connections, and layer normalization.
- Combine embeddings and decoder blocks into a tiny model that produces next-token scores (logits).

Optional: train the model on the provided French news dataset, [frnews.txt](frnews.txt).

## Additional resources

- [The Illustrated Transformer — Jay Alammar](https://jalammar.github.io/illustrated-transformer/): a visual explanation of attention and Transformers.
- [Let's build GPT from scratch — Andrej Karpathy](https://www.youtube.com/watch?v=kCc8FmEb1nY): a video walkthrough of a decoder-only model in PyTorch.
- [Generalized Language Models — Lilian Weng](https://lilianweng.github.io/posts/2019-01-31-lm/): a broader overview of pretrained language models; the GPT section is especially relevant to this session.
- [Decoder-Only Transformers: The Workhorse of Generative LLMs — Cameron R. Wolfe](https://cameronrwolfe.substack.com/p/decoder-only-transformers-the-workhorse): a detailed explanation of decoder-only Transformers and their architecture.
- [Attention Is All You Need — Vaswani et al. (2017)](https://arxiv.org/abs/1706.03762): the original encoder-decoder Transformer paper.