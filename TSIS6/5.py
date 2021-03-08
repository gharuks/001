#Write a Python program to reverse a string
def revfunc(s):
    res=''
    i=len(s)
    while(i>0):
        res+=s[i-1]
        i-=1
    return res

print(revfunc(input()))