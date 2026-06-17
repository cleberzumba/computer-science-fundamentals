# Stack

> Part of the **computer-science-fundamentals** repository — a series of studies on Computer Science fundamentals applied to the real world.

---

## What it is

A **LIFO** (Last In, First Out) structure — the last element to enter is the first to leave. Only allows insertion and removal **at the top**.

---

## How it works

Two main operations:
- `push(x)`: pushes x onto the top
- `pop()`: removes and returns the top
- `peek()`: looks at the top without removing (optional)

Internally it's usually implemented with a dynamic array or linked list. Insertion and removal operations always happen at the same end.

---

## Complexity

- `push`: **O(1)**
- `pop`: **O(1)**
- `peek`: **O(1)**

---

## Example

A stack of plates. You stack them one by one and, when you need one, take the one on top. The plate at the bottom only comes out after all the others.

```python
stack = []
stack.append(1)     # push → [1]
stack.append(2)     # push → [1, 2]
stack.append(3)     # push → [1, 2, 3]
stack.pop()         # removes and returns 3 → [1, 2]
stack[-1]           # peek → returns 2
```

---

## Real-world applications

- **Function call stack** (every function call is pushed onto it)
- **Undo/Redo** in editors
- **Browser history** (back button)
- **Mathematical expression evaluation** in compilers
- Spark's **Catalyst Optimizer** uses a stack to traverse expression trees

---

## References

- Cormen, T. H.; Leiserson, C. E.; Rivest, R. L.; Stein, C. **Introduction to Algorithms**. 4th edition. MIT Press, 2022.
- Sedgewick, R.; Wayne, K. **Algorithms**. 4th edition. Addison-Wesley, 2011.
- Aho, A. V.; Lam, M. S.; Sethi, R.; Ullman, J. D. **Compilers: Principles, Techniques, and Tools**. 2nd edition. Pearson, 2006.

---

*Repository: **computer-science-fundamentals** — solid fundamentals for building robust systems.*
