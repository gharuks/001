#print the even numbers from a given list
def evennums(a):
    res=[]
    for i in a:
        t=int(i)
        if t%2==0:
            res.append(t)
    return res
print(*evennums(input().split()))