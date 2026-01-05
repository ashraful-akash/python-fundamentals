#dictionairy = a collection of {key:value} pairs
#               ordered and changeable. No duplicates


capitals ={"USA": "Washington D.C",
            "India":"New Delhi",
            "China":"Beijing",
            "Russia":"Moscow"  }

#print(dir(capitals))
#print(help(capitals))
#print(capitals.get("Japan"))

capitals.update({"Germany":"Berlin"})
capitals.update({"USA":"Detroit"})
# capitals.pop("China")
# capitals.popitem()  #pops last insert item
# capitals.clear()

print(capitals)

