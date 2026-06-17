# DFS — Depth-First Search

> Part of the **computer-science-fundamentals** repository — a series of studies on Computer Science fundamentals applied to the real world.

---

## What it is

A graph traversal algorithm that **goes as deep as possible** on each path before backtracking.

---

## How it works

Uses a **stack** or recursion:

1. Starts at the initial node
2. Goes to an unvisited neighbor
3. Then to a neighbor of that neighbor
4. And so on, diving deeper and deeper
5. When it reaches a dead end, **backtracks** to the last fork
6. Tries another path from there

Since it uses a stack (LIFO), the last path opened is the first to be explored — hence the name "depth-first search".

---

## Complexity

- Time: **O(V + E)** — V vertices, E edges
- Memory: **O(V)** — for the stack (or recursion stack) and visited set

---

## Example

Exploring a maze always going forward until hitting a dead end, going back to the last fork, trying another path. That's exactly what DFS does in a graph.

```python
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    visited.add(node)
    print(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

graph = {
    "Cleber": ["John", "Mary"],
    "John":   ["Cleber", "Peter"],
    "Mary":   ["Cleber", "Ann"],
    "Peter":  ["John"],
    "Ann":    ["Mary"]
}

dfs(graph, "Cleber")
# Cleber, John, Peter, Mary, Ann
```

Notice the difference with BFS: DFS goes deep into "John → Peter" before visiting "Mary".

---

## Real-world applications

- **Topological sort** — ordering dependencies (used in **Spark's DAG** and Airflow)
- **Cycle detection** in graphs (important for validating DAGs)
- **Maze solving** and puzzles
- **Strongly connected component detection**
- **Dependency analysis** in compilers and package managers (npm, pip)
- **Garbage collectors** use DFS to identify reachable objects

---

## References

- Cormen, T. H.; Leiserson, C. E.; Rivest, R. L.; Stein, C. **Introduction to Algorithms**. 4th edition. MIT Press, 2022.
- Sedgewick, R.; Wayne, K. **Algorithms**. 4th edition. Addison-Wesley, 2011.
- Skiena, S. **The Algorithm Design Manual**. 3rd edition. Springer, 2020.

---

*Repository: **computer-science-fundamentals** — solid fundamentals for building robust systems.*
