#Задача №3853. Большой сдвиг
n=input().split()
k=int(input())
if k>=0:
    for i in range(k,):
        n.insert(0, n.pop(-1))
else:
    for i in range(abs(k)):
        n.append(n.pop(0))
print(*n)