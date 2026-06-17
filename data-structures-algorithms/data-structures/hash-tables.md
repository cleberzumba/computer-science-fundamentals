# Hash Tables

> Part of the **computer-science-fundamentals** repository — a series of studies on Computer Science fundamentals applied to the real world.

---

## What it is

A **key-value** structure that maps a unique key to an associated value. Allows search, insertion, and removal in average **O(1)** time.

---

## How it works

When you insert a key, a **hash function** transforms the key into a number indicating the position (bucket) where the value will be stored. To search, the same hash function is applied and you go directly to the position.

**Collision handling** (when two keys generate the same position):
- **Chaining:** each bucket becomes a linked list of pairs
- **Open addressing:** searches for the next free position in the table

---

## Complexity

- Insertion: **O(1) on average**, O(N) worst case
- Search: **O(1) on average**, O(N) worst case
- Removal: **O(1) on average**, O(N) worst case

Worst case only happens when there are many collisions — rare with a good hash function.

---

## Example

```python
person = {"name": "Cleber", "age": 48, "country": "Brazil"}

person["name"]                # returns "Cleber" instantly
person["profession"] = "Eng"  # inserts new key in O(1)
del person["age"]             # removes in O(1)
```

---

## Real-world applications

- **Dictionaries in Python** (`dict`) and in almost every modern language
- **Database indexes** (some types)
- **Caches** (Redis, Memcached)
- **Broadcast Hash Join in Spark** — the small table becomes a hash table in executors' memory
- **Duplicate detection** in datasets

---

## References

- Cormen, T. H.; Leiserson, C. E.; Rivest, R. L.; Stein, C. **Introduction to Algorithms**. 4th edition. MIT Press, 2022.
- Sedgewick, R.; Wayne, K. **Algorithms**. 4th edition. Addison-Wesley, 2011.
- Knuth, D. E. **The Art of Computer Programming, Volume 3: Sorting and Searching**. 2nd edition. Addison-Wesley, 1998.

---

*Repository: **computer-science-fundamentals** — solid fundamentals for building robust systems.*
