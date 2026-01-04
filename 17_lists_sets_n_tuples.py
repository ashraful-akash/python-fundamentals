#collection = single 'variable' used to store multiple values
# list = [] ordered and changeable . Dublicates OK
# Set = () ordered and immutable, but add/remove ok. no dublicates
# tuple = () orderesd and unchangeable. dublicates ok. faster than list

fruits = ["apple","orange", "banana","coconut"]
# fruits = {"apple","orange", "banana","coconut"}
# fruits = ("apple","orange", "banana","coconut")

fruits.append("pineapple") #to add in list
print(dir(fruits))
print(help(fruits))
fruits.remove("apple") #to remove in list
fruits.insert(0,"pine")
fruits.sort()
fruits.reverse()
fruits.clear()

print(fruits[0])

for fruit in fruits:
    print(fruit)
