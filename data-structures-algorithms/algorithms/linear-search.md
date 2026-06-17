# Linear Search

> Part of the **computer-science-fundamentals** repository — a series of studies on Computer Science fundamentals applied to the real world.

---

## What it is

The simplest search algorithm. Goes through the structure **from start to end**, comparing each element with the searched value.

---

## How it works

Starts at the first element, tests one by one. Returns the position when found. If it reaches the end without finding, returns that it doesn't exist.

Doesn't require the list to be sorted — works on any sequential structure.

---

## Complexity

- Best case: **O(1)** — found at the first position
- Worst case: **O(N)** — needs to traverse everything
- Average case: **O(N/2)** → **O(N)**

---

## Example

Searching for the number `25` in `[10, 7, 25, 3, 18]`:

```
position 0: 10 ≠ 25
position 1:  7 ≠ 25
position 2: 25 = 25 ✓ found!
```

```python
def linear_search(lst, target):
    for i, value in enumerate(lst):
        if value == target:
            return i
    return -1

linear_search([10, 7, 25, 3, 18], 25)  # returns 2
```

---

## Real-world applications

- Search in small lists (up to a few hundred elements)
- Unsorted lists where sorting would cost more than searching
- Structures where random access isn't available (linked lists)
- When you'll only do one search — not worth sorting first

---

## References

- Cormen, T. H.; Leiserson, C. E.; Rivest, R. L.; Stein, C. **Introduction to Algorithms**. 4th edition. MIT Press, 2022.
- Sedgewick, R.; Wayne, K. **Algorithms**. 4th edition. Addison-Wesley, 2011.
- Knuth, D. E. **The Art of Computer Programming, Volume 3: Sorting and Searching**. 2nd edition. Addison-Wesley, 1998.

---

*Repository: **computer-science-fundamentals** — solid fundamentals for building robust systems.*
