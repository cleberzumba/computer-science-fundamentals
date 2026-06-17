# Quick Sort

> Part of the **computer-science-fundamentals** repository — a series of studies on Computer Science fundamentals applied to the real world.

---

## What it is

A sorting algorithm **fast in practice**, also based on "divide and conquer". It's the most used sort in language libraries.

---

## How it works

1. Chooses an element as a **pivot**
2. Reorganizes the list so that values smaller than the pivot go to the **left** and larger ones go to the **right** (operation called **partition**)
3. Recursively applies the same process on each side
4. When all sub-lists are trivial (1 element), the list is sorted

Pivot choice is critical. Good strategies: random pivot or median of three elements.

---

## Complexity

- Average case: **O(N log N)**
- Worst case (badly chosen pivot): **O(N²)**
- Memory: **O(log N)** (recursive call stack)

Despite the bad worst case, in practice quick sort is usually **faster than merge sort** because it sorts in place and has good cache locality.

---

## Example

Sorting `[3, 1, 4, 2]` with pivot = 3:

```
[1, 2] [3] [4]      ← partition around 3
[1, 2]              ← pivot = 1 → [] [1] [2]
[2]                 ← already sorted
Result: [1, 2, 3, 4]
```

```python
def quick_sort(lst):
    if len(lst) <= 1:
        return lst

    pivot = lst[len(lst) // 2]
    smaller = [x for x in lst if x < pivot]
    equal = [x for x in lst if x == pivot]
    larger = [x for x in lst if x > pivot]

    return quick_sort(smaller) + equal + quick_sort(larger)

quick_sort([3, 1, 4, 2])  # [1, 2, 3, 4]
```

---

## Real-world applications

- **Default sort** in many languages (C, C++, Rust)
- **Pandas/Polars DataFrames** use quick sort variants
- In-memory sorting of **medium and large datasets**
- Algorithms like **quickselect** (find the K-th smallest) are derived from quick sort

---

## References

- Cormen, T. H.; Leiserson, C. E.; Rivest, R. L.; Stein, C. **Introduction to Algorithms**. 4th edition. MIT Press, 2022.
- Sedgewick, R.; Wayne, K. **Algorithms**. 4th edition. Addison-Wesley, 2011.
- Hoare, C. A. R. **Algorithm 64: Quicksort**. Communications of the ACM, 1961.

---

*Repository: **computer-science-fundamentals** — solid fundamentals for building robust systems.*
