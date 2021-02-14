#Задача №3835. Наименьший положительный
a=input().split()
for x in range(len(a)):
    k=int(a[x])
    if k<0:
        a.remove(a[x])
a.sort()
print(a[0])

