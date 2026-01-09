#if __name__ == __main__ : (this script can be imported OR run standalone)
#                           Fuctions and classes in this module can be reused 
#                           without the main block of code executing

def fav_food(food):
    print(f"Your fav food is {food}")

def main():
    print("This is script1")
    fav_food("pizza")
    print("Goodbye")

if __name__ == '__main__':
    main()