"""Small decoder-only Transformer used in Session 03.

The architecture lives in this module so that the practical notebook can focus
on the training loop, validation, and experimental diagnosis.
"""

import math

import torch
import torch.nn as nn
import torch.nn.functional as F

__all__ = ["CausalSelfAttention", "TransformerBlock", "TinyTransformer"]


class CausalSelfAttention(nn.Module):
    """Multi-head self-attention that cannot attend to future positions."""

    def __init__(self, d_model: int, num_heads: int, max_len: int):
        super().__init__()
        if d_model % num_heads != 0:
            raise ValueError("d_model must be divisible by num_heads")

        self.num_heads = num_heads
        self.d_head = d_model // num_heads
        self.q = nn.Linear(d_model, d_model, bias=False)
        self.k = nn.Linear(d_model, d_model, bias=False)
        self.v = nn.Linear(d_model, d_model, bias=False)
        self.proj = nn.Linear(d_model, d_model, bias=False)
        self.register_buffer(
            "causal_mask",
            torch.tril(torch.ones(max_len, max_len, dtype=torch.bool)),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        batch_size, seq_len, d_model = x.shape
        if seq_len > self.causal_mask.shape[0]:
            raise ValueError("sequence length exceeds the configured max_len")

        def split_heads(projection: torch.Tensor) -> torch.Tensor:
            return projection.view(
                batch_size, seq_len, self.num_heads, self.d_head
            ).transpose(1, 2)

        q = split_heads(self.q(x))
        k = split_heads(self.k(x))
        v = split_heads(self.v(x))

        scores = q @ k.transpose(-2, -1) / math.sqrt(self.d_head)
        mask = self.causal_mask[:seq_len, :seq_len]
        scores = scores.masked_fill(~mask, float("-inf"))
        weights = F.softmax(scores, dim=-1)

        attended = weights @ v
        attended = attended.transpose(1, 2).contiguous().view(
            batch_size, seq_len, d_model
        )
        return self.proj(attended)


class TransformerBlock(nn.Module):
    """Pre-normalization Transformer block with residual connections."""

    def __init__(
        self,
        d_model: int,
        num_heads: int,
        d_ff: int,
        max_len: int,
    ):
        super().__init__()
        self.ln1 = nn.LayerNorm(d_model)
        self.attention = CausalSelfAttention(d_model, num_heads, max_len)
        self.ln2 = nn.LayerNorm(d_model)
        self.mlp = nn.Sequential(
            nn.Linear(d_model, d_ff),
            nn.GELU(),
            nn.Linear(d_ff, d_model),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = x + self.attention(self.ln1(x))
        x = x + self.mlp(self.ln2(x))
        return x


class TinyTransformer(nn.Module):
    """A small character-level decoder that returns next-token logits."""

    def __init__(
        self,
        vocab_size: int,
        d_model: int = 32,
        num_heads: int = 4,
        d_ff: int = 64,
        num_layers: int = 1,
        max_len: int = 128,
    ):
        super().__init__()
        self.vocab_size = vocab_size
        self.max_len = max_len
        self.token_embedding = nn.Embedding(vocab_size, d_model)
        self.position_embedding = nn.Embedding(max_len, d_model)
        self.blocks = nn.ModuleList(
            [
                TransformerBlock(d_model, num_heads, d_ff, max_len)
                for _ in range(num_layers)
            ]
        )
        self.final_norm = nn.LayerNorm(d_model)
        self.head = nn.Linear(d_model, vocab_size, bias=False)

    def forward(self, token_ids: torch.Tensor) -> torch.Tensor:
        _, seq_len = token_ids.shape
        if seq_len > self.max_len:
            raise ValueError("sequence length exceeds the configured max_len")

        positions = torch.arange(seq_len, device=token_ids.device)
        x = self.token_embedding(token_ids) + self.position_embedding(positions)
        for block in self.blocks:
            x = block(x)
        return self.head(self.final_norm(x))
