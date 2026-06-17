# Selection Sort

> Part of the **computer-science-fundamentals** repository — a series of studies on Computer Science fundamentals applied to the real world.

---

## What it is

A sorting algorithm that finds the **smallest element in the list** and places it in the first position, then the second smallest in the second position, and so on.

---

## How it works

1. Scan the entire list to find the smallest element
2. Swap with position 0
3. Scan the rest (from position 1 onward), find the second smallest
4. Swap with position 1
5. Repeat N times

In each pass, one position becomes "fixed" with the correct value.

---

## Complexity

- Worst case: **O(N²)**
- Average case: **O(N²)**
- Best case: **O(N²)** (does the same comparisons even if already sorted)
- Memory: **O(1)** — sorts in place

---

## Example

Sorting `[3, 1, 4, 2]`:

```
Find smallest = 1 → swap with position 0 → [1, 3, 4, 2]
Find smallest (from index 1) = 2 → swap → [1, 2, 4, 3]
Find smallest (from index 2) = 3 → swap → [1, 2, 3, 4]
```

```python
def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst

selection_sort([3, 1, 4, 2])  # [1, 2, 3, 4]
```

---

## Real-world applications

- Rarely used in production — also O(N²)
- Educational
- Useful when the cost of **swapping elements is high** (selection sort does at most N swaps, fewer than bubble sort)
- Good for small lists on embedded systems with little memory

---

## References

- Cormen, T. H.; Leiserson, C. E.; Rivest, R. L.; Stein, C. **Introduction to Algorithms**. 4th edition. MIT Press, 2022.
- Sedgewick, R.; Wayne, K. **Algorithms**. 4th edition. Addison-Wesley, 2011.
- Knuth, D. E. **The Art of Computer Programming, Volume 3: Sorting and Searching**. 2nd edition. Addison-Wesley, 1998.

---

*Repository: **computer-science-fundamentals** — solid fundamentals for building robust systems.*
