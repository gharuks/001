#Write a Python function that takes a list and returns a new list with unique elements of the first list.
def f(a):
    # res=[]
    # for i in a:
    #     if i not in res:
    #         res.append(i)
    # return res
    return list(set(a))
print(f(input().split()))
