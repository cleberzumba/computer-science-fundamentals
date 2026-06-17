# Data Structures and Algorithms: Fundamentals

> Part of the **computer-science-fundamentals** repository — a series of studies on Computer Science fundamentals applied to the real world.

---

## Table of Contents

- [Introduction](#introduction)
- [Data Structures](#data-structures)
  - [Arrays / Lists](#arrays--lists)
  - [Linked Lists](#linked-lists)
  - [Stack](#stack)
  - [Queue](#queue)
  - [Hash Tables](#hash-tables)
  - [Trees](#trees)
  - [Heap](#heap)
  - [Graphs](#graphs)
- [Algorithms](#algorithms)
  - [Big O Notation](#big-o-notation)
  - [Linear Search](#linear-search)
  - [Binary Search](#binary-search)
  - [Bubble Sort](#bubble-sort)
  - [Selection Sort](#selection-sort)
  - [Insertion Sort](#insertion-sort)
  - [Merge Sort](#merge-sort)
  - [Quick Sort](#quick-sort)
  - [Recursion](#recursion)
  - [BFS — Breadth-First Search](#bfs--breadth-first-search)
  - [DFS — Depth-First Search](#dfs--depth-first-search)
- [References](#references)

---

## Introduction

Data structures and algorithms are the **foundation of any serious computing professional**. Mastering these fundamentals is what separates those who write code from those who understand what the code actually does.

This document covers the classical fundamentals: what each structure/algorithm is, how it works, its computational complexity, and a concrete example.

---

## Data Structures

### Arrays / Lists

**What it is:** an ordered collection of elements of the same type, stored in **contiguous memory positions** and accessed by **numeric index** starting at 0.

**How it works:** the computer reserves a continuous block of memory. To access the element at position `i`, it calculates `base_address + i × element_size`. That's why access is instantaneous.

**Complexity:**
- Index access: **O(1)**
- Search by value: **O(N)**
- Insertion/removal in the middle: **O(N)** (requires shifting elements)

**Example:**
```python
my_list = [10, 20, 30, 40]
my_list[2]  # returns 30 immediately
my_list.append(50)  # [10, 20, 30, 40, 50]
```

---

### Linked Lists

**What it is:** a sequence of **nodes** connected by pointers. Each node contains a value and a reference to the next node (or to the previous one, in doubly linked lists).

**How it works:** unlike arrays, nodes **are not in contiguous memory**. To access node 5, you have to start from the first and follow the pointers one by one. In exchange, inserting/removing is fast — just adjust two pointers.

**Complexity:**
- Index access: **O(N)** (requires traversal)
- Insertion/removal at the beginning: **O(1)**
- Insertion/removal in the middle (knowing the position): **O(1)**

**Example:**
```
[10] → [20] → [30] → None
```
To reach `30`, start from `10`, follow pointer to `20`, follow pointer to `30`.

---

### Stack

**What it is:** a **LIFO** (Last In, First Out) structure — the last element to enter is the first to leave. Only allows insertion and removal **at the top**.

**How it works:** two main operations:
- `push(x)`: pushes x onto the top
- `pop()`: removes and returns the top

**Complexity:** push and pop are **O(1)**.

**Real-world applications:** function call stack, undo/redo, browser history.

**Example:** a stack of plates. You stack them one by one and, when you need one, take the one on top. The plate at the bottom only comes out after all the others.

---

### Queue

**What it is:** a **FIFO** (First In, First Out) structure — the first element to enter is the first to leave. Inserts at one end and removes from the other.

**How it works:** two main operations:
- `enqueue(x)`: inserts x at the end
- `dequeue()`: removes and returns the front

**Complexity:** enqueue and dequeue are **O(1)**.

**Real-world applications:** print queues, messages in Kafka/RabbitMQ, task scheduling in Spark.

**Example:** a bank line. Whoever arrives first is served first. Whoever arrives later waits at the back.

---

### Hash Tables

**What it is:** a **key-value** structure that maps a unique key to an associated value. Allows search, insertion, and removal in average **O(1)** time.

**How it works:** when you insert a key, a **hash function** transforms the key into a number indicating the position (bucket) where the value will be stored. To search, the same hash function is applied and you go directly to the position. If two keys generate the same position (collision), chaining or other strategies are used.

**Complexity:**
- Insertion, search, removal: **O(1) on average**
- Worst case (many collisions): **O(N)**

**Real-world applications:** Python dictionaries, database indexes, caches, joins in Spark (broadcast hash join).

**Example:**
```python
person = {"name": "Cleber", "age": 48, "country": "Brazil"}
person["name"]  # returns "Cleber" instantly
```

---

### Trees

**What it is:** a **hierarchical** structure with a root node at the top and child nodes below, forming a tree. Each node can have zero or more children, but only one parent.

**How it works:** the most common structure is the **Binary Search Tree (BST)**: each node has at most two children, values smaller than the parent go to the left, larger ones go to the right. This allows search by successive division.

**Complexity (in balanced BST):**
- Search, insertion, removal: **O(log N)**
- Worst case (degenerate tree): **O(N)**

**Real-world applications:** database indexes (B-trees), file systems, expression parsing (Spark's Catalyst), HTML DOM.

**Example:** a BST with values `[8, 3, 10, 1, 6, 14]`:
```
        8
       / \
      3   10
     / \    \
    1   6    14
```
Searching for `6`: start at `8` → `6 < 8`, go left → `3` → `6 > 3`, go right → find `6`.

---

### Heap

**What it is:** a **complete** binary tree with a special property: in a **min-heap**, the parent is always **smaller** than the children; in a **max-heap**, the parent is always **larger**. The root is always the smallest (or largest) element.

**How it works:** the main application is implementing a **priority queue** — a queue where the highest-priority element exits first, regardless of arrival order. Insertion and removal operations maintain the heap property automatically.

**Complexity:**
- Insert: **O(log N)**
- Remove the smallest/largest: **O(log N)**
- Look at the smallest/largest: **O(1)**

**Real-world applications:** Dijkstra's algorithm (shortest path), OS process scheduling, top-K elements.

**Example:** hospital triage. Patients arrive in random order, but the system always treats the most critical one first. The heap keeps the most critical at the top, ready to be removed in O(log N).

---

### Graphs

**What it is:** a set of **vertices (nodes)** connected by **edges**. Unlike trees, graphs can have cycles and any node can connect to any other.

**How it works:** there are two main types:
- **Directed:** edges have direction (A → B is different from B → A)
- **Undirected:** edges are bidirectional (A ↔ B)

And two ways to represent in code:
- **Adjacency list:** dictionary where each node points to its neighbors. Memory-efficient.
- **Adjacency matrix:** N×N matrix where `[i][j] = 1` if there's an edge. Fast for checking direct connections.

**Complexity (depends on the algorithm applied):** typical traversals are **O(V + E)** where V = vertices and E = edges.

**Real-world applications:** social networks, maps and GPS (Waze), product recommendation, fraud analysis, Spark execution graphs (DAG).

**Example:** social network — people are vertices, friendships are edges. "People you may know" is a graph algorithm that looks at friends of friends.

---

## Algorithms

### Big O Notation

**What it is:** mathematical notation that describes **how the time (or memory) of an algorithm grows as the input size N increases**. It's the standard way to compare algorithms.

**How it works:** considers the **worst case** and discards constants and smaller terms. An algorithm that performs `3N + 5` operations is classified as **O(N)**, because the growth is linear.

**Main classes (from fastest to slowest):**

| Notation | Name | Example |
|----------|------|---------|
| O(1) | Constant | Accessing `array[i]` |
| O(log N) | Logarithmic | Binary search |
| O(N) | Linear | Iterating through a list |
| O(N log N) | Linearithmic | Merge sort, quick sort |
| O(N²) | Quadratic | Bubble sort, two nested loops |
| O(2ⁿ) | Exponential | Some recursive solutions (naive Fibonacci) |

**Example:** iterating through a 1,000-element list with a loop is **O(N)** — 1,000 operations. If it's `O(N²)`, that's 1,000,000 operations. That's why notation matters: for large N, the difference is enormous.

---

### Linear Search

**What it is:** the simplest search algorithm. Goes through the structure **from start to end**, comparing each element with the searched value.

**How it works:** starts at the first element, tests one by one. Returns the position when found. If it reaches the end without finding, returns that it doesn't exist.

**Complexity:** **O(N)** in the worst case.

**When to use:** when the list is **not sorted**, or is too small to justify more sophisticated algorithms.

**Example:** searching for `25` in `[10, 7, 25, 3, 18]`:
```
position 0: 10 ≠ 25
position 1:  7 ≠ 25
position 2: 25 = 25 ✓ found!
```

---

### Binary Search

**What it is:** a search algorithm **much more efficient** than linear, but requires the list to be **sorted**. Divides the search interval in half at each step.

**How it works:** looks at the middle element. If it's the one searched, done. If the searched is smaller, discards the right half and repeats on the left half. If larger, discards the left. Continues dividing until found or exhausted.

**Complexity:** **O(log N)** — in a list of 1 million elements, at most 20 comparisons.

**When to use:** when the list is sorted and you'll perform many searches.

**Example:** searching for `7` in `[1, 3, 5, 7, 9, 11, 13]`:
```
middle = 7  → found in 1 comparison
```
Searching for `11`:
```
middle = 7   → 11 > 7, discard left
middle = 11  → found
```

---

### Bubble Sort

**What it is:** a simple (and slow) sorting algorithm. Compares **adjacent** pairs and swaps if out of order. Repeats until the list is sorted.

**How it works:** in each pass through the list, the largest element "bubbles up" to the end. Hence the name. Repeats N times.

**Complexity:** **O(N²)** — terrible for large lists.

**When to use:** practically never in production. Used in teaching because it's easy to understand.

**Example:** sorting `[3, 1, 4, 2]`:
```
Pass 1: [1, 3, 2, 4]
Pass 2: [1, 2, 3, 4]  ✓
```

---

### Selection Sort

**What it is:** a sorting algorithm that finds the **smallest element in the list** and places it in the first position, then the second smallest in the second position, and so on.

**How it works:** scans the entire list to find the smallest, swaps with position 0. Then scans the rest, finds the second smallest, swaps with position 1. Repeats N times.

**Complexity:** **O(N²)**.

**When to use:** also rarely in production. Educational.

**Example:** sorting `[3, 1, 4, 2]`:
```
Find smallest = 1 → swap with position 0 → [1, 3, 4, 2]
Find smallest (from index 1) = 2 → swap → [1, 2, 4, 3]
Find smallest (from index 2) = 3 → swap → [1, 2, 3, 4]
```

---

### Insertion Sort

**What it is:** an algorithm that builds the sorted list **one element at a time**, inserting each new element in the correct position among those already sorted.

**How it works:** considers the first element as already sorted. Takes the second and inserts it in the right position relative to the first. Takes the third and inserts it in the right position between the first two. And so on.

**Complexity:** **O(N²)** in the worst case, but **very efficient for nearly sorted lists** (close to O(N)).

**When to use:** small or nearly sorted lists. It's used internally by hybrid algorithms like Timsort (Python's sort).

**Example:** sorting `[3, 1, 4, 2]` like organizing cards in your hand:
```
[3]                ← start with 3
[1, 3]             ← insert 1 before 3
[1, 3, 4]          ← 4 is already in position
[1, 2, 3, 4]       ← insert 2 between 1 and 3
```

---

### Merge Sort

**What it is:** an **efficient and stable** sorting algorithm, based on the **"divide and conquer"** strategy.

**How it works:** divides the list in half recursively until having 1-element lists (which are already "sorted"). Then **merges pairs of sorted lists**, always comparing the first elements of each, until reconstructing the entire sorted list.

**Complexity:** **O(N log N)** guaranteed, even in the worst case. Uses O(N) extra memory.

**When to use:** when you need performance guarantees. It's the basis of many sorts in production languages.

**Example:** sorting `[3, 1, 4, 2]`:
```
Divide: [3, 1]   [4, 2]
Divide: [3] [1]  [4] [2]
Merge:  [1, 3]   [2, 4]
Merge:  [1, 2, 3, 4]
```

---

### Quick Sort

**What it is:** a sorting algorithm **fast in practice**, also based on "divide and conquer". It's the most used sort in language libraries.

**How it works:** chooses an element as a **pivot**. Reorganizes the list so that values smaller than the pivot go to the left and larger ones go to the right. Then recursively applies the same process on each side.

**Complexity:**
- Average case: **O(N log N)**
- Worst case (badly chosen pivot): **O(N²)**
- Memory: O(log N)

**When to use:** general-purpose sort. Tends to be faster than merge sort in practice, despite the theoretical worst case.

**Example:** sorting `[3, 1, 4, 2]` with pivot = 3:
```
[1, 2] [3] [4]      ← partition around 3
[1, 2]              ← pivot = 1 → [] [1] [2]
[2]                 ← already sorted
Result: [1, 2, 3, 4]
```

---

### Recursion

**What it is:** a technique where a function **calls itself** with smaller input, until reaching a **base case** that is solved directly.

**How it works:** every recursive function has two parts:
1. **Base case:** condition that stops the recursion (without it, the function runs forever and overflows the stack)
2. **Recursive case:** call of the function itself with a smaller problem

With each call, a new "frame" is pushed onto the **call stack**. When the function returns, the frame is popped off the stack.

**Complexity:** depends on the algorithm. Badly written recursions can be exponential; well-written ones (with memoization) can be O(N).

**When to use:** problems naturally divided into similar sub-problems (trees, graphs, divide-and-conquer sorts).

**Example:** factorial of N (`N! = N × (N-1)!`):
```python
def factorial(n):
    if n == 0:        # base case
        return 1
    return n * factorial(n - 1)   # recursive case

factorial(4)
# = 4 × factorial(3)
# = 4 × 3 × factorial(2)
# = 4 × 3 × 2 × factorial(1)
# = 4 × 3 × 2 × 1 × factorial(0)
# = 4 × 3 × 2 × 1 × 1 = 24
```

---

### BFS — Breadth-First Search

**What it is:** a graph (or tree) traversal algorithm that explores nodes **level by level**, starting from the initial node.

**How it works:** uses a **queue**. Starts by placing the initial node in the queue. In a loop, removes the first node from the queue, marks it as visited, and adds all its unvisited neighbors to the end of the queue. Continues until the queue is empty.

**Complexity:** **O(V + E)** — V vertices, E edges.

**When to use:**
- Find the **shortest path** in unweighted graphs
- Explore all nodes at a distance K from the start
- Social network analysis (degrees of separation)

**Example:** in a social network, finding all friends of friends of Cleber:
```
Level 0: Cleber
Level 1: direct friends (John, Mary, Peter)
Level 2: friends of friends (all friends of John, Mary, Peter)
```

---

### DFS — Depth-First Search

**What it is:** a graph traversal algorithm that **goes as deep as possible** on each path before backtracking.

**How it works:** uses a **stack** or recursion. Starts at the initial node, goes to an unvisited neighbor, then to a neighbor of that neighbor, and so on. When it reaches a dead end, it backtracks and tries another path.

**Complexity:** **O(V + E)**.

**When to use:**
- Detect **cycles** in graphs
- **Topological sort** (ordering dependencies — used in Spark's DAG)
- Solve mazes
- Find connected components

**Example:** exploring a maze always going forward until hitting a dead end, going back to the last fork, trying another path. That's exactly what DFS does in a graph.

---

## References

- Cormen, T. H.; Leiserson, C. E.; Rivest, R. L.; Stein, C. **Introduction to Algorithms**. 4th edition. MIT Press, 2022.
- Sedgewick, R.; Wayne, K. **Algorithms**. 4th edition. Addison-Wesley, 2011.
- Skiena, S. **The Algorithm Design Manual**. 3rd edition. Springer, 2020.
- Kleinberg, J.; Tardos, É. **Algorithm Design**. Pearson, 2005.
- Knuth, D. E. **The Art of Computer Programming, Volumes 1-4**. Addison-Wesley.

---

*Repository: **computer-science-fundamentals** — solid fundamentals for building robust systems.*
