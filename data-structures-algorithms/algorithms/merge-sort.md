# Merge Sort

> Part of the **computer-science-fundamentals** repository — a series of studies on Computer Science fundamentals applied to the real world.

---

## What it is

An **efficient and stable** sorting algorithm, based on the **"divide and conquer"** strategy.

---

## How it works

1. **Divides** the list in half recursively
2. Continues dividing until having 1-element lists (which are already "sorted")
3. **Merges** pairs of sorted lists, always comparing the first elements of each
4. Continues merging until reconstructing the entire sorted list

The genius is in the **merge** phase: combining two sorted lists into one sorted list is O(N).

---

## Complexity

- Worst case: **O(N log N)** guaranteed
- Average case: **O(N log N)**
- Best case: **O(N log N)**
- Memory: **O(N)** — needs extra space to merge

---

## Example

Sorting `[3, 1, 4, 2]`:

```
Divide: [3, 1]   [4, 2]
Divide: [3] [1]  [4] [2]
Merge:  [1, 3]   [2, 4]
Merge:  [1, 2, 3, 4]
```

```python
def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

merge_sort([3, 1, 4, 2])  # [1, 2, 3, 4]
```

---

## Real-world applications

- **External sort** — sorting large files that don't fit in memory
- **Spark uses merge sort** internally in operations like `sortBy` and `sortMergeJoin`
- **Databases** use merge sort for large orderings
- When you need **O(N log N) guarantee** even in the worst case
- **Stable** sort — preserves relative order of equal elements (important in multiple sortings)

---

## References

- Cormen, T. H.; Leiserson, C. E.; Rivest, R. L.; Stein, C. **Introduction to Algorithms**. 4th edition. MIT Press, 2022.
- Sedgewick, R.; Wayne, K. **Algorithms**. 4th edition. Addison-Wesley, 2011.
- Knuth, D. E. **The Art of Computer Programming, Volume 3: Sorting and Searching**. 2nd edition. Addison-Wesley, 1998.

---

*Repository: **computer-science-fundamentals** — solid fundamentals for building robust systems.*
