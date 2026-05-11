# Binary ↔ Hexadecimal Conversion

> Part of the [computer-science-fundamentals](https://github.com/) repository — a series of studies on Computer Science fundamentals applied to the real world.

---

## Table of Contents

- [Introduction](#introduction)
- [What is hexadecimal?](#what-is-hexadecimal)
- [Why is hexadecimal so widely used in computing?](#why-is-hexadecimal-so-widely-used-in-computing)
- [Equivalence table: 4 bits = 1 hex digit](#equivalence-table-4-bits--1-hex-digit)
- [Binary → Hexadecimal](#binary--hexadecimal)
- [Hexadecimal → Binary](#hexadecimal--binary)
- [Python implementation](#python-implementation)
- [Conclusion](#conclusion)
- [References](#references)

---

## Introduction

Hexadecimal (base 16) is everywhere in computing: memory addresses, web colors, byte values, cryptographic hashes, memory dumps, and error codes. Knowing how to convert between binary and hexadecimal is a foundational skill — and fortunately, it's one of the simplest and most direct conversions out there.

The reason is mathematical: 16 is a power of 2 (16 = 2⁴), so each hexadecimal digit corresponds to exactly 4 bits. This enables conversion by grouping, without complex calculations.

---

## What is hexadecimal?

The hexadecimal system (base 16) uses 16 symbols: digits `0` through `9` and letters `A` through `F`, where:

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

| Position | 2 | 1 | 0 |
|---|---|---|---|
| Weight | 16² | 16¹ | 16⁰ |
| Value | 256 | 16 | 1 |

---

## Why is hexadecimal so widely used in computing?

Computers work in binary, but writing long binary numbers is inconvenient and error-prone. For example, the number `11111111 00001010 10110011 01000110` is hard to read and type.

The elegant solution: since 4 bits correspond to a single hex digit, the same number becomes compact and readable in hex: `FF 0A B3 46`.

**Real-world applications:**

- **Memory addresses:** `0x7FFE2A3B`
- **Web colors:** `#FF5733` (orange-red)
- **Bytes in dumps:** 1 byte = exactly 2 hex digits
- **Hashes:** MD5, SHA-1, SHA-256 are displayed in hex
- **Error codes:** `0x80004005` (HRESULT in Windows)
- **MAC addresses:** `00:1A:2B:3C:4D:5E`
- **Unicode codepoints:** `U+1F680` for the rocket emoji 🚀

---

## Equivalence table: 4 bits = 1 hex digit

This is the most important table to master conversion. **Worth memorizing.**

| Binary (4 bits) | Decimal | Hexadecimal |
|---|---|---|
| 0000 | 0 | 0 |
| 0001 | 1 | 1 |
| 0010 | 2 | 2 |
| 0011 | 3 | 3 |
| 0100 | 4 | 4 |
| 0101 | 5 | 5 |
| 0110 | 6 | 6 |
| 0111 | 7 | 7 |
| 1000 | 8 | 8 |
| 1001 | 9 | 9 |
| 1010 | 10 | A |
| 1011 | 11 | B |
| 1100 | 12 | C |
| 1101 | 13 | D |
| 1110 | 14 | E |
| 1111 | 15 | F |

Each group of 4 bits is called a **nibble** (half a byte). A **byte** (8 bits) is represented by exactly 2 hex digits.

---

## Binary → Hexadecimal

### Algorithm

1. Group the bits into sets of 4, from right to left
2. If the leftmost group has fewer than 4 bits, pad with `0`s on the left
3. Convert each 4-bit group to its corresponding hex digit (use the table)
4. Concatenate the hex digits

---

### Example 1: convert `1101` to hexadecimal

```
Bits:   1101
Group:  1101  (already has 4 bits)
Hex:    D
```

**Result: 1101₂ = D₁₆**

---

### Example 2: convert `11111111` to hexadecimal

```
Bits:    11111111
Groups:  1111  1111  (grouped by 4, right → left)
Hex:     F     F
```

**Result: 11111111₂ = FF₁₆**

> This is the maximum value of 1 byte (255 in decimal).

---

### Example 3: convert `101101111010` to hexadecimal

```
Bits:    101101111010
Groups:  1011  0111  1010  (grouped by 4, right → left)
Hex:     B     7     A
```

**Result: 101101111010₂ = B7A₁₆**

---

### Example 4: number with leftover bits (needs zero padding)

Converting `10110110` (8 bits) is straightforward. But what about `10110` (5 bits)?

```
Bits:    10110
Padded:  00010110  (add leading zeros to complete a multiple of 4)
Groups:  0001  0110
Hex:     1     6
```

**Result: 10110₂ = 16₁₆**

> **Important:** leading zeros don't change the numeric value. `10110` and `00010110` represent the same number.

---

## Hexadecimal → Binary

The opposite direction is even simpler: each hex digit becomes exactly 4 bits.

### Algorithm

1. For each hex digit, write its 4-bit representation (consulting the table)
2. Concatenate all the groups

---

### Example 1: convert `D` to binary

```
Hex:    D
4 bits: 1101
```

**Result: D₁₆ = 1101₂**

---

### Example 2: convert `FF` to binary

```
Hex:    F     F
4 bits: 1111  1111
```

**Result: FF₁₆ = 11111111₂**

---

### Example 3: convert `2F` to binary

```
Hex:    2     F
4 bits: 0010  1111
```

**Result: 2F₁₆ = 00101111₂** (or `101111₂` removing leading zeros)

---

### Example 4: convert `B7A` to binary

```
Hex:    B     7     A
4 bits: 1011  0111  1010
```

**Result: B7A₁₆ = 101101111010₂**

---

### Example 5: convert `0x1A3F` to binary

```
Hex:    1     A     3     F
4 bits: 0001  1010  0011  1111
```

**Result: 1A3F₁₆ = 0001101000111111₂**

> The `0x` prefix is just notation indicating the number is hexadecimal — it's not part of the value.

---

## Python implementation

Python provides built-in functions for these conversions, but understanding the manual implementation is valuable.

### Built-in functions

```python
# Hex to decimal and then to binary
int("FF", 16)          # 255 (hex string → decimal)
bin(int("FF", 16))     # '0b11111111'

# Decimal to hex
hex(255)               # '0xff'
hex(255)[2:]           # 'ff' (without prefix)
f"{255:X}"             # 'FF' (uppercase format)
f"{255:04X}"           # '00FF' (with 4-digit padding)

# Direct conversion between the two using int as bridge
int("1101", 2)         # 13
hex(int("1101", 2))    # '0xd'
bin(int("D", 16))      # '0b1101'
```

### Manual implementation: Binary → Hexadecimal

```python
def binary_to_hex(binary: str) -> str:
    """
    Converts a binary string to hexadecimal
    via 4-bit grouping.
    Example: '11111111' → 'FF'
    """
    # Equivalence table
    table = {
        "0000": "0", "0001": "1", "0010": "2", "0011": "3",
        "0100": "4", "0101": "5", "0110": "6", "0111": "7",
        "1000": "8", "1001": "9", "1010": "A", "1011": "B",
        "1100": "C", "1101": "D", "1110": "E", "1111": "F",
    }

    # Pad with leading zeros up to multiple of 4
    missing = (4 - len(binary) % 4) % 4
    binary = "0" * missing + binary

    # Group by 4 and convert each group
    hex_str = ""
    for i in range(0, len(binary), 4):
        group = binary[i:i+4]
        hex_str += table[group]

    return hex_str

# Tests
print(binary_to_hex("1101"))          # 'D'
print(binary_to_hex("11111111"))      # 'FF'
print(binary_to_hex("101101111010"))  # 'B7A'
print(binary_to_hex("10110"))         # '16'
```

### Manual implementation: Hexadecimal → Binary

```python
def hex_to_binary(hex_str: str) -> str:
    """
    Converts a hexadecimal string to binary
    via 4-bit expansion of each digit.
    Example: 'FF' → '11111111'
    """
    # Equivalence table (inverse)
    table = {
        "0": "0000", "1": "0001", "2": "0010", "3": "0011",
        "4": "0100", "5": "0101", "6": "0110", "7": "0111",
        "8": "1000", "9": "1001", "A": "1010", "B": "1011",
        "C": "1100", "D": "1101", "E": "1110", "F": "1111",
    }

    # Normalize to uppercase
    hex_str = hex_str.upper()

    # Concatenate the 4 bits of each digit
    binary = ""
    for digit in hex_str:
        binary += table[digit]

    return binary

# Tests
print(hex_to_binary("D"))     # '1101'
print(hex_to_binary("FF"))    # '11111111'
print(hex_to_binary("2F"))    # '00101111'
print(hex_to_binary("B7A"))   # '101101111010'
print(hex_to_binary("1A3F"))  # '0001101000111111'
```

---

## Conclusion

Conversion between binary and hexadecimal is one of the most elegant in computing. Since 16 = 2⁴, the relationship is direct: **1 hex digit = 4 bits**.

**Pocket summary:**

- **Binary → Hex:** group bits by 4 (from right to left), pad with zeros if needed, and convert each group
- **Hex → Binary:** each hex digit becomes exactly 4 bits
- Memorize the table from `0000`–`1111` (0–F): this makes conversion automatic
- In Python: `bin()`, `hex()`, and `int(s, base)` solve any conversion
- Hexadecimal is used in memory addresses, colors, bytes, hashes — worth mastering

---

## References

- Patterson, D. A.; Hennessy, J. L. *Computer Organization and Design: The Hardware/Software Interface*. 5th edition. Morgan Kaufmann, 2013.
- Tanenbaum, A. S.; Austin, T. *Structured Computer Organization*. 6th edition. Pearson, 2012.
- Mano, M. M.; Ciletti, M. D. *Digital Design*. 5th edition. Pearson, 2012.
- Stallings, W. *Computer Organization and Architecture: Designing for Performance*. 10th edition. Pearson, 2016.
- Knuth, D. E. *The Art of Computer Programming, Volume 2: Seminumerical Algorithms*. 3rd edition. Addison-Wesley, 1997.
- Repository: `computer-science-fundamentals` — solid fundamentals for building robust systems.
