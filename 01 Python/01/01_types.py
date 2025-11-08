# Fundamental data types
# int -> 3, 5, -2
# float -> 0.5
# complex
# str 
# bool 
# list 
# tuple
# set 
# dict 
# Non

# Number and float
print(type(2 + 4))
print(type(2.5 + 4.5))
print(2 + 4)
print(type(2 - 4))
print(type(2 * 4))
print(2 / 4)
print(2.1 + 4.9)
print(2 ** 4)
print(10 // 4) # -> integer rounded down: 2
print(10 % 4) # -> modulo: 2

# Math functions
print(round(3.1))
print(round(3.5))
print(abs(0))
print(abs(-3.1))
print(abs(3.1))

# Bin()
number = 15
binary_representation = bin(number)
print("Binary of", number, "is", binary_representation)
# Output: Binary of 15 is 0b1111

negative_number = -7
print("Binary of", negative_number, "is", bin(negative_number))
# Output: Binary of -7 is -0b111

# Complex
# Create complex number with real part 3 and imaginary part 4
z1 = complex(3, 4)
print("z1 =", z1)
# Output: z1 = (3+4j)

# Another complex number using literal syntax
z2 = 2 + 5j
print("z2 =", z2)
# Output: z2 = (2+5j)

# Access real and imaginary parts
print("Real part of z1:", z1.real)
print("Imaginary part of z1:", z1.imag)
