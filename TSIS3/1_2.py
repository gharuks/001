#Задача №3835. Наименьший положительный
a=input().split()
min=1000
for x in range(len(a)):
    k=int(a[x])
    if k<min and k>0:
        min=k
print(min)

