# function to create and print a list where the values are square of numbers between 1 and 30 (both included)
def funclist():
    l=[]
    for i in range(1,31):
        t=pow(i,2)
        l.append(t)
    print(*l)
funclist()