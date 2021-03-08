# Write a Python function to sum all the numbers in a list.
def sum(n):
    s=0
    for i in n:
        t=int(i)
        s+=t
    return(s)
print(sum(input().split()))