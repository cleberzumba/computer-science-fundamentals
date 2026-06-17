# Graphs

> Part of the **computer-science-fundamentals** repository — a series of studies on Computer Science fundamentals applied to the real world.

---

## What it is

A set of **vertices (nodes)** connected by **edges**. Unlike trees, graphs can have cycles and any node can connect to any other.

---

## How it works

**Main types:**
- **Directed:** edges have direction (A → B is different from B → A)
- **Undirected:** edges are bidirectional (A ↔ B)
- **Weighted:** edges have associated weight/cost
- **Cyclic vs Acyclic:** may or may not contain cycles

**Ways to represent in code:**
- **Adjacency list:** dictionary where each node points to its neighbors. Memory-efficient.
- **Adjacency matrix:** N×N matrix where `[i][j] = 1` if there's an edge. Fast for checking direct connections.

---

## Complexity

Depends on the algorithm applied. Typical traversals (BFS, DFS) are **O(V + E)** where V = vertices and E = edges.

| Operation | Adjacency list | Adjacency matrix |
|-----------|----------------|------------------|
| Space | O(V + E) | O(V²) |
| Add edge | O(1) | O(1) |
| Check edge | O(V) | O(1) |
| Iterate neighbors | O(degree) | O(V) |

---

## Example

Social network — people are vertices, friendships are edges.

```python
# Adjacency list
graph = {
    "Cleber": ["John", "Mary"],
    "John":   ["Cleber", "Peter"],
    "Mary":   ["Cleber", "Ann"],
    "Peter":  ["John"],
    "Ann":    ["Mary"]
}

# Cleber's friends
graph["Cleber"]  # ["John", "Mary"]
```

---

## Real-world applications

- **Social networks** — people (vertices) and friendships (edges)
- **Maps and GPS** (Waze, Google Maps) — cities and roads
- **Product recommendation** — users and items
- **Fraud analysis** — transactions between accounts
- **Spark DAG** — directed acyclic graph of transformations
- **Airflow** — workflows are DAGs
- **Google PageRank** — algorithm based on link graphs

---

## References

- Cormen, T. H.; Leiserson, C. E.; Rivest, R. L.; Stein, C. **Introduction to Algorithms**. 4th edition. MIT Press, 2022.
- Sedgewick, R.; Wayne, K. **Algorithms**. 4th edition. Addison-Wesley, 2011.
- Skiena, S. **The Algorithm Design Manual**. 3rd edition. Springer, 2020.

---

*Repository: **computer-science-fundamentals** — solid fundamentals for building robust systems.*
