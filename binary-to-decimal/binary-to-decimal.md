# Binary to Decimal Conversion

> Part of the [computer-science-fundamentals](https://github.com/) repository — a series of studies on Computer Science fundamentals applied to the real world.

---

## Table of Contents

- [Introduction](#introduction)
- [What is binary?](#what-is-binary)
- [Core concepts](#core-concepts)
- [The conversion formula](#the-conversion-formula)
- [Step-by-step example](#step-by-step-example)
- [More solved examples](#more-solved-examples)
- [Mental shortcut: powers of 2 table](#mental-shortcut-powers-of-2-table)
- [Python implementation](#python-implementation)
- [Conclusion](#conclusion)
- [References](#references)

---

## Introduction

Computers work with only two electrical states: on and off, represented as 1 and 0. All digital information — numbers, text, images, videos — is, at its core, a sequence of these two symbols.

But humans think in decimal (0 to 9). That's why knowing how to convert binary to decimal is the first step toward understanding how a computer "sees" the numbers it processes.

---

## What is binary?

The binary system (base 2) uses only two symbols: 0 and 1. Each binary digit is called a **bit** (short for *binary digit*).

Quick comparison with decimal:

| System | Base | Symbols |
|---|---|---|
| Decimal | 10 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 |
| Binary | 2 | 0, 1 |

Just as each position in decimal represents a power of 10 (units, tens, hundreds…), each position in binary represents a power of 2.

---

## Core concepts

Before converting, you need to understand two terms:

- **MSB (Most Significant Bit):** the leftmost bit. It has the highest weight.
- **LSB (Least Significant Bit):** the rightmost bit. It has the lowest weight (worth 2⁰ = 1).

```
 1  1  0  1
 ↑           ↑
MSB         LSB
```

Each position, from right to left, gets an increasing power of 2:

| Position | 3 | 2 | 1 | 0 |
|---|---|---|---|---|
| Weight | 2³ | 2² | 2¹ | 2⁰ |
| Value | 8 | 4 | 2 | 1 |

---

## The conversion formula

To convert a binary number to decimal, multiply each bit by its weight (power of 2 at its position) and sum everything:

```
Decimal = (bit_n × 2ⁿ) + ... + (bit_2 × 2²) + (bit_1 × 2¹) + (bit_0 × 2⁰)
```

Where the position starts at 0 from right to left.

---

## Step-by-step example

Let's convert the binary `1101` to decimal.

**Step 1: identify the positions**

Number the positions from right to left, starting at 0:

```
 1  1  0  1
 3  2  1  0  ← positions
```

**Step 2: write the weights (powers of 2)**

```
 1   1   0   1
 2³  2²  2¹  2⁰  ← weights
 8   4   2   1   ← value of each weight
```

**Step 3: multiply each bit by its weight**

```
 1×8  1×4  0×2  1×1
  8    4    0    1
```

**Step 4: sum everything**

```
8 + 4 + 0 + 1 = 13
```

### Result

```
1101₂ = 13₁₀
```

> **Note:** when a bit is 0, the multiplication yields 0 — meaning that position doesn't contribute to the sum. You only need to sum the weights where the bit is 1.

---

## More solved examples

### Example 1: convert `0110` to decimal

```
 0   1   1   0
 2³  2²  2¹  2⁰
 0   4   2   0

Total = 0 + 4 + 2 + 0 = 6
```

**0110₂ = 6₁₀**

---

### Example 2: convert `1010` to decimal

```
 1   0   1   0
 2³  2²  2¹  2⁰
 8   0   2   0

Total = 8 + 0 + 2 + 0 = 10
```

**1010₂ = 10₁₀**

---

### Example 3: convert `11111111` to decimal (a full byte)

```
 1    1   1   1   1  1  1  1
 2⁷  2⁶  2⁵  2⁴  2³  2²  2¹  2⁰
 128  64  32  16   8   4   2   1

Total = 128 + 64 + 32 + 16 + 8 + 4 + 2 + 1 = 255
```

**11111111₂ = 255₁₀**

> This is the maximum value that fits in 1 byte (8 bits). That's why `TINYINT` in Spark/SQL goes up to 255 when unsigned.

---

### Example 4: convert `00110011` to decimal

```
 0   0   1   1   0   0   1   1
 2⁷  2⁶  2⁵  2⁴  2³  2²  2¹  2⁰
 0   0   32  16   0   0   2   1

Total = 0 + 0 + 32 + 16 + 0 + 0 + 2 + 1 = 51
```

**00110011₂ = 51₁₀**

---

## Mental shortcut: powers of 2 table

Memorizing the first powers of 2 dramatically speeds up mental conversion:

| Position | Power | Value |
|---|---|---|
| 0 | 2⁰ | 1 |
| 1 | 2¹ | 2 |
| 2 | 2² | 4 |
| 3 | 2³ | 8 |
| 4 | 2⁴ | 16 |
| 5 | 2⁵ | 32 |
| 6 | 2⁶ | 64 |
| 7 | 2⁷ | 128 |
| 8 | 2⁸ | 256 |
| 9 | 2⁹ | 512 |
| 10 | 2¹⁰ | 1024 |

**Quick trick:** to convert a binary, write the weights above the bits, mark only where the bit is 1, and sum.

Example with `10110`:

```
Weights:  16   8   4   2   1
Bits:      1   0   1   1   0
Sum:      16 +   + 4 + 2 +   = 22
```

---

## Python implementation

Python provides built-in functions for conversion, but it's worth understanding how to do it manually.

### Using built-in functions

```python
# The int() function takes the binary string and the base (2)
int("1101", 2)      # 13
int("11111111", 2)  # 255
int("00110011", 2)  # 51
```

### Manual implementation (weighted sum)

```python
def binary_to_decimal(binary: str) -> int:
    """
    Converts a binary string to decimal using weighted sum.
    Example: '1101' → 13
    """
    decimal = 0
    # Iterate over bits from right to left
    for position, bit in enumerate(reversed(binary)):
        decimal += int(bit) * (2 ** position)
    return decimal

# Tests
print(binary_to_decimal("1101"))      # 13
print(binary_to_decimal("0110"))      # 6
print(binary_to_decimal("1010"))      # 10
print(binary_to_decimal("11111111"))  # 255
print(binary_to_decimal("00110011"))  # 51
```

### Alternative version (Horner's method)

This version is more efficient — it iterates through the bits from left to right, multiplying the partial result by 2 at each step:

```python
def binary_to_decimal_horner(binary: str) -> int:
    """
    Converts using Horner's method.
    More efficient: no need to compute powers.
    """
    decimal = 0
    for bit in binary:
        decimal = decimal * 2 + int(bit)
    return decimal

print(binary_to_decimal_horner("1101"))  # 13
```

**How Horner's method works with `1101`:**

```
Start:    decimal = 0
Read '1': decimal = 0 × 2 + 1 = 1
Read '1': decimal = 1 × 2 + 1 = 3
Read '0': decimal = 3 × 2 + 0 = 6
Read '1': decimal = 6 × 2 + 1 = 13
```

---

## Conclusion

Converting binary to decimal is a foundational skill that opens the door to understanding how computers represent numbers. The process is simple and mechanical:

1. Number the positions from right to left, starting at 0
2. Assign the weight `2^position` to each bit
3. Multiply each bit by its weight
4. Sum the results

With practice, small conversions (up to 8 bits) become almost automatic. And understanding this mechanism is what later enables you to grasp advanced topics like integer representation, floating-point arithmetic, bitwise operations, and low-level optimizations.

**Pocket summary:**

- Binary uses 2 symbols: 0 and 1
- Each position represents a power of 2 (1, 2, 4, 8, 16, …)
- To convert: multiply each bit by its weight and sum
- In Python: `int("1101", 2)` solves it directly

---

## References

- Patterson, D. A.; Hennessy, J. L. *Computer Organization and Design: The Hardware/Software Interface*. 5th edition. Morgan Kaufmann, 2013.
- Tanenbaum, A. S.; Austin, T. *Structured Computer Organization*. 6th edition. Pearson, 2012.
- Mano, M. M.; Ciletti, M. D. *Digital Design*. 5th edition. Pearson, 2012.
- Stallings, W. *Computer Organization and Architecture: Designing for Performance*. 10th edition. Pearson, 2016.
- Knuth, D. E. *The Art of Computer Programming, Volume 2: Seminumerical Algorithms*. 3rd edition. Addison-Wesley, 1997.
