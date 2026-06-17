# Binary Search

> Part of the **computer-science-fundamentals** repository — a series of studies on Computer Science fundamentals applied to the real world.

---

## What it is

A search algorithm **much more efficient** than linear, but requires the list to be **sorted**. Divides the search interval in half at each step.

---

## How it works

1. Look at the middle element
2. If it's the one searched, done
3. If the searched is smaller, discard the right half and repeat on the left
4. If larger, discard the left and repeat on the right
5. Continue dividing until found or exhausted

At each step, **half of the remaining elements is discarded**. That's why complexity is logarithmic.

---

## Complexity

- Worst case: **O(log N)**
- In a 1 million element list: at most 20 comparisons
- In a 1 billion element list: at most 30 comparisons

---

## Example

Searching for `7` in `[1, 3, 5, 7, 9, 11, 13]`:

```
middle = 7  → found in 1 comparison
```

Searching for `11`:

```
middle = 7   → 11 > 7, discard left
middle = 11  → found
```

```python
def binary_search(lst, target):
    start, end = 0, len(lst) - 1
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

binary_search([1, 3, 5, 7, 9, 11, 13], 11)  # returns 5
```

---

## Real-world applications

- **Database indexes** (B-trees use binary search internally)
- **Search in sorted arrays** in any language
- **Looking up a word in a dictionary** — humans do binary search intuitively
- **Git bisect** — finds the commit that introduced a bug via binary search
- **Spark** uses binary search to locate sorted data partitions

---

## References

- Cormen, T. H.; Leiserson, C. E.; Rivest, R. L.; Stein, C. **Introduction to Algorithms**. 4th edition. MIT Press, 2022.
- Sedgewick, R.; Wayne, K. **Algorithms**. 4th edition. Addison-Wesley, 2011.
- Knuth, D. E. **The Art of Computer Programming, Volume 3: Sorting and Searching**. 2nd edition. Addison-Wesley, 1998.

---

*Repository: **computer-science-fundamentals** — solid fundamentals for building robust systems.*
