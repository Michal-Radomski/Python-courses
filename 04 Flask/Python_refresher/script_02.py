# # -- While loop --
# number = 7
# play = input("Would you like to play? (Y/n) ")

# while play != "n":
#     user_number = int(input("Guess our number: "))
#     if user_number == number:
#         print("You guessed correctly!")
#     elif abs(number - user_number) == 1:
#         print("You were off by 1.")
#     else:
#         print("Sorry, it's wrong!")

#     play = input("Would you like to play? (Y/n) ")


# # -- The break keyword --
# while True:
#     play = input("Would you like to play? (Y/n) ")

#     if play == "n":
#         break  # Exit the loop

#     user_number = int(input("Guess our number: "))
#     if user_number == number:
#         print("You guessed correctly!")
#     elif abs(number - user_number) == 1:
#         print("You were off by 1.")
#     else:
#         print("Sorry, it's wrong!")


# # -- For loop --
# friends = ["Rolf", "Jen", "Bob", "Anne"]
# for friend in friends:
#     print(f"{friend} is my friend.")

# # -- For loop 2 -- Average
# grades = [35, 67, 98, 100, 100]
# total = 0
# amount = len(grades)

# for grade in grades:
#     total += grade
# print(total / amount)  # 80.0

# # -- Rewritten using sum() --
# grades = [35, 67, 98, 100, 100]
# total = sum(grades)
# amount = len(grades)
# print(total / amount)  # 80.0
# # * You kinda just have to "know" that exists. It takes time and experience, but searching for almost _everything_ really helps. For example, you could've searched for "sum list of numbers python".

# * List comprehensions in Python
numbers = [1, 3, 5]
squares = [x**2 for x in numbers]
print(squares)  # [1, 9, 25]

# -- Dealing with strings --
friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = []

for friend in friends:
    if friend.startswith("S"):
        starts_s.append(friend)
print(starts_s)  # ['Sam', 'Samantha', 'Saurabh']


# -- Can make a new list of friends whose name starts with S --
friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = [friend for friend in friends if friend.startswith("S")]
print(starts_s)  # ['Sam', 'Samantha', 'Saurabh']

# -- List comprehension creates a _new_ list --
friends = ["Sam", "Samantha", "Saurabh"]
starts_s = [friend for friend in friends if friend.startswith("S")]  # same as above

print(friends)  # ['Sam', 'Samantha', 'Saurabh']
print(starts_s)  # ['Sam', 'Samantha', 'Saurabh']
print(friends is starts_s)  # False
print(friends == starts_s)  # True
print(
    "friends: ", id(friends), " starts_s: ", id(starts_s)
)  # friends:  129593678312640  starts_s:  129593677757952

# * Dictionaries
friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}
friend_ages["Bob"] = 20
print(friend_ages)  # {'Rolf': 24, 'Adam': 30, 'Anne': 27, 'Bob': 20}
print(friend_ages["Bob"])  # 20

# -- List of dictionaries --
friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27},
]
print(
    friends
)  # [{'name': 'Rolf Smith', 'age': 24}, {'name': 'Adam Wool', 'age': 30}, {'name': 'Anne Pun', 'age': 27}]

# -- Iteration --
student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}
for student in student_attendance:
    print(f"{student}: {student_attendance[student]}")
# Rolf: 96
# Bob: 80
# Anne: 100

# Better
for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")
# Rolf: 96
# Bob: 80
# Anne: 100

# -- Using the `in` keyword --
if "Bob" in student_attendance:
    print(f"Bob: {student_attendance[student]}")  # Bob: 100
else:
    print("Bob isn't a student in this class!")

# -- Calculate an average with `.values()` --
attendance_values = student_attendance.values()
print(sum(attendance_values) / len(attendance_values))  # 92.0
