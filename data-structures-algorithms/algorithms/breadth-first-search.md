# BFS — Breadth-First Search

> Part of the **computer-science-fundamentals** repository — a series of studies on Computer Science fundamentals applied to the real world.

---

## What it is

A graph (or tree) traversal algorithm that explores nodes **level by level**, starting from the initial node.

---

## How it works

Uses a **queue**:

1. Places the initial node in the queue
2. In a loop:
   - Removes the first node from the queue
   - Marks it as visited
   - Adds all unvisited neighbors to the end of the queue
3. Continues until the queue is empty

Since it uses a queue (FIFO), it explores all nearby nodes before going further — hence the name "breadth-first search".

---

## Complexity

- Time: **O(V + E)** — V vertices, E edges
- Memory: **O(V)** — for the queue and visited set

---

## Example

In a social network, finding all friends of friends of Cleber:

```
Level 0: Cleber
Level 1: direct friends (John, Mary, Peter)
Level 2: friends of friends (all friends of John, Mary, Peter)
```

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

graph = {
    "Cleber": ["John", "Mary"],
    "John":   ["Cleber", "Peter"],
    "Mary":   ["Cleber", "Ann"],
    "Peter":  ["John"],
    "Ann":    ["Mary"]
}

bfs(graph, "Cleber")
# Cleber, John, Mary, Peter, Ann
```

---

## Real-world applications

- **Shortest path** in unweighted graphs
- **Degrees of separation** in social networks (LinkedIn, Facebook)
- **Web crawlers** — Google explores the web breadth-first
- **GPS** — finding the shortest route in number of "hops"
- **Connected component detection** in graphs
- **Puzzle solving** (Rubik's cube, board games)

---

## References

- Cormen, T. H.; Leiserson, C. E.; Rivest, R. L.; Stein, C. **Introduction to Algorithms**. 4th edition. MIT Press, 2022.
- Sedgewick, R.; Wayne, K. **Algorithms**. 4th edition. Addison-Wesley, 2011.
- Skiena, S. **The Algorithm Design Manual**. 3rd edition. Springer, 2020.

---

*Repository: **computer-science-fundamentals** — solid fundamentals for building robust systems.*
