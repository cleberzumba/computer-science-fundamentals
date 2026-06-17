# Heap

> Part of the **computer-science-fundamentals** repository — a series of studies on Computer Science fundamentals applied to the real world.

---

## What it is

A **complete** binary tree with a special property: in a **min-heap**, the parent is always **smaller** than the children; in a **max-heap**, the parent is always **larger**. The root is always the smallest (or largest) element.

---

## How it works

The main application is implementing a **priority queue** — a queue where the highest-priority element exits first, regardless of arrival order.

Internally, the heap is usually stored in an **array**, without needing pointers:
- Parent of index `i`: `(i - 1) / 2`
- Left child: `2i + 1`
- Right child: `2i + 2`

Insertion and removal operations maintain the heap property automatically via **heapify** (moving the element up or down until reaching the correct position).

---

## Complexity

- Insert: **O(log N)**
- Remove the smallest/largest (the root): **O(log N)**
- Look at the smallest/largest: **O(1)**
- Build a heap from an array: **O(N)**

---

## Example

Min-heap with values `[1, 3, 6, 5, 9, 8]`:

```
        1
       / \
      3   6
     / \  /
    5  9 8
```

The root is always the smallest element (`1`).

```python
import heapq

heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)

heapq.heappop(heap)  # returns 1 (the smallest)
heapq.heappop(heap)  # returns 3
```

---

## Real-world applications

- **Dijkstra's algorithm** (shortest path in graphs)
- **Process scheduling** in operating systems
- **Top-K elements** (finding the K largest/smallest in a data stream)
- **Hospital triage** — most critical patients treated first
- **Huffman compression** — used in ZIP, gzip

---

## References

- Cormen, T. H.; Leiserson, C. E.; Rivest, R. L.; Stein, C. **Introduction to Algorithms**. 4th edition. MIT Press, 2022.
- Sedgewick, R.; Wayne, K. **Algorithms**. 4th edition. Addison-Wesley, 2011.
- Williams, J. W. J. **Algorithm 232: Heapsort**. Communications of the ACM, 1964.

---

*Repository: **computer-science-fundamentals** — solid fundamentals for building robust systems.*
