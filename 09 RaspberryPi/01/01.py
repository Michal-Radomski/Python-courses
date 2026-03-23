# number = -5

# if number > 0:
#     print("Positive number")
# elif number < 0:
#     print("Negative number")
# else:
#     print("Zero")


# score = 85

# if score >= 90:
#     print("Grade: A")
# elif score >= 80:
#     print("Grade: B")
# elif score >= 70:
#     print("Grade: C")
# else:
#     print("Grade: F")


# x = int(input("Enter the number"))
# if x > 0:
#     print("x is positive")
# else:
#     print("x is negative")


# fruits = ["apple", "banana", "cherry"]

# for index, elem in enumerate(fruits):
#     print(f"Index: {index}, Element: {elem}")

# for index in range(len(fruits)):
#     elem = fruits[index]
#     print(f"Index: {index}, Element: {elem}")


# d = {"a": 10, "b": 20, "c": 30, "d": 40}
# for i in d:
#     print("keys: ", i)
#     print("values :", d[i])


for i in range(0, 5, 2):
    print(i)  # 0 2 4


print(list(range(0, 5, 2)))  # [0, 2, 4]


sum = 0
n = int(input("Enter the value"))
for i in range(1, n + 1):
    sum = sum + i
print("sum of print values:", sum)


# Factorial
n = int(input("Enter the number"))
fact = 1
if n < 0:
    print("sorry we cannot find factorial of this number")
elif n == 0:
    print("factorial is 1")
else:
    for i in range(1, n + 1):
        fact = fact * i
    print("factorial of a number is ", fact)
