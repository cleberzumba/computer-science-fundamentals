# Decimal to Binary Conversion

> Part of the [computer-science-fundamentals](https://github.com/) repository — a series of studies on Computer Science fundamentals applied to the real world.

---

## Table of Contents

- [Introduction](#introduction)
- [Why convert decimal to binary?](#why-convert-decimal-to-binary)
- [Core idea](#core-idea)
- [Method 1: Successive Division by 2](#method-1-successive-division-by-2)
- [More solved examples](#more-solved-examples)
- [Method 2: Subtraction by powers of 2](#method-2-subtraction-by-powers-of-2)
- [Mental shortcut: powers of 2 table](#mental-shortcut-powers-of-2-table)
- [Python implementation](#python-implementation)
- [Conclusion](#conclusion)
- [References](#references)

---

## Introduction

Every number we type on a keyboard, every value stored in a database, every count in a Spark DataFrame is eventually translated into binary — sequences of `0`s and `1`s — so the computer's hardware can process it.

Knowing how to convert from decimal to binary is a fundamental skill in Computer Science. It reveals how integers are stored in memory, how data types are sized, and how low-level operations actually work.

---

## Why convert decimal to binary?

Humans count in decimal (base 10), using ten symbols: `0` to `9`. Computers operate in binary (base 2), using only `0` and `1`, because each digit maps directly to two electrical states: off and on.

To bridge the human and the machine, we need a systematic process to translate decimal numbers into binary.

---

## Core idea

Any decimal number can be written as a sum of powers of 2. Converting to binary is essentially finding which powers of 2 add up to that number — and marking those positions with `1`, leaving the rest as `0`.

For example, 13 can be written as:

```
13 = 8 + 4 + 1
   = 2³ + 2² + 2⁰
```

Which gives the binary `1101`:

```
 2³  2²  2¹  2⁰
  1   1   0   1
  8 + 4 + 0 + 1 = 13
```

There are two standard methods to perform this conversion: **successive division by 2** (the most reliable and widely taught), and **subtraction by powers of 2** (faster for mental math with small numbers).

---

## Method 1: Successive Division by 2

This is the standard algorithm. The idea is to repeatedly divide the number by 2 and collect the remainders. Reading the remainders from bottom to top gives the binary representation.

### Steps

1. Divide the decimal number by 2
2. Write down the remainder (it will be 0 or 1)
3. Take the quotient and divide it by 2 again
4. Repeat until the quotient reaches 0
5. Read the remainders from **bottom to top** — that's the binary number

### Step-by-step example

Let's convert `13` to binary.

```
13 ÷ 2 = 6  remainder 1  ↑
 6 ÷ 2 = 3  remainder 0  │  read from
 3 ÷ 2 = 1  remainder 1  │  bottom to top
 1 ÷ 2 = 0  remainder 1  │
```

**Result: 1101₂**

Verification:
```
1101₂ = 1×2³ + 1×2² + 0×2¹ + 1×2⁰
      = 8 + 4 + 0 + 1
      = 13₁₀ ✓
```

> **Important:** always read the remainders from bottom to top, never top to bottom. Reading in the wrong direction gives a completely different number.

---

## More solved examples

### Example 1: convert `25` to binary

```
25 ÷ 2 = 12  remainder 1  ↑
12 ÷ 2 =  6  remainder 0  │
 6 ÷ 2 =  3  remainder 0  │  read from
 3 ÷ 2 =  1  remainder 1  │  bottom to top
 1 ÷ 2 =  0  remainder 1  │
```

**Result: 11001₂**

Verification: 1×16 + 1×8 + 0×4 + 0×2 + 1×1 = 16 + 8 + 1 = 25 ✓

---

### Example 2: convert `42` to binary

```
42 ÷ 2 = 21  remainder 0  ↑
21 ÷ 2 = 10  remainder 1  │
10 ÷ 2 =  5  remainder 0  │
 5 ÷ 2 =  2  remainder 1  │  read from
 2 ÷ 2 =  1  remainder 0  │  bottom to top
 1 ÷ 2 =  0  remainder 1  │
```

**Result: 101010₂**

Verification: 32 + 0 + 8 + 0 + 2 + 0 = 42 ✓

---

### Example 3: convert `100` to binary

```
100 ÷ 2 = 50  remainder 0  ↑
 50 ÷ 2 = 25  remainder 0  │
 25 ÷ 2 = 12  remainder 1  │
 12 ÷ 2 =  6  remainder 0  │  read from
  6 ÷ 2 =  3  remainder 0  │  bottom to top
  3 ÷ 2 =  1  remainder 1  │
  1 ÷ 2 =  0  remainder 1  │
```

**Result: 1100100₂**

Verification: 64 + 32 + 0 + 0 + 4 + 0 + 0 = 100 ✓

---

### Example 4: convert `255` to binary (a full byte)

```
255 ÷ 2 = 127  remainder 1  ↑
127 ÷ 2 =  63  remainder 1  │
 63 ÷ 2 =  31  remainder 1  │
 31 ÷ 2 =  15  remainder 1  │  read from
 15 ÷ 2 =   7  remainder 1  │  bottom to top
  7 ÷ 2 =   3  remainder 1  │
  3 ÷ 2 =   1  remainder 1  │
  1 ÷ 2 =   0  remainder 1  │
```

**Result: 11111111₂**

> This is the maximum value that fits in 1 byte (8 bits) when unsigned.

---

## Method 2: Subtraction by powers of 2

For small numbers, this method is often faster mentally. The idea is to find the largest power of 2 that fits into the number, subtract it, and repeat until the number reaches zero.

### Steps

1. Find the largest power of 2 that is ≤ the number
2. Place a `1` at that position
3. Subtract that power from the number
4. Repeat with the remaining value
5. Fill any skipped positions with `0`

### Example: convert `13` to binary

```
Largest power of 2 ≤ 13  →  2³ = 8
13 - 8 = 5  →  bit at position 3 = 1

Largest power of 2 ≤ 5   →  2² = 4
 5 - 4 = 1  →  bit at position 2 = 1

Largest power of 2 ≤ 1   →  2⁰ = 1
              (skip position 1  →  bit = 0)
 1 - 1 = 0  →  bit at position 0 = 1

Positions:  3  2  1  0
Bits:       1  1  0  1
```

**Result: 1101₂**

### Example: convert `42` to binary

```
42 - 32 (2⁵) = 10  →  bit at position 5 = 1
10 -  8 (2³) =  2  →  bit at position 3 = 1
 2 -  2 (2¹) =  0  →  bit at position 1 = 1

Positions:  5  4  3  2  1  0
Bits:       1  0  1  0  1  0
```

**Result: 101010₂**

---

## Mental shortcut: powers of 2 table

Memorizing the first powers of 2 makes mental conversion much faster:

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

---

## Python implementation

Python has built-in functions for this conversion, but it's worth implementing manually to understand the algorithm.

### Built-in functions

```python
# The bin() function returns a string with the '0b' prefix
bin(13)   # '0b1101'
bin(42)   # '0b101010'
bin(255)  # '0b11111111'

# To get the binary string without the prefix:
bin(13)[2:]  # '1101'

# Using format() or f-strings (more flexible):
format(13, "b")   # '1101'
f"{13:b}"         # '1101'
f"{13:08b}"       # '00001101' — 8-digit zero-padding
```

### Manual implementation (successive division)

```python
def decimal_to_binary(n: int) -> str:
    """
    Converts a non-negative integer to binary
    using successive division by 2.
    Example: 13 → '1101'
    """
    if n == 0:
        return "0"

    bits = []
    while n > 0:
        bits.append(str(n % 2))  # remainder of division by 2
        n = n // 2               # integer quotient

    # Remainders were collected bottom-up; reverse them
    return "".join(reversed(bits))

# Tests
print(decimal_to_binary(13))   # '1101'
print(decimal_to_binary(25))   # '11001'
print(decimal_to_binary(42))   # '101010'
print(decimal_to_binary(100))  # '1100100'
print(decimal_to_binary(255))  # '11111111'
```

### Manual implementation (subtraction by powers of 2)

```python
def decimal_to_binary_powers(n: int) -> str:
    """
    Converts to binary using subtraction by powers of 2.
    """
    if n == 0:
        return "0"

    # Find the largest power of 2 ≤ n
    largest_power = 0
    while 2 ** (largest_power + 1) <= n:
        largest_power += 1

    # Build the binary from MSB to LSB
    bits = []
    for power in range(largest_power, -1, -1):
        value = 2 ** power
        if value <= n:
            bits.append("1")
            n -= value
        else:
            bits.append("0")

    return "".join(bits)

print(decimal_to_binary_powers(13))  # '1101'
print(decimal_to_binary_powers(42))  # '101010'
```

---

## Conclusion

Converting decimal to binary is the inverse of the binary-to-decimal conversion. While binary-to-decimal multiplies bits by powers of 2 and sums them, decimal-to-binary breaks the number down into powers of 2.

The two main methods:

1. **Successive division by 2** — most reliable, works for any number, read remainders bottom to top
2. **Subtraction by powers of 2** — faster for mental math with small numbers

**Pocket summary:**

- Divide by 2, collect the remainders, read bottom to top
- Or subtract powers of 2 starting from the largest that fits
- In Python: `bin(n)` or `f"{n:b}"` solve it directly
- Mastering powers of 2 (1, 2, 4, 8, 16, 32, 64, 128, 256…) makes conversion almost automatic

---

## References

- Patterson, D. A.; Hennessy, J. L. *Computer Organization and Design: The Hardware/Software Interface*. 5th edition. Morgan Kaufmann, 2013.
- Tanenbaum, A. S.; Austin, T. *Structured Computer Organization*. 6th edition. Pearson, 2012.
- Mano, M. M.; Ciletti, M. D. *Digital Design*. 5th edition. Pearson, 2012.
- Stallings, W. *Computer Organization and Architecture: Designing for Performance*. 10th edition. Pearson, 2016.
- Knuth, D. E. *The Art of Computer Programming, Volume 2: Seminumerical Algorithms*. 3rd edition. Addison-Wesley, 1997.
