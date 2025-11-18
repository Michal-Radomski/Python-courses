import re

string = "this is a really cool string really!"

a = re.search("really", string)
print(a)  # <re.Match object; span=(10, 16), match='really'>

# the below 4 commands will give error if the searching string does not exist.
print(a.span())  # (10, 16)
print(a.start())  # 10
print(a.end())  # 16
print(a.group())  # really

pattern = re.compile("really")

b = pattern.search(string)
c = pattern.findall(string)

pattern = re.compile("this is a really cool string really!")
d = pattern.fullmatch("this is a really cool string really!")
e = pattern.fullmatch(
    "hello this is a really cool string really!"
)  # this should be exact match, otherwise returns none

pattern = re.compile("really")
f = pattern.match(
    "really cool feature"
)  # it starts matching from the first character otherwise returns none
g = pattern.match("yo really")

print(f"b: {b}")  # b: <re.Match object; span=(10, 16), match='really'>
print(f"c: {c}")  # c: ['really', 'really']
print(
    f"d: {d}"
)  # d: <re.Match object; span=(0, 36), match='this is a really cool string really!'>
print(f"e: {e}")  # e: None
print(f"f: {f}")  # f: <re.Match object; span=(0, 6), match='really'>
print(f"g: {g}")  # g: None

pattern2 = re.compile(r"([a-zA-Z])([a])", re.IGNORECASE | re.MULTILINE)
print(pattern2.search(string))  # <re.Match object; span=(11, 13), match='ea'>

email_pattern = re.compile(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
check_email = email_pattern.fullmatch("test@test.com")

password_patter = re.compile(r"([a-zA-Z0-9@#$%]{8,}$)")
check_password = password_patter.fullmatch("12345678")

if check_email and check_password:
    print(
        "Both email and password are correct."
    )  # Both email and password are correct.
else:
    print("Try again.")
