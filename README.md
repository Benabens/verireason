# VeriReason

A Transformer reasoning system built from scratch in PyTorch and trained with
procedurally generated, automatically verifiable tasks.

## Goal

This project studies whether a small decoder-only Transformer can learn
reusable algorithms instead of memorizing answers. It will compare supervised
training with verifier-driven reinforcement-learning post-training and measure
generalization on out-of-distribution problems.

## Planned pipeline

```text
Procedural task generation
        ↓
Tokenizer and numerical batches
        ↓
Decoder-only Transformer built from scratch
        ↓
Supervised training
        ↓
Automatic verifiers and rewards
        ↓
Reinforcement-learning post-training
        ↓
Reproducible in-distribution and OOD evaluation
```

## Current status

- [x] Reproducible Python environment with pinned PyTorch and NumPy versions
- [x] Procedural addition-problem generator
- [x] In-memory dataset generation
- [x] Reproducible generator smoke test with a fixed random seed
- [ ] Character-level tokenizer
- [ ] Embeddings and positional information
- [ ] Causal self-attention and multi-head attention
- [ ] Decoder blocks and language-model head
- [ ] Supervised training and autoregressive generation
- [ ] Verifiable algorithmic task families
- [ ] Reinforcement-learning post-training
- [ ] Baselines, ablations, and out-of-distribution evaluation

## Run the current generator

```bash
source .venv/bin/activate
python3 tasks.py
```

The current vertical slice generates `(problem, answer)` pairs such as:

```text
("42+97=", "139")
```

Addition is only the initial pipeline test. Later task families will include
structured arithmetic, sequence transformations, graphs, algorithms, and
automatically tested code.

## References

- Vaswani et al., [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- Umar Jamil, [Coding a Transformer from scratch in PyTorch](https://www.youtube.com/watch?v=ISNdQcPhsts)
