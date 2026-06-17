# Bubble Sort

> Part of the **computer-science-fundamentals** repository — a series of studies on Computer Science fundamentals applied to the real world.

---

## What it is

A simple (and slow) sorting algorithm. Compares **adjacent** pairs and swaps if out of order. Repeats until the list is sorted.

---

## How it works

In each pass through the list, the largest element "bubbles up" to the end. Hence the name.

1. Iterate through the list from start to end
2. Compare each adjacent pair
3. If the left one is larger, swap
4. Repeat N times (or until no more swaps occur)

---

## Complexity

- Worst case: **O(N²)**
- Average case: **O(N²)**
- Best case (already sorted list with optimization): **O(N)**
- Memory: **O(1)** — sorts in place

---

## Example

Sorting `[3, 1, 4, 2]`:

```
Pass 1:
[3, 1, 4, 2] → compare 3 and 1 → swap → [1, 3, 4, 2]
[1, 3, 4, 2] → compare 3 and 4 → ok   → [1, 3, 4, 2]
[1, 3, 4, 2] → compare 4 and 2 → swap → [1, 3, 2, 4]

Pass 2:
[1, 3, 2, 4] → compare 1 and 3 → ok   → [1, 3, 2, 4]
[1, 3, 2, 4] → compare 3 and 2 → swap → [1, 2, 3, 4]
[1, 2, 3, 4] → compare 3 and 4 → ok   → [1, 2, 3, 4] ✓
```

```python
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

bubble_sort([3, 1, 4, 2])  # [1, 2, 3, 4]
```

---

## Real-world applications

- Practically **none in production** — it's too slow
- Used in **teaching** because it's easy to understand
- Useful for very small lists (up to ~10 elements) when simplicity matters more than performance

---

## References

- Cormen, T. H.; Leiserson, C. E.; Rivest, R. L.; Stein, C. **Introduction to Algorithms**. 4th edition. MIT Press, 2022.
- Sedgewick, R.; Wayne, K. **Algorithms**. 4th edition. Addison-Wesley, 2011.
- Knuth, D. E. **The Art of Computer Programming, Volume 3: Sorting and Searching**. 2nd edition. Addison-Wesley, 1998.

---

*Repository: **computer-science-fundamentals** — solid fundamentals for building robust systems.*
