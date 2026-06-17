# Big O Notation

> Part of the **computer-science-fundamentals** repository — a series of studies on Computer Science fundamentals applied to the real world.

---

## What it is

Mathematical notation that describes **how the time (or memory) of an algorithm grows as the input size N increases**. It's the standard way to compare algorithms.

---

## How it works

Considers the **worst case** and discards constants and smaller terms. An algorithm that performs `3N + 5` operations is classified as **O(N)**, because the growth is linear.

The analysis focuses on "how much worse it gets as input grows", not on absolute time. An O(N) algorithm can be slower than an O(N²) for small N — but for large N, O(N) always wins.

---

## Main classes (from fastest to slowest)

| Notation | Name | Example |
|----------|------|---------|
| O(1) | Constant | Accessing `array[i]` |
| O(log N) | Logarithmic | Binary search |
| O(N) | Linear | Iterating through a list |
| O(N log N) | Linearithmic | Merge sort, quick sort |
| O(N²) | Quadratic | Bubble sort, two nested loops |
| O(2ⁿ) | Exponential | Some recursive solutions (naive Fibonacci) |
| O(N!) | Factorial | Permutations |

---

## Example

Iterating through a 1,000-element list with a loop is **O(N)** — 1,000 operations.

If it's `O(N²)`, that's 1,000,000 operations.

For N = 1 million:
- **O(N)**: 1,000,000 operations → milliseconds
- **O(N²)**: 1,000,000,000,000 operations → hours

That's why notation matters: for large N, the difference is enormous.

---

## Real-world applications

- **Data structure choices** in production code
- **SQL query optimization** — thinking about join complexity
- **Spark/Big Data** — O(N²) algorithms make large datasets infeasible
- **Technical interviews** at top companies — complexity is always asked
- **System design** — analyzing solution scalability

---

## References

- Cormen, T. H.; Leiserson, C. E.; Rivest, R. L.; Stein, C. **Introduction to Algorithms**. 4th edition. MIT Press, 2022.
- Sedgewick, R.; Wayne, K. **Algorithms**. 4th edition. Addison-Wesley, 2011.
- Knuth, D. E. **The Art of Computer Programming, Volume 1: Fundamental Algorithms**. 3rd edition. Addison-Wesley, 1997.

---

*Repository: **computer-science-fundamentals** — solid fundamentals for building robust systems.*
