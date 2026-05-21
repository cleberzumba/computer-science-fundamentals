# Compiled vs Interpreted Languages

## Compiled

The source code is translated **before execution** into machine code (binary) by a program called a **compiler**. The result is an executable that runs directly on the operating system.

**Flow:** Source code → Compiler → Executable → Execution

**Examples:** C, C++, Rust, Go

**Characteristics:**
- **Fast** execution (code is already in native format)
- Syntax errors are detected at compile time
- Executable is **platform-specific** (Windows, Linux, Mac)
- Distributed as a binary, without exposing the source code

## Interpreted

The source code is executed **line by line at runtime** by a program called an **interpreter**. There is no prior step to generate an executable.

**Flow:** Source code → Interpreter → Execution

**Examples:** Python, JavaScript, Ruby, PHP

**Characteristics:**
- **Slower** execution (translation happens on every run)
- Errors appear at runtime
- **Portable**: the same code runs on any system with the interpreter installed
- Faster development cycle (no compilation step)

## Hybrid (intermediate case)

Some languages combine both approaches: the code is compiled into an **intermediate bytecode**, which is then executed by a virtual machine.

**Examples:** Java (JVM), C# (.NET CLR), Kotlin, Scala

**Flow:** Source code → Compiler → Bytecode → Virtual Machine → Execution

## Quick Comparison

| Aspect            | Compiled          | Interpreted |
|-------------------|-------------------|-------------|
| Execution speed   | Fast              | Slower      |
| Portability       | Platform-specific | High        |
| Error detection   | At compile time   | At runtime  |
| Distribution      | Binary            | Source code |
| Development cycle | Slower            | Faster      |

## References

- [Compiled vs Interpreted Languages – GeeksforGeeks](https://www.geeksforgeeks.org/difference-between-compiled-and-interpreted-language/)
- [Compiler vs Interpreter – freeCodeCamp](https://www.freecodecamp.org/news/compiled-versus-interpreted-languages/)
- [Programming Language Implementation – Wikipedia](https://en.wikipedia.org/wiki/Programming_language_implementation)
- *Compilers: Principles, Techniques, and Tools* (Aho, Sethi, Ullman) — classic reference on compilers
- [Python execution model – Python Docs](https://docs.python.org/3/reference/executionmodel.html)
