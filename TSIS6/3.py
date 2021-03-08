#Write a Python function to multiply all the numbers in a list
# a=input().split()
# s=1
# for x in a:
#   t=int(x)
#   s*=t
# print(s)
def mult(a):
    s=1
    for x in a:
        t=int(x)
        s*=t
    return s
print(mult(input().split()))