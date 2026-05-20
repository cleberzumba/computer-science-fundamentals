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


# Prime numbers and divisibility
#
# A prime number is a natural number > 1 with only two divisors: 1 and itself.
# Example: 7 is prime. 8 is not (divisors: 1, 2, 4, 8).
# A divisor of n is any integer that divides n with remainder 0 (using %).

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
print(is_prime(7))    # True
print(is_prime(8))    # False
print(is_prime(13))   # True

# Lists all divisors of n by testing integers from 1 to n with the modulo operator.
def divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]
print(divisors(12))   # [1, 2, 3, 4, 6, 12]
print(divisors(7))    # [1, 7]

# Optimization: testing up to sqrt(n) is enough — reduces complexity from O(n) to O(sqrt(n)).
