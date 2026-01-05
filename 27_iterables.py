# iterables = an object/collection that can return its elements one at a time,
#             allowing it to be iterated over in a loop

numbers = [1,2,3,4,5]

for item in numbers:
    print(item, end =" ")
print()

fruits = {"apple","orange","banana","coconut"}

for fruit in fruits:
    print(fruit)

name = "Ashraful"
for ch in name:
    print(ch, end = " ")
print()

my_dictionary= {"A":1, "B":2}

for key, value in my_dictionary.items():
    print(key, value)