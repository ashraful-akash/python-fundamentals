# keyword arguments = an argument preceded by an identifier
#                   helps with readability
#                   order of arguments doesnt matter
#                   1. positional 2. default 3. KEYWORD 4. arbitrary


def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")


hello("Hello",title="Mr.", last="John",first="James")



for x in range (1,11):
    print(x, end ="")
print()
print ("1","2","3","4","5",sep="-")

def get_phone(country,area,first,last):
    return f"+{country}{area}-{first}-{last}"

phone_num = get_phone(country=880,area=13,first=2456,last=7880)

print(phone_num)
