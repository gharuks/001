#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters
def letters(s):
    res={"u":0, "l":0}
    u=0
    l=0
    for i in s:
        if i.isupper():
            res["u"]+=1
        elif i.islower():
            res["l"]+=1
        else:
            pass
    print("No. of Upper case characters : ", res["u"])
    print("No. of Lower case characters : ", res["l"])
letters(input())
