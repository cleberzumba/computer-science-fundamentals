# Stack and Queue: Fundamentals, Differences, and Real-World Applications

> Part of the [computer-science-fundamentals](https://github.com/) repository — a series of in-depth studies on Computer Science fundamentals applied to the real world, especially in distributed systems and data engineering.

---

## Table of Contents

- [Introduction](#introduction)
- [Formal Definitions](#formal-definitions)
- [Stack — LIFO](#stack--lifo)
- [Queue — FIFO](#queue--fifo)
- [Implementation in Python](#implementation-in-python)
- [Important Variations](#important-variations)
- [Conclusion](#conclusion)

---

## Introduction

Stack and Queue are two of the most fundamental data structures in Computer Science. Although simple on the surface, they sit behind virtually every modern computing system: from the internal workings of the JVM to task scheduling in Apache Spark clusters, including message brokers like Kafka, search engines, compilers, and graph algorithms.

The difference between the two boils down to the order in which elements are removed:

- **Stack:** the last element inserted is the first to be removed (LIFO — Last In, First Out)
- **Queue:** the first element inserted is the first to be removed (FIFO — First In, First Out)

This small difference in access policy produces radically different behaviors — and each one solves distinct problems.

---

## Formal Definitions

Both are **linear data structures** (elements organized in sequence) with **restricted access** — you don't access elements in the middle, only through the endpoints defined by the structure.

This restriction is not an accidental limitation: it's precisely what guarantees constant-time O(1) operations and the behavioral predictability that makes these structures so useful in critical systems.

---

## Stack — LIFO

### Concept

Picture a stack of plates in the kitchen. You stack plates one on top of another. When you need one, you take the top plate — the last one placed. The bottom plate only comes out after all the others have been removed.

### Main Operations

| Operation | Description |
|---|---|
| `push(x)` | Inserts x on the top |
| `pop()` | Removes and returns the top element |
| `peek()` | Returns the top element without removing it |
| `is_empty()` | Checks whether the stack is empty |

### Step-by-Step Example

```
Initial state: [ ]
push(1)  →  [1]
push(2)  →  [1, 2]
push(3)  →  [1, 2, 3]
peek()   →  returns 3, stack stays [1, 2, 3]
pop()    →  returns 3, stack becomes [1, 2]
pop()    →  returns 2, stack becomes [1]
```

### Visual Representation

```
 ┌───┐
 │ 3 │  ← top (input and output)
 ├───┤
 │ 2 │
 ├───┤
 │ 1 │  ← bottom
 └───┘
```

---

## Queue — FIFO

### Concept

Picture a line at a bank. The first person to arrive is the first to be served. Whoever arrives later waits at the back. Arrival order = departure order.

### Main Operations

| Operation | Description |
|---|---|
| `enqueue(x)` | Inserts x at the back |
| `dequeue()` | Removes and returns the front element |
| `front()` | Returns the front element without removing it |
| `is_empty()` | Checks whether the queue is empty |

### Step-by-Step Example

```
Initial state: [ ]
enqueue(1)  →  [1]
enqueue(2)  →  [1, 2]
enqueue(3)  →  [1, 2, 3]
front()     →  returns 1, queue stays [1, 2, 3]
dequeue()   →  returns 1, queue becomes [2, 3]
dequeue()   →  returns 2, queue becomes [3]
```

### Visual Representation

```
  input                output
    ↓                    ↓
 ┌───┬───┬───┐
 │ 3 │ 2 │ 1 │
 └───┴───┴───┘
  back              front
```

---

## Implementation in Python

### Stack — using `list` is efficient

Python's built-in `list` works perfectly as a stack, since `append` and `pop` (without index) are O(1):

```python
# Stack with list
stack = []
stack.append(1)  # push
stack.append(2)
stack.append(3)
print(stack)      # [1, 2, 3]

top = stack.pop() # returns 3 (LIFO)
print(stack)      # [1, 2]

# Peek: look without removing
print(stack[-1])  # 2
```

### Queue — do NOT use `list`, use `deque`

Using `list.pop(0)` looks intuitive, but it's O(n) — Python has to shift every element on each removal. On large lists, this destroys performance.

The correct solution is `collections.deque`, optimized for operations on both ends:

```python
from collections import deque

# Queue with deque
queue = deque()
queue.append(1)    # enqueue (at the back)
queue.append(2)
queue.append(3)
print(queue)       # deque([1, 2, 3])

first = queue.popleft()  # dequeue (from the front) — O(1)
print(first)       # 1
print(queue)       # deque([2, 3])
```

### Performance comparison: `list` vs `deque` as queue

```python
import time
from collections import deque

n = 100_000

# Using list (wrong)
lst = list(range(n))
start = time.time()
while lst:
    lst.pop(0)
print(f"list.pop(0): {time.time() - start:.4f}s")

# Using deque (correct)
dq = deque(range(n))
start = time.time()
while dq:
    dq.popleft()
print(f"deque.popleft(): {time.time() - start:.4f}s")
```

> Typical result: `deque` is dozens to hundreds of times faster for this case. This kind of detail separates code that scales from code that breaks in production.

### Manual implementation (educational)

For learning purposes, it's worth implementing both from scratch at least once:

```python
class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        if not self._items:
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)


class Queue:
    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if not self._items:
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()

    def front(self):
        if not self._items:
            raise IndexError("front from empty queue")
        return self._items[0]

    def is_empty(self):
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)
```

---

## Important Variations

### Deque (Double-Ended Queue)

Allows insertion and removal at both ends. It's the structure behind Python's `collections.deque` and can work as either stack or queue, depending on how it's used.

```python
from collections import deque

d = deque([1, 2, 3])
d.appendleft(0)  # [0, 1, 2, 3]
d.append(4)      # [0, 1, 2, 3, 4]
d.pop()          # remove from the back
d.popleft()      # remove from the front
```

### Priority Queue

Elements leave by priority, not by arrival order. Typically implemented with a binary heap (`heapq` in Python). Insertion and removal operations have O(log n) complexity.

```python
import heapq

pq = []
heapq.heappush(pq, (2, "medium task"))
heapq.heappush(pq, (1, "urgent task"))
heapq.heappush(pq, (3, "low task"))

heapq.heappop(pq)  # (1, 'urgent task') — smallest value comes out first
```

> Appears in schedulers that prioritize critical tasks (e.g., some configurations of Spark's FairScheduler, OS schedulers, routing algorithms).

### Circular Queue

Reuses freed positions, avoiding shifts. Useful in fixed-size buffers (e.g., network buffers, log ring buffers in high-performance systems).

### Blocking Queue

Thread-safe variation used in concurrent programming. When empty, `dequeue` blocks the calling thread until an element is available. When full (in bounded queues), `enqueue` blocks. It's the structure behind task pools in concurrent systems — including the JVM internals used by Spark.

---

## Conclusion

Stack and Queue are seemingly simple structures, but deeply understanding them is a turning point in data engineering and distributed systems.

**Pocket summary:**

- Stack = LIFO = input and output at the top = stack of plates
- Queue = FIFO = input on one side, output on the other = bank line
- Both O(1) on main operations, as long as properly implemented (in Python: `list` for stack, `deque` for queue)

Every time you use Kafka, schedule a task on Spark, run a recursive function, or click "undo" in an editor, these structures are working silently underneath. Understanding them is not an academic exercise — it's grasping the foundation on which modern systems are built.

---

## References and Further Reading

- Cormen, T. H. et al. *Introduction to Algorithms (CLRS)*, chapter on elementary data structures.
- Sedgewick, R. *Algorithms*, 4th edition — chapters on stacks and queues.
- Official Python documentation: [`collections.deque`](https://docs.python.org/3/library/collections.html#collections.deque), [`heapq`](https://docs.python.org/3/library/heapq.html).
- [Apache Spark internals: Job Scheduling](https://spark.apache.org/docs/latest/job-scheduling.html).
