# Linked Lists

> Part of the **computer-science-fundamentals** repository — a series of studies on Computer Science fundamentals applied to the real world.

---

## What it is

A sequence of **nodes** connected by pointers. Each node contains a value and a reference to the next node (or to the previous one, in doubly linked lists).

---

## How it works

Unlike arrays, nodes **are not in contiguous memory**. To access node 5, you have to start from the first and follow the pointers one by one. In exchange, inserting/removing is fast — just adjust two pointers.

**Main types:**
- **Singly Linked List:** each node points only to the next
- **Doubly Linked List:** each node points to the next and to the previous
- **Circular Linked List:** the last node points back to the first

---

## Complexity

- Index access: **O(N)** (requires traversal)
- Insertion/removal at the beginning: **O(1)**
- Insertion/removal in the middle (knowing the position): **O(1)**
- Search by value: **O(N)**

---

## Example

```
[10] → [20] → [30] → None
```

To reach `30`, start from `10`, follow pointer to `20`, follow pointer to `30`.

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Creating: 10 → 20 → 30
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n1.next = n2
n2.next = n3
```

---

## Real-world applications

- Internal implementation of queues and stacks in some languages
- Task lists in the operating system kernel
- Browser navigation history (doubly linked list)
- Structures that need fast insertion/removal at any position

---

## References

- Cormen, T. H.; Leiserson, C. E.; Rivest, R. L.; Stein, C. **Introduction to Algorithms**. 4th edition. MIT Press, 2022.
- Sedgewick, R.; Wayne, K. **Algorithms**. 4th edition. Addison-Wesley, 2011.
- Knuth, D. E. **The Art of Computer Programming, Volume 1: Fundamental Algorithms**. 3rd edition. Addison-Wesley, 1997.

---

*Repository: **computer-science-fundamentals** — solid fundamentals for building robust systems.*
