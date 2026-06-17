# Recursion

> Part of the **computer-science-fundamentals** repository — a series of studies on Computer Science fundamentals applied to the real world.

---

## What it is

A technique where a function **calls itself** with smaller input, until reaching a **base case** that is solved directly.

---

## How it works

Every recursive function has two parts:

1. **Base case:** condition that stops the recursion (without it, the function runs forever and overflows the stack)
2. **Recursive case:** call of the function itself with a smaller problem

With each call, a new "frame" is pushed onto the **call stack**. When the function returns, the frame is popped off the stack. That's why very deep recursion can cause **stack overflow**.

**Related concepts:**
- **Memoization:** stores already-calculated results to avoid recalculation (transforms exponential recursion into linear)
- **Tail recursion:** when the recursive call is the last operation (some compilers optimize to iteration)

---

## Complexity

Depends on the algorithm:
- Badly written recursions can be **exponential** (naive Fibonacci is O(2ⁿ))
- Well-written recursions with memoization can be **O(N)**
- Recursive divide-and-conquer is usually **O(N log N)**

---

## Example

Factorial of N (`N! = N × (N-1)!`):

```python
def factorial(n):
    if n == 0:        # base case
        return 1
    return n * factorial(n - 1)   # recursive case

factorial(4)
# = 4 × factorial(3)
# = 4 × 3 × factorial(2)
# = 4 × 3 × 2 × factorial(1)
# = 4 × 3 × 2 × 1 × factorial(0)
# = 4 × 3 × 2 × 1 × 1 = 24
```

Fibonacci with memoization:

```python
def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]
```

---

## Real-world applications

- **Tree and graph traversal** (DFS is naturally recursive)
- **Divide and conquer** (merge sort, quick sort, binary search)
- **Expression parsing** in compilers and optimizers (Spark's Catalyst)
- **Backtracking** (solving mazes, sudoku, search problems)
- **File system algorithms** (traversing directories)
- **Dynamic programming** (with memoization)

---

## References

- Cormen, T. H.; Leiserson, C. E.; Rivest, R. L.; Stein, C. **Introduction to Algorithms**. 4th edition. MIT Press, 2022.
- Sedgewick, R.; Wayne, K. **Algorithms**. 4th edition. Addison-Wesley, 2011.
- Abelson, H.; Sussman, G. J. **Structure and Interpretation of Computer Programs**. 2nd edition. MIT Press, 1996.

---

*Repository: **computer-science-fundamentals** — solid fundamentals for building robust systems.*
