# Computational Complexity

> Part of the **computer-science-fundamentals** repository — a series of studies on Computer Science fundamentals applied to the real world.

---

## What it is

**Computational Complexity** is the study of **how many resources** (time and memory) an algorithm needs to solve a problem **as the input size grows**.

It's the scientific answer to the question: **"Does this algorithm scale well?"**

---

## The two main types

**1. Time Complexity**
- How many operations the algorithm executes
- Measured in Big O: O(1), O(log N), O(N), O(N log N), O(N²), etc.
- The most discussed in day-to-day work

**2. Space Complexity**
- How much extra memory the algorithm uses
- Also measured in Big O
- Important when working with large datasets

---

## Why it exists

Without complexity analysis, it would be impossible to know which algorithm to choose for each problem.

Practical examples:

- Binary search on 1 billion elements: **30 operations**
- Linear search on 1 billion elements: **1 billion operations**
- TSP with 60 cities: **more than atoms in the universe**

The difference between an O(N) and an O(log N) algorithm can be the difference between **a system that works** and **a system that crashes**.

---

## Complexity classes

Computational complexity also **classifies problems** (not just algorithms) into categories:

| Class | Meaning | Example |
|-------|---------|---------|
| **P** | Solvable in polynomial time | Binary search, sort, shortest path |
| **NP** | Verifiable in polynomial time | TSP, SAT, Sudoku |
| **NP-complete** | The "hardest" in NP | TSP, Knapsack, 3-SAT |
| **NP-hard** | At least as hard as NP-complete | Route optimization, chip layout |
| **PSPACE** | Solvable with polynomial space | Generalized chess |
| **EXPTIME** | Require exponential time | Some game theory problems |
| **Undecidable** | Impossible to solve by algorithm | Halting Problem (Turing) |

---

## The central question of the field: P vs NP

**If a problem can be verified quickly, can it be solved quickly?**

- **P** = problems solvable in polynomial time
- **NP** = problems whose solution can be verified in polynomial time

**If P = NP:** every problem we can verify quickly would have a fast solution. It would revolutionize computing, cryptography, AI.

**If P ≠ NP:** there are problems that fundamentally have no fast solution, no matter how much hardware you have.

**Nobody knows the answer since 1971.** It's worth **US$ 1 million** as a prize from the Clay Mathematics Institute. It's one of the seven Millennium Problems and the most famous open question in computer science.

---

## Why this matters in practice

**Data Engineering:**
- Choosing algorithms that scale to billions of rows
- Understanding why certain SQL queries are slow
- Optimizing Spark pipelines knowing what's expensive

**Machine Learning / AI:**
- Many ML problems are **NP-hard** (feature selection, network architecture)
- That's why ML uses **approximations** (gradient descent, random forests) instead of optimal solutions
- Training LLMs involves complex time × memory trade-offs

**International interviews:**
- Top companies test complexity analysis in almost every technical interview
- Knowing how to classify problems separates a good candidate from an exceptional one

---

## Tools of the field

**Algorithm analysis:**
- Big O, Big Omega (Ω), Big Theta (Θ)
- Recurrences (for recursive algorithms)
- Amortized analysis

**Complexity proofs:**
- Problem reduction (showing A is as hard as B)
- Counting arguments
- Game theory

**Theory:**
- Turing Machines
- Automata
- Lambda calculus

---

## Difference between computational complexity and algorithm analysis

Terms that sometimes confuse:

**Algorithm analysis** = studying ONE specific algorithm (binary search is O(log N))

**Computational complexity** = studying CLASSES of problems (TSP is NP-complete, independent of the algorithm used)

The first is about **solutions**. The second is about **the problems themselves**.

---

## Pocket summary

- **Computational Complexity** = study of how much time and memory algorithms need as input grows
- **Time Complexity** = how many operations
- **Space Complexity** = how much memory
- **P vs NP** = the field's central question, open since 1971
- **NP-complete / NP-hard** = fundamentally hard problems (TSP, optimization)
- **Mathematical foundation** of every algorithm choice in production

---

## References

- Sipser, M. **Introduction to the Theory of Computation**. 3rd edition. Cengage Learning, 2013.
- Arora, S.; Barak, B. **Computational Complexity: A Modern Approach**. Cambridge University Press, 2009.
- Cormen, T. H.; Leiserson, C. E.; Rivest, R. L.; Stein, C. **Introduction to Algorithms**. 4th edition. MIT Press, 2022.
- Papadimitriou, C. H. **Computational Complexity**. Addison-Wesley, 1994.
- Garey, M. R.; Johnson, D. S. **Computers and Intractability: A Guide to the Theory of NP-Completeness**. W. H. Freeman, 1979.

---

*Repository: **computer-science-fundamentals** — solid fundamentals for building robust systems.*
