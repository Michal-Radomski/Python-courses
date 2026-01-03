import cmath

# Rules about variable names
# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)

# x = 10
# y = "Mich"
# age = 30
# carname = "ASTON MARTIN"
# total_volume = 50

# Assigning values to multiple variables at once
player_name, total_score, initial_score = "Mich", 100, 0
print(player_name, total_score, initial_score)

# PYTHON NUMBERS
# Int, float, complex
my_age = 30
amount = -30.789
car_model_name = 3j

# Complex
# Direct literal
z1 = 3 + 4j
print(z1)  # (3+4j)
print(type(z1))  # <class 'complex'>

# Using complex() function
z2 = complex(3, 4)
print(z2)  # (3+4j)

# Real part only
z3 = complex(5)  # (5+0j)

z1 = 3 + 4j
z2 = 1 - 2j

print(z1 + z2)  # (4+2j)
print(z1 * z2)  # (11+2j)
print(z1 / z2)  # (2.2+2.8j)
print(abs(z1))  # 5.0 (magnitude)

# Access parts
print(z1.real)  # 3.0
print(z1.imag)  # 4.0
print(z1.conjugate())  # (3-4j)


z = 3 + 4j
print(f"Magnitude: {abs(z):.1f}")  # 5.0
print(f"Phase: {cmath.phase(z):.2f} rad")  # 0.93 radians
print(f"Polar form: {cmath.polar(z)}")  # (5.0, 0.9272952180016122)

z = 3 + 4j
print(cmath.sqrt(z))  # (2+1j) - complex square root
print(cmath.sin(z))  # (3.8537-27.0168j)
print(cmath.phase(z))  # 0.9273 radians (angle)
print(cmath.polar(z))  # (5.0, 0.9273) - (magnitude, angle)
print(cmath.rect(5, 0.9273))  # Converts back to (3+4j)

# Type conversion
my_new_amount = int(amount)
print(type(my_new_amount))  # <class 'int'>


# my_new_age = float(car_model_name)
# print(type(my_new_age)) #* Error
print(type(car_model_name))  # <class 'complex'>

print(int(30.30))  # 30

my_name = "Mich"
score = 100
isAdult = True
complex_number = 1j
percentage_wining = 60.5

# * String modification
paragraph = "  I have an awesome Aston Martin in my garage  "
# upper, lower, strip, replace
print(paragraph.strip())  # *I have an awesome Aston Martin in my garage
