#a Python program to access a function inside a function
def func1(a):
    def func2(b):
        return b+b
    return func2(a)
print(func1(input()))
