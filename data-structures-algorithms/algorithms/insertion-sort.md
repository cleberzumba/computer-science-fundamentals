# Insertion Sort

> Part of the **computer-science-fundamentals** repository — a series of studies on Computer Science fundamentals applied to the real world.

---

## What it is

An algorithm that builds the sorted list **one element at a time**, inserting each new element in the correct position among those already sorted.

---

## How it works

1. Considers the first element as already sorted
2. Takes the second and inserts it in the right position relative to the first
3. Takes the third and inserts it in the right position between the first two
4. And so on

At each step, the left side of the list is always sorted.

---

## Complexity

- Worst case: **O(N²)** — list in reverse order
- Average case: **O(N²)**
- Best case: **O(N)** — nearly sorted list
- Memory: **O(1)** — sorts in place

**Important advantage:** very efficient for **nearly sorted** lists.

---

## Example

Sorting `[3, 1, 4, 2]` like organizing cards in your hand:

```
[3]                ← start with 3
[1, 3]             ← insert 1 before 3
[1, 3, 4]          ← 4 is already in position
[1, 2, 3, 4]       ← insert 2 between 1 and 3
```

```python
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

insertion_sort([3, 1, 4, 2])  # [1, 2, 3, 4]
```

---

## Real-world applications

- **Timsort** (Python and Java sort) uses insertion sort for small sub-lists
- Small lists in general
- Lists that arrive **nearly sorted** (e.g., sorted data with few out-of-place elements)
- Online algorithms — when receiving streamed data and needing to maintain sort order

---

## References

- Cormen, T. H.; Leiserson, C. E.; Rivest, R. L.; Stein, C. **Introduction to Algorithms**. 4th edition. MIT Press, 2022.
- Sedgewick, R.; Wayne, K. **Algorithms**. 4th edition. Addison-Wesley, 2011.
- Knuth, D. E. **The Art of Computer Programming, Volume 3: Sorting and Searching**. 2nd edition. Addison-Wesley, 1998.

---

*Repository: **computer-science-fundamentals** — solid fundamentals for building robust systems.*
