# Processes vs Threads

> Understanding the fundamental units of execution in modern operating systems — and why the distinction matters for every piece of software you write.

---

## The Big Picture

Every program you run becomes either a **process**, a **thread**, or a combination of both. Understanding the difference is the foundation for everything from web servers to distributed systems like Apache Spark.

```
Operating System
    │
    ├── Process A (Chrome)
    │     ├── Thread 1 (UI)
    │     ├── Thread 2 (network)
    │     └── Thread 3 (JS engine)
    │
    └── Process B (Spotify)
          ├── Thread 1 (audio)
          └── Thread 2 (UI)
```

---

## What is a Process?

A **process** is an independent program in execution. Each process has:

- Its **own memory space** (heap, stack, code, data)
- Its **own resources** (file handles, network connections)
- **Isolation** from other processes
- One or more threads running inside

```
┌──────────────────────────────────────┐
│  PROCESS                             │
├──────────────────────────────────────┤
│  PID, memory space, file descriptors │
│  Code, data, heap, stack             │
│  Threads (1+)                        │
└──────────────────────────────────────┘
```

---

## What is a Thread?

A **thread** is the smallest unit of execution **within** a process.

- **Lives inside a process** — cannot exist alone
- **Shares memory** with sibling threads
- Has its **own stack** and **registers**
- Much **lighter** than a process

```
┌──────────────────────────────────────┐
│  THREAD                              │
├──────────────────────────────────────┤
│  Own: stack, registers, TID          │
│  Shared: heap, code, globals, files  │
└──────────────────────────────────────┘
```

---

## The Core Differences

| Aspect | Process | Thread |
|---|---|---|
| **Memory** | Own private space | Shared with other threads |
| **Isolation** | Fully isolated | Not isolated |
| **Creation cost** | Heavy | Light |
| **Context switch** | Expensive | Cheap |
| **Communication** | IPC required | Direct via memory |
| **Failure impact** | Doesn't affect others | Can crash entire process |
| **Synchronization** | Less needed | Heavily needed (locks) |

---

## Visual Comparison

### Two processes (each with one thread)

```
┌─────────────────┐     ┌─────────────────┐
│   Process A     │     │   Process B     │
│  ┌───────────┐  │     │  ┌───────────┐  │
│  │ Memory    │  │     │  │ Memory    │  │
│  │ (private) │  │     │  │ (private) │  │
│  └───────────┘  │     │  └───────────┘  │
│  ┌───────────┐  │     │  ┌───────────┐  │
│  │ Thread 1  │  │     │  │ Thread 1  │  │
│  └───────────┘  │     │  └───────────┘  │
└─────────────────┘     └─────────────────┘
        ↕                       ↕
        └─── needs IPC to ──────┘
```

### One process with multiple threads

```
┌──────────────────────────────────────┐
│   Process A                          │
│  ┌────────────────────────────────┐  │
│  │  Shared Memory (heap, globals) │  │
│  └────────────────────────────────┘  │
│  ┌────────┐  ┌────────┐  ┌────────┐  │
│  │Thread 1│  │Thread 2│  │Thread 3│  │
│  └────────┘  └────────┘  └────────┘  │
│       └──── direct access ────┘      │
└──────────────────────────────────────┘
```

---

## Practical Examples

### Web Browser (Chrome)

Uses **both**:
- Each tab = separate process (isolation)
- Within each tab = multiple threads (UI, network, JS, rendering)

### Web Servers

- **Nginx**: multi-process (master + workers)
- **Tomcat**: multi-threaded (thread pool per request)

### Apache Spark

```
Cluster
  ├── Driver process (1)
  └── Executor processes (N)
        └── Each runs multiple threads
              └── Each thread = 1 Task
```

That's why `spark.executor.cores` controls **thread count** per executor.

---

## When to Use Each

### Use processes when:

- You need **strong isolation** (security, fault tolerance)
- Work is **CPU-bound** in Python (bypass GIL)
- Components communicate **rarely**
- Failure in one **must not** affect others

### Use threads when:

- You need **shared state** between tasks
- Work is **I/O-bound** (network, disk)
- You need **fast communication**
- **Memory efficiency** matters

---

## Common Pitfalls

### Race Conditions (Threads)

```python
counter = 0

def increment():
    global counter
    for _ in range(1000):
        counter += 1   # NOT atomic — race condition!
```

**Solution:** locks, mutexes, atomic operations.

### Deadlocks (Threads)

```
Thread A: holds lock 1, wants lock 2
Thread B: holds lock 2, wants lock 1
→ both wait forever 
```

**Solution:** acquire locks in the same order, use timeouts.

### High Memory (Processes)

- 100 processes × 100MB each = 10 GB
- 100 threads in 1 process × 1MB stack = 100 MB

---

## The Python GIL

Python's **Global Interpreter Lock (GIL)** prevents multiple threads from executing Python bytecode simultaneously.

**Implications:**
- Threads in Python don't help **CPU-bound** work
- Use `multiprocessing` for true parallelism
- This is why PySpark workers are **processes**, not threads

```python
# CPU-bound — threading WON'T speed up
import threading

# CPU-bound — multiprocessing WILL speed up
import multiprocessing

with multiprocessing.Pool(4) as pool:
    pool.map(heavy_computation, range(4))   # true parallelism 
```

---

## Key Takeaways

1. **Processes are isolated, threads share memory.** Single most important distinction.

2. **Threads are cheaper, but riskier.** Faster, less memory, but one bug can crash everything.

3. **Processes are heavier, but safer.** More overhead, but fault-tolerant.

4. **Communication style differs.** Threads share memory; processes pass messages.

5. **Modern systems use both.** Browsers, Spark, OS services combine processes (isolation) with threads (concurrency).

6. **Choice depends on workload.** I/O-bound = threads. CPU-bound in Python = processes. Need isolation = processes. Shared state = threads.

---

## Related Concepts

- **Concurrency vs Parallelism** — *dealing with* vs *doing* many things at once
- **Context switching** — OS swapping between processes/threads
- **Synchronization primitives** — mutexes, semaphores, condition variables
- **IPC** — pipes, sockets, shared memory, message queues
- **Thread pools** — pre-created threads waiting for work

---
