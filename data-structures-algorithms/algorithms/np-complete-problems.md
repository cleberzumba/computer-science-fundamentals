# NP-Complete Problems

> Part of the **computer-science-fundamentals** repository — a series of studies on Computer Science fundamentals applied to the real world.

---

## What they are

**NP-complete problems** are the hardest class of problems within NP — problems whose solutions can be **verified quickly**, but for which **no fast algorithm is known to solve them**.

All are **equivalent in difficulty** — solving one in polynomial time would solve all of them. This discovery, by Stephen Cook (1971) and Richard Karp (1972), founded modern complexity theory.

---

## The most famous NP-complete problems

### 1. Traveling Salesman Problem (TSP)

**Problem:** find the shortest route that visits all cities exactly once, returning to the starting point.

**Where it appears:** delivery routing (Amazon, FedEx), bus routes, sequencing holes in circuit boards.

---

### 2. Knapsack Problem

**Problem:** given a knapsack with limited capacity and various items with values and weights, which combination maximizes total value without exceeding capacity?

**Where it appears:** resource allocation, investment selection, feature selection in ML, task scheduling.

---

### 3. SAT (Satisfiability)

**Problem:** given a Boolean logic formula with N variables, is there any combination of values (True/False) that makes the formula true?

**Where it appears:** hardware verification, software testing, sudoku solving, symbolic AI.

**Curiosity:** it was the **first problem proven NP-complete** by Stephen Cook in 1971 (Cook-Levin Theorem).

---

### 4. Graph Coloring

**Problem:** color all vertices of a graph using at most K colors, such that adjacent vertices have different colors.

**Where it appears:** radio frequency allocation, university schedule planning, register allocation in compilers, Wi-Fi channel distribution.

---

### 5. Vertex Cover

**Problem:** find the smallest set of vertices such that every edge in the graph has at least one endpoint in the set.

**Where it appears:** security camera placement in buildings, network monitoring, anomaly detection.

---

### 6. Independent Set

**Problem:** find the largest possible set of vertices in a graph such that no pair of vertices is adjacent.

**Where it appears:** task allocation on parallel processors, site selection for installation (without interference), scheduling.

---

### 7. Hamiltonian Cycle

**Problem:** is there a path in the graph that visits every vertex exactly once and returns to the start?

**Important not to confuse with Eulerian** (which visits every edge, solvable in polynomial time).

**Where it appears:** DNA sequencing, route planning in games, circuit assembly.

---

### 8. Set Cover

**Problem:** given a universe of elements and various subsets, choose the smallest number of subsets whose union covers all elements.

**Where it appears:** placement of radio stations to cover a region, datacenter installation, class scheduling.

---

### 9. Partition Problem

**Problem:** given a set of numbers, can it be divided into two subsets with the same sum?

**Where it appears:** server load balancing, fair resource distribution, task distribution.

---

### 10. Bin Packing

**Problem:** pack N items of different sizes into the smallest possible number of fixed-size bins.

**Where it appears:** truck loading, virtual machine allocation on physical servers, ad packaging in TV time slots.

---

### 11. Generalized Sudoku

**Problem:** complete an N×N Sudoku.

**Curiosity:** the 9×9 Sudoku from the newspaper is easy. But generalized versions (16×16, 25×25) are NP-complete. Classic teaching example.

---

### 12. Subgraph Isomorphism

**Problem:** given a graph G and a smaller graph H, is H contained in G?

**Where it appears:** pattern search in social networks, similarity detection in chemical molecules, pattern recognition in images.

---

## The great equivalence

All these problems are **equivalent in difficulty**. This means:

- If anyone finds a polynomial-time algorithm for **ANY OF THEM**, it automatically solves **ALL OTHERS** in polynomial time
- This would prove **P = NP**
- It would earn US$ 1 million from the Clay Mathematics Institute and revolutionize computing

**Karp proved in 1972** that 21 famous problems are NP-complete, all reducible to each other. It was the paper that defined modern NP-completeness theory.

---

## How these problems are solved in practice

Since none has an exact solution in reasonable time for large N, the following are used:

- **Greedy algorithms** (fast, approximate)
- **Dynamic programming** (for special cases)
- **Backtracking with pruning** (smart brute force)
- **Genetic algorithms**
- **Simulated annealing**
- **Modern solvers** — CPLEX, Gurobi, Google's OR-Tools
- **SAT solvers** — Microsoft's Z3, MiniSAT

**Modern engineering accepts approximations.** A solution 5% worse than optimal in 10 seconds is worth more than an optimal solution in 1000 years.

---

## Applications in Data Engineering, ML, and AI

**Data Engineering:**
- SQL query optimization (approximate plans)
- Data partitioning in Spark (approximate balancing)
- Cluster resource allocation (Bin Packing variants)

**Machine Learning:**
- Feature Selection is NP-hard → use forward/backward selection (greedy)
- Neural Architecture Search is NP-hard → approximate search
- Hyperparameter optimization → Bayesian Optimization instead of brute force

**Modern AI:**
- Token routing in Mixture of Experts models
- Attention structure optimization in Transformers
- Training scheduling in distributed clusters

---

## Pocket summary

**NP-complete problems are:**
- The hardest class in NP
- All equivalent in difficulty
- Without any known fast algorithm
- Solved in practice with approximations
- Present in almost all real-world optimization problems

**If you solve one in polynomial time:** you win US$ 1 million, revolutionize computing, and answer the greatest open question in computer science (P vs NP).

---

## References

- Karp, R. M. **Reducibility Among Combinatorial Problems**. Complexity of Computer Computations, 1972.
- Cook, S. A. **The Complexity of Theorem-Proving Procedures**. ACM STOC, 1971.
- Garey, M. R.; Johnson, D. S. **Computers and Intractability: A Guide to the Theory of NP-Completeness**. W. H. Freeman, 1979.
- Sipser, M. **Introduction to the Theory of Computation**. 3rd edition. Cengage Learning, 2013.
- Arora, S.; Barak, B. **Computational Complexity: A Modern Approach**. Cambridge University Press, 2009.
- Cormen, T. H.; Leiserson, C. E.; Rivest, R. L.; Stein, C. **Introduction to Algorithms**. 4th edition. MIT Press, 2022.
