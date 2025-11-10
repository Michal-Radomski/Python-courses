# Basics 2

# * Conditional Logic
a = True
b = False
if a and b:
    print("Both a and b are true")
elif a:
    print("Only a is true")
elif b:
    print("Only b is true")
else:
    print("Both a and b are false")

is_old = True
is_licensed = True

if is_old:
    print("You are old enough to drive!")
elif is_licensed:
    print("You can drive now!")
else:
    print("You are not of age!")

print("ok ok")
print()

# improved version
if is_old and is_licensed:
    print("You are old enough to drive, and you have a license!")
else:
    print("You are not of age!")

print("ok ok")
