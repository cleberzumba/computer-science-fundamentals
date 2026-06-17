# Trees

> Part of the **computer-science-fundamentals** repository — a series of studies on Computer Science fundamentals applied to the real world.

---

## What it is

A **hierarchical** structure with a root node at the top and child nodes below, forming a tree. Each node can have zero or more children, but only one parent.

---

## How it works

The most common structure is the **Binary Search Tree (BST)**: each node has at most two children. Values smaller than the parent go to the left, larger ones go to the right. This allows search by successive division.

**Important terms:**
- **Root:** the top node
- **Leaf:** node with no children
- **Height:** longest distance from root to a leaf
- **Depth:** distance from a node to the root

**Important variations:**
- **Balanced BST** (AVL, Red-Black): automatically maintains minimum height
- **B-Tree / B+Tree:** used in databases
- **Trie:** used for string search

---

## Complexity (in balanced BST)

- Search: **O(log N)**
- Insertion: **O(log N)**
- Removal: **O(log N)**

**Worst case (degenerate tree, became a list):** O(N)

---

## Example

BST with values `[8, 3, 10, 1, 6, 14]`:

```
        8
       / \
      3   10
     / \    \
    1   6    14
```

Searching for `6`:
- Start at `8` → `6 < 8`, go left
- `3` → `6 > 3`, go right
- Find `6`

---

## Real-world applications

- **Database indexes** (B-Trees in PostgreSQL, MySQL, Delta Lake)
- **File systems** (HDFS, NTFS, ext4)
- **HTML DOM** — every web page is a tree
- **Spark's Catalyst Optimizer** — execution plans are expression trees
- **JSON / XML** — hierarchical structures naturally represented as trees

---

## References

- Cormen, T. H.; Leiserson, C. E.; Rivest, R. L.; Stein, C. **Introduction to Algorithms**. 4th edition. MIT Press, 2022.
- Sedgewick, R.; Wayne, K. **Algorithms**. 4th edition. Addison-Wesley, 2011.
- Knuth, D. E. **The Art of Computer Programming, Volume 3: Sorting and Searching**. 2nd edition. Addison-Wesley, 1998.

---

*Repository: **computer-science-fundamentals** — solid fundamentals for building robust systems.*
