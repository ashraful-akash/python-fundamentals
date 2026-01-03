name = input("enter your full name: ")


## 1st occurance use .find()
#result = len(name)

result = name.find("a")
#result = name.find(" ")

print (result)


## last orccurence , use .rfind()

r = name.rfind("z")
print(r)

name = name.capitalize()
name = name.upper()
name = name.lower()
result = name.isdigit()
result = name.isalpha()

phone_number = input("Enter ur phone number: ")

phone_number = phone_number.replace("-"," ")
print(phone_number)

## validate username
#  username is no more than 12 char
# username must not conatain spaces
#username must not contain digits

username = input ("Enter a username: ")
if len(username) > 12:
    print("Cant be more than 12 char.")
elif not username.find(" ")== -1:
    print("Your username cant contain spaces")
elif not username.isalpha():
    print("Username cant contain numbers")
else:
    print(f"Welcome {username}")