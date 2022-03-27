#Global and local variables

#global(can be used by all functions)
x = 10
y = 20
print(x)

#local(can only be used in the given function)
def func1():
    x = 20
    print(x)
    global y
    y += 10
    print(y)
func1()
#in func1(), y is a global variable while x is a local variable