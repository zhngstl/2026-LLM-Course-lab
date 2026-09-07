# Session 01 — Using a coding harness

This session introduces a **coding harness** through two short activities:

1. use natural-language requests to explore a real workspace; and
2. diagnose, repair, and verify a bug in Python.


## Install / Requirements
- Python 3
- A way to run a local LLM: [llama.cpp](https://github.com/ggerganov/llama.cpp) or [llama.app](https://llama.app/)
- Harness: [Pi](https://pi.dev/) or [deepseek-harness](https://github.com/deepseek-ai/deepseek-harness), or the harness of your choice
- Model: [unsloth/gemma-4-E4B-it-GGUF](https://huggingface.co/unsloth/gemma-4-E4B-it-GGUF)

## What is a harness?
> The software layer around the language model that controls how the model interacts with its environment.

```text
                HARNESS
        ┌─────────────────────────┐
        │ prompt / instructions   │
        │ context management      │
User ──▶│ agent loop              │◀──▶ LLM
        │ tool definitions        │
        │ tool execution          │
        │ permissions / policies  │
        │ state / history         │
        └───────────┬─────────────┘
                    │
            ┌───────┴────────┐
            │ Environment    │
            │ files, shell,  │
            │ git, browser…  │
            └────────────────┘
```

## How to choose a model for Local LLM?
To know if the model is runnable on your system, number of parameters * 0.65 = required RAM in GB. 

For example, a 9B model requires 9 * 0.65 = 5.85 GB of RAM. 

## Exercises
Start with [prompts.md](prompts.md). The Python buggy file is [code.py](code.py).
