# Membership operators = used to test whether a value or variable is found in a sequence
#                       (string, list, tuple, set, or dictionary)
#                       1. in
#                       2. not in

word = "APPLE"

letter = input("Guess a letter in the secret word: ")

if letter in word:
    print(f"There is a {letter}")

else:
    print(f"{letter} was not found")


students = {"Spongebob", "Patrik","Sandy"}
student = input("Enter the name of a student: ")

if student in students:
    print(f"{student} is a studnet")
else:
    print(f"{student} was not found")


grades = { "Sandy" : "B",
          "Spongebob": "A"}

student = input("Enter the name of a student: ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else: print(f"{student} was not found")