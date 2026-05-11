# Decimal ↔ Hexadecimal Conversion

> Part of the [computer-science-fundamentals](https://github.com/) repository — a series of studies on Computer Science fundamentals applied to the real world.

---

## Table of Contents

- [Introduction](#introduction)
- [Review: the hexadecimal system](#review-the-hexadecimal-system)
- [Hexadecimal → Decimal](#hexadecimal--decimal)
- [Decimal → Hexadecimal](#decimal--hexadecimal)
- [Reference table](#reference-table)
- [Python implementation](#python-implementation)
- [Conclusion](#conclusion)
- [References](#references)

---

## Introduction

Conversion between decimal (base 10) and hexadecimal (base 16) shows up constantly in computing: when interpreting a memory address, decoding a web color, reading a byte dump, or inspecting the contents of a binary file. Unlike the binary-to-hex conversion (which is direct, by grouping), this one requires calculation — but the method is the same one applied to any base.

---

## Review: the hexadecimal system

The hexadecimal system uses 16 symbols: digits `0` through `9` and letters `A` through `F`:

| Hex | Decimal |
|---|---|
| 0–9 | 0–9 |
| A | 10 |
| B | 11 |
| C | 12 |
| D | 13 |
| E | 14 |
| F | 15 |

Each position in a hexadecimal number represents a power of 16:

| Position | 3 | 2 | 1 | 0 |
|---|---|---|---|---|
| Weight | 16³ | 16² | 16¹ | 16⁰ |
| Value | 4096 | 256 | 16 | 1 |

---

## Hexadecimal → Decimal

The process is analogous to binary → decimal: multiply each digit by its weight (power of 16) and sum everything.

### Formula

```
Decimal = (digit_n × 16ⁿ) + ... + (digit_2 × 16²) + (digit_1 × 16¹) + (digit_0 × 16⁰)
```

Where the position starts at 0, from right to left. Before multiplying, remember to convert letters (A–F) to their numeric values (10–15).

---

### Example 1: convert `2F` to decimal

```
Hex:      2    F
Position: 1    0
Weight:   16¹  16⁰
           16   1

Values: 2×16 + 15×1
      = 32 + 15
      = 47
```

**Result: 2F₁₆ = 47₁₀**

---

### Example 2: convert `FF` to decimal

```
Hex:      F    F
Position: 1    0
Weight:   16¹  16⁰
           16   1

Values: 15×16 + 15×1
      = 240 + 15
      = 255
```

**Result: FF₁₆ = 255₁₀**

> This is the maximum value that fits in 1 byte (8 bits).

---

### Example 3: convert `1A3` to decimal

```
Hex:      1    A    3
Position: 2    1    0
Weight:   16²  16¹  16⁰
          256   16   1

Values: 1×256 + 10×16 + 3×1
      = 256 + 160 + 3
      = 419
```

**Result: 1A3₁₆ = 419₁₀**

---

### Example 4: convert `B7A` to decimal

```
Hex:      B    7    A
Position: 2    1    0
Weight:   16²  16¹  16⁰
          256   16   1

Values: 11×256 + 7×16 + 10×1
      = 2816 + 112 + 10
      = 2938
```

**Result: B7A₁₆ = 2938₁₀**

---

### Example 5: convert `1A3F` to decimal

```
Hex:      1     A    3    F
Position: 3     2    1    0
Weight:   16³  16²  16¹  16⁰
          4096  256   16   1

Values: 1×4096 + 10×256 + 3×16 + 15×1
      = 4096 + 2560 + 48 + 15
      = 6719
```

**Result: 1A3F₁₆ = 6719₁₀**

---

## Decimal → Hexadecimal

The process is analogous to decimal → binary, but dividing by 16 (not by 2).

### Algorithm: successive division by 16

1. Divide the decimal number by 16
2. Write down the remainder (it will be a value from 0 to 15)
3. If the remainder is ≥ 10, convert to a letter (10=A, 11=B, …, 15=F)
4. Take the quotient and divide it by 16 again
5. Repeat until the quotient reaches 0
6. Read the remainders from **bottom to top**

---

### Example 1: convert `47` to hexadecimal

```
47 ÷ 16 = 2  remainder 15 (F)  ↑
 2 ÷ 16 = 0  remainder  2      │  read from bottom to top
```

**Result: 2F₁₆**

Verification: 2×16 + 15 = 32 + 15 = 47 ✓

---

### Example 2: convert `255` to hexadecimal

```
255 ÷ 16 = 15  remainder 15 (F)  ↑
 15 ÷ 16 =  0  remainder 15 (F)  │  read from bottom to top
```

**Result: FF₁₆**

Verification: 15×16 + 15 = 240 + 15 = 255 ✓

---

### Example 3: convert `419` to hexadecimal

```
419 ÷ 16 = 26  remainder  3      ↑
 26 ÷ 16 =  1  remainder 10 (A)  │  read from bottom to top
  1 ÷ 16 =  0  remainder  1      │
```

**Result: 1A3₁₆**

Verification: 1×256 + 10×16 + 3 = 256 + 160 + 3 = 419 ✓

---

### Example 4: convert `2938` to hexadecimal

```
2938 ÷ 16 = 183  remainder 10 (A)  ↑
 183 ÷ 16 =  11  remainder  7      │  read from bottom to top
  11 ÷ 16 =   0  remainder 11 (B)  │
```

**Result: B7A₁₆**

Verification: 11×256 + 7×16 + 10 = 2816 + 112 + 10 = 2938 ✓

---

### Example 5: convert `6719` to hexadecimal

```
6719 ÷ 16 = 419  remainder 15 (F)  ↑
 419 ÷ 16 =  26  remainder  3      │
  26 ÷ 16 =   1  remainder 10 (A)  │  read from bottom to top
   1 ÷ 16 =   0  remainder  1      │
```

**Result: 1A3F₁₆**

Verification: 1×4096 + 10×256 + 3×16 + 15 = 4096 + 2560 + 48 + 15 = 6719 ✓

---

## Reference table

Frequent values worth keeping in mind:

| Decimal | Hex | Meaning |
|---|---|---|
| 10 | A | first value with a letter |
| 15 | F | largest value in 1 hex digit (1 nibble) |
| 16 | 10 | first 2-digit hex number |
| 100 | 64 | |
| 127 | 7F | limit of signed TINYINT |
| 128 | 80 | sign bit active in 1 byte |
| 255 | FF | largest value in 1 byte (unsigned) |
| 256 | 100 | first 3-digit hex number |
| 1000 | 3E8 | |
| 4095 | FFF | largest value in 12 bits |
| 4096 | 1000 | first 4-digit hex number |
| 65535 | FFFF | largest value in 2 bytes (unsigned) |
| 65536 | 10000 | first 5-digit hex number |

---

## Python implementation

### Built-in functions

```python
# Hexadecimal → Decimal
int("2F", 16)      # 47
int("FF", 16)      # 255
int("1A3F", 16)    # 6719
int("0x1A3F", 16)  # 6719 (accepts 0x prefix)

# Decimal → Hexadecimal
hex(47)    # '0x2f'
hex(255)   # '0xff'
hex(6719)  # '0x1a3f'

# Without prefix, uppercase, with padding
f"{47:X}"      # '2F'
f"{255:X}"     # 'FF'
f"{255:04X}"   # '00FF'   — 4 digits
f"{6719:08X}"  # '00001A3F' — 8 digits
```

### Manual implementation: Hexadecimal → Decimal

```python
def hex_to_decimal(hex_str: str) -> int:
    """
    Converts a hexadecimal string to decimal
    via weighted sum.
    Example: '2F' → 47
    """
    # Value table for each hex digit
    values = {
        "0": 0,  "1": 1,  "2": 2,  "3": 3,
        "4": 4,  "5": 5,  "6": 6,  "7": 7,
        "8": 8,  "9": 9,  "A": 10, "B": 11,
        "C": 12, "D": 13, "E": 14, "F": 15,
    }

    hex_str = hex_str.upper()
    decimal = 0

    # Iterate over digits from right to left
    for position, digit in enumerate(reversed(hex_str)):
        decimal += values[digit] * (16 ** position)

    return decimal

# Tests
print(hex_to_decimal("2F"))    # 47
print(hex_to_decimal("FF"))    # 255
print(hex_to_decimal("1A3"))   # 419
print(hex_to_decimal("B7A"))   # 2938
print(hex_to_decimal("1A3F"))  # 6719
```

### Manual implementation: Decimal → Hexadecimal

```python
def decimal_to_hex(n: int) -> str:
    """
    Converts a non-negative integer to hexadecimal
    via successive division by 16.
    Example: 47 → '2F'
    """
    if n == 0:
        return "0"

    # Hex symbol table
    symbols = "0123456789ABCDEF"
    digits = []

    while n > 0:
        remainder = n % 16
        digits.append(symbols[remainder])
        n = n // 16

    # Digits were collected bottom-up; reverse them
    return "".join(reversed(digits))

# Tests
print(decimal_to_hex(47))    # '2F'
print(decimal_to_hex(255))   # 'FF'
print(decimal_to_hex(419))   # '1A3'
print(decimal_to_hex(2938))  # 'B7A'
print(decimal_to_hex(6719))  # '1A3F'
```

---

## Conclusion

Conversion between decimal and hexadecimal uses the same principles as decimal-to-binary conversion, with the base changing from 2 to 16:

- **Hex → Decimal:** multiply each digit by its weight (power of 16) and sum
- **Decimal → Hex:** divide successively by 16, reading remainders from bottom to top
- **Mind the letters:** A–F represent 10–15

**Pocket summary:**

- Remember the weights: 16⁰=1, 16¹=16, 16²=256, 16³=4096
- Always convert letters (A–F) to their values (10–15) before calculating
- In Python: `int("FF", 16)` and `hex(255)` solve it directly
- Familiarity with common values (`FF=255`, `FFFF=65535`) speeds up reading code

---

## References

- Patterson, D. A.; Hennessy, J. L. *Computer Organization and Design: The Hardware/Software Interface*. 5th edition. Morgan Kaufmann, 2013.
- Tanenbaum, A. S.; Austin, T. *Structured Computer Organization*. 6th edition. Pearson, 2012.
- Mano, M. M.; Ciletti, M. D. *Digital Design*. 5th edition. Pearson, 2012.
- Stallings, W. *Computer Organization and Architecture: Designing for Performance*. 10th edition. Pearson, 2016.
- Knuth, D. E. *The Art of Computer Programming, Volume 2: Seminumerical Algorithms*. 3rd edition. Addison-Wesley, 1997.
- Repository: `computer-science-fundamentals` — solid fundamentals for building robust systems.
