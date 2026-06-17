# Arrays / Lists

> Part of the **computer-science-fundamentals** repository — a series of studies on Computer Science fundamentals applied to the real world.

---

## What it is

An ordered collection of elements of the same type, stored in **contiguous memory positions** and accessed by **numeric index** starting at 0.

---

## How it works

The computer reserves a continuous block of memory. To access the element at position `i`, it calculates `base_address + i × element_size`. That's why access is instantaneous.

**Classic array:** has a fixed size, defined at creation.
**List (dynamic):** adjusts size automatically as you add or remove elements. Under the hood, it still uses an array — when full, it creates a larger array and copies the data.

---

## Complexity

- Index access: **O(1)**
- Search by value: **O(N)**
- Insertion/removal at the end (in dynamic list): **O(1) amortized**
- Insertion/removal in the middle: **O(N)** (requires shifting elements)

---

## Example

```python
my_list = [10, 20, 30, 40]

my_list[2]            # returns 30 immediately — O(1)
my_list.append(50)    # [10, 20, 30, 40, 50] — O(1)
my_list.insert(0, 5)  # [5, 10, 20, 30, 40, 50] — O(N), shifts everything
```

---

## Real-world applications

- Base structure for most other data structures (stacks, queues, heaps use arrays internally)
- DataFrames in pandas/PySpark are arrays under the hood
- I/O buffers, video frames, audio samples

---

## References

- Cormen, T. H.; Leiserson, C. E.; Rivest, R. L.; Stein, C. **Introduction to Algorithms**. 4th edition. MIT Press, 2022.
- Sedgewick, R.; Wayne, K. **Algorithms**. 4th edition. Addison-Wesley, 2011.
- Skiena, S. **The Algorithm Design Manual**. 3rd edition. Springer, 2020.

---

*Repository: **computer-science-fundamentals** — solid fundamentals for building robust systems.*
