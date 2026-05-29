# FLOP — Floating Point Operation


---

## What is a FLOP

**FLOP** (Floating Point Operation) is **a single arithmetic operation on floating-point numbers** — meaning decimal numbers (with a decimal point).

Examples of 1 FLOP:
- `3.14 + 2.71` — an addition
- `2.5 × 4.0` — a multiplication
- `10.0 / 3.0` — a division

Each of these counts as **1 FLOP**.

---

## FLOP vs FLOPS

These are different things, and confusion is common:

| Term | Meaning |
|------|---------|
| **FLOP** | A floating-point operation (singular) |
| **FLOPs** | Multiple operations (plural, lowercase s) |
| **FLOPS** | FLOPs **per second** — measure of speed |

**FLOPS** is the metric used to measure the **computational power** of a processor.

---

## Common FLOPS scales

| Acronym | Value | Example |
|---------|-------|---------|
| KFLOPS | 10³ FLOPS | Computers from the 1960s |
| MFLOPS | 10⁶ FLOPS | PCs from the 1980s |
| GFLOPS | 10⁹ FLOPS | Modern CPU |
| TFLOPS | 10¹² FLOPS | Modern GPU |
| PFLOPS | 10¹⁵ FLOPS | GPU cluster |
| EFLOPS | 10¹⁸ FLOPS | Top supercomputers (El Capitan, Frontier) |

---

## Typical hardware values

- **Modern CPU (Intel/AMD)**: ~100–500 GFLOPS
- **Consumer GPU (RTX 4090)**: ~80 TFLOPS (FP32)
- **Datacenter GPU (NVIDIA H100)**: ~67 TFLOPS (FP64), ~1,000 TFLOPS (FP16 with Tensor Cores)
- **El Capitan supercomputer (2024)**: ~1.7 ExaFLOPS

A modern datacenter GPU performs, in **1 second**, more operations than a 1980s PC would in **30 years**.

---

## Why FLOPS matters in AI

Training AI models is, at its core, performing **trillions of multiplications on decimal numbers**. That's why the industry measures:

- **Hardware**: in TFLOPS of capacity (how many operations per second)
- **Models**: in total FLOPs to train (computational cost of training)

Example:
- **GPT-3** (training): ~3.14 × 10²³ total FLOPs
- **GPT-4** (estimated): ~10²⁵ FLOPs

The more FLOPS the hardware has, the faster the model trains. This is why GPUs dominate AI — they offer orders of magnitude more FLOPS than CPUs.

---

## FLOP precisions

Not all FLOPs are equal. There are different floating-point precisions:

| Type | Bits | Typical use |
|------|------|-------------|
| FP64 (double) | 64 | Scientific computing, high precision |
| FP32 (single) | 32 | Graphics, classical ML training |
| FP16 (half) | 16 | Modern deep learning |
| BF16 (bfloat16) | 16 | LLM training |
| FP8 / INT8 | 8 | Optimized inference |

Fewer bits = less precision, but **more FLOPS** on the same hardware. That's why modern AI models use FP16/BF16 — they trade a bit of precision for 2–4x speedup.

---

## Pocket summary

- **FLOP** = one operation on a decimal number (addition, multiplication, etc.)
- **FLOPS** = FLOPs per second, measures hardware speed
- **GPUs >> CPUs in FLOPS**, which is why they dominate AI
- **AI models** are measured in total training FLOPs
- **Fewer precision bits = more FLOPS**, ideal for deep learning

---

## References

- Patterson, D. A.; Hennessy, J. L. **Computer Architecture: A Quantitative Approach**. 6th edition. Morgan Kaufmann, 2017.
- Hennessy, J. L.; Patterson, D. A. **Computer Organization and Design: The Hardware/Software Interface**. 5th edition. Morgan Kaufmann, 2013.
- Goldberg, D. **What Every Computer Scientist Should Know About Floating-Point Arithmetic**. ACM Computing Surveys, 1991.
- IEEE 754-2019 — **Standard for Floating-Point Arithmetic**.
