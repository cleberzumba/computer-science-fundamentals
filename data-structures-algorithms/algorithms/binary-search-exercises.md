# Binary Search — Complexity Exercises

> Part of the **computer-science-fundamentals** repository.

---

## Formula

```
Max steps = ⌈log₂(N)⌉
```

Where N is the list size. Symbol `⌈ ⌉` = round up.

---

## Question 1

**List with 128 names. How many steps in the worst case?**

```
log₂(128) = 7
```

**Answer: 7 steps.**

---

## Question 2

**Double the list (256 names). How many steps now?**

```
log₂(256) = 8
```

**Answer: 8 steps.**

Doubling the list adds only 1 step.

---

## Question 3

**List with 100 names. How many steps in the worst case?**

```
log₂(100) ≈ 6.64  →  ⌈6.64⌉ = 7
```

**Answer: 7 steps.**

---

## Question 4

**List with 4,000,000,000 names. How many steps in the worst case?**

```
log₂(4,000,000,000) ≈ 31.9  →  ⌈31.9⌉ = 32
```

**Answer: 32 steps.**

---

## Reference table

| N (list) | Max steps |
|----------|-----------|
| 8 | 3 |
| 16 | 4 |
| 32 | 5 |
| 64 | 6 |
| 100 | 7 |
| 128 | 7 |
| 256 | 8 |
| 1,024 | 10 |
| 1,000,000 | 20 |
| 1,000,000,000 | 30 |
| 4,000,000,000 | 32 |

---

## Comparison with Linear Search

| N | Binary Search | Linear Search |
|---|---------------|---------------|
| 128 | 7 | 128 |
| 256 | 8 | 256 |
| 4 billion | 32 | 4 billion |

---

*Repository: **computer-science-fundamentals**.*
