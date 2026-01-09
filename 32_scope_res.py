#variable scope = where a variable visible and accessible
# scope resolution = (LGEB) local> enclosed > global > built in

#local
def func1():
    a =1 
    print(a)

def func2():
    b =2 
    print(b)

func1()
func2()

#enclosed
def func3():
    x=4

    def func4():
        print(x)
    func4()
func3()


