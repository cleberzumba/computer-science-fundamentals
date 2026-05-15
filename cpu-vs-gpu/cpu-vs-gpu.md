# CPU vs GPU


## What's the difference?

- **CPU**: few powerful cores (4–128), optimized for **sequential tasks with complex logic**. High clock (3–5 GHz), large cache.
- **GPU**: thousands of simple cores (1,000–20,000+), optimized for **the same operation on lots of data in parallel**. Lower clock (1–2 GHz), high-bandwidth memory.

The core idea: **CPU optimizes latency** (how fast one task finishes), **GPU optimizes throughput** (how many tasks per second).

Analogy: CPU is a sports car, GPU is a bus.

## Quick comparison

|                   | CPU                       | GPU                          |
|-------------------|---------------------------|------------------------------|
| Cores             | 4–128                     | 1,000–20,000+                |
| Clock             | 3–5 GHz                   | 1–2 GHz                      |
| Memory bandwidth  | ~50–100 GB/s              | ~1–3 TB/s                    |
| Best for          | Varied, sequential logic  | Same operation, lots of data |

## When to use which

**CPU**: business logic, `if/else` decisions, text processing, transactional databases, OS, web servers.

**GPU**: training/inference of neural networks, large matrix operations, graphics rendering, scientific simulations, batch image/video processing.

> **Rule of thumb**: if the task is "do this simple operation on millions of independent elements", GPU wins. If it's "follow this complex flowchart", CPU wins.

## Why GPU dominates AI

Neural networks are essentially **matrix multiplications in sequence** — exactly the kind of massively parallel workload GPUs were built for.

Training a vision model:
- CPU: days to weeks
- GPU: hours
- GPU cluster: minutes

Large LLMs are practically impossible to train on CPU.

## GPU in data engineering

Traditionally CPU territory, but Spark 3.0+ supports GPU via **RAPIDS Accelerator** (NVIDIA), with 3–10x gains on heavy joins/aggregations. Databricks offers GPU clusters for ML training and batch inference.

Not worth it for I/O-bound pipelines or simple transformations — the data transfer cost to the GPU eats the gain.

## Summary

- **CPU** = few fast cores → sequential, varied tasks
- **GPU** = many simple cores + fast memory → identical parallel tasks
- Not "which is better", but **"which is right for the task"**

## References

- Patterson & Hennessy. *Computer Architecture: A Quantitative Approach*, 6th ed.
- Kirk & Hwu. *Programming Massively Parallel Processors*, 4th ed.
- Goodfellow, Bengio & Courville. *Deep Learning*. MIT Press.
