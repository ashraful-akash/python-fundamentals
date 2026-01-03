# while loop = execute some code while some coditions remains true
name = input("Enter your name: ")


# if name == "":
#     print("You didnt enter your name")
# else:
#     print(f"Hello {name}")

while name == "":
    print("You didnt enter your name")
    name = input("Enter your name")
print(f"Hello {name}")