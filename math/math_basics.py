# This code calculates the GCD (Greatest Common Divisor) between two numbers using the Euclidean algorithm by subtraction, recursively.
#
# GCD is the Greatest Common Divisor between two numbers and is the largest number that divides both without leaving a remainder.
# Example: GCD(10, 15) = 5 (because 5 divides both 10 and 15, and is the largest number that does so).

def gcd(a,b):
	if a == b:
		return a
	elif a > b:
		a = a - b
		return gcd(a,b)
	else:
		b = b - a
		return gcd(a,b)
print(gcd(10,15))   # 5



# This code calculates the LCM (Least Common Multiple) between two numbers using the mathematical relationship: LCM(a, b) = (a * b) / GCD(a, b).
# The GCD is calculated by the Euclidean algorithm by subtraction, recursively.
#
# LCM is the Least Common Multiple between two numbers and is the smallest number that is a multiple of both at the same time.
# Example: LCM(10, 15) = 30 (because 30 is the smallest number divisible by both 10 and 15).
#
# The LCM (Least Common Multiple) has a mathematical relationship with the GCD. The LCM is the product of the two numbers divided by the GCD.

def gcd(a, b):
    if a == b:
        return a
    elif a > b:
        return gcd(a - b, b)
    else:
        return gcd(a, b - a)
def lcm(a, b):
    return (a * b) // gcd(a, b)
print(lcm(10, 15))   # 30


# Math operators
+    # addition              10 + 3 = 13
-    # subtraction           10 - 3 = 7
*    # multiplication        10 * 3 = 30
/    # division (regular)    10 / 3 = 3.3333...
//   # integer division      10 // 3 = 3
**   # exponentiation        10 ** 3 = 1000
%    # modulo (remainder)    10 % 3 = 1

  
# Exponentiation = raising a number to a power.
2 ** 3      # 2³ = 8
5 ** 2      # 5² = 25
10 ** 6     # 10⁶ = 1,000,000
2 ** 0.5    # square root of 2 ≈ 1.414


# Returns the remainder of the division:
10 % 3     # 1   (10 ÷ 3 = 3 with remainder 1)
15 % 5     # 0   (15 is divisible by 5)
7 % 2      # 1   (odd number)
8 % 2      # 0   (even number)
