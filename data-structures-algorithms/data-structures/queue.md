# Queue

> Part of the **computer-science-fundamentals** repository — a series of studies on Computer Science fundamentals applied to the real world.

---

## What it is

A **FIFO** (First In, First Out) structure — the first element to enter is the first to leave. Inserts at one end and removes from the other.

---

## How it works

Two main operations:
- `enqueue(x)`: inserts x at the end
- `dequeue()`: removes and returns the front
- `front()`: looks at the front without removing (optional)

Internally it's usually implemented with a linked list or circular array to guarantee O(1) at both ends.

**Important variations:**
- **Deque** (Double-Ended Queue): allows inserting/removing from both sides
- **Priority Queue**: elements exit by priority, not arrival order
- **Circular Queue**: reuses freed positions

---

## Complexity

- `enqueue`: **O(1)**
- `dequeue`: **O(1)**
- `front`: **O(1)**

---

## Example

A bank line. Whoever arrives first is served first. Whoever arrives later waits at the back.

```python
from collections import deque

queue = deque()
queue.append(1)     # enqueue → deque([1])
queue.append(2)     # enqueue → deque([1, 2])
queue.append(3)     # enqueue → deque([1, 2, 3])
queue.popleft()     # dequeue → returns 1, queue becomes deque([2, 3])
```

**Important:** in Python, use `collections.deque` (not `list.pop(0)`) — operations at both ends are O(1) in deque.

---

## Real-world applications

- **Message brokers** (Kafka, RabbitMQ, AWS SQS)
- **Spark Task Scheduler** — pending tasks live in queues
- **Spark Structured Streaming** — micro-batches in temporal order
- **Airflow / Databricks Jobs** — workflows waiting for execution slots
- **BFS** (Breadth-First Search) — uses a queue to explore graphs

---

## References

- Cormen, T. H.; Leiserson, C. E.; Rivest, R. L.; Stein, C. **Introduction to Algorithms**. 4th edition. MIT Press, 2022.
- Sedgewick, R.; Wayne, K. **Algorithms**. 4th edition. Addison-Wesley, 2011.
- Kleppmann, M. **Designing Data-Intensive Applications**. O'Reilly, 2017.

---

*Repository: **computer-science-fundamentals** — solid fundamentals for building robust systems.*
