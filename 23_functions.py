#functions = a block of reusable code
#           place () after the function name to invoke it

def happy_bd(name,age):
    print(f"Happy birthday to {name}!")
    print(f"You are {age} years old!")
    print("Happy Birthday to you!")
    print()

happy_bd("Bro",20)
happy_bd("Ash",25)
happy_bd("Akash",25)


def add(x,y):
    z = x + y
    return z

print(add(2,3))