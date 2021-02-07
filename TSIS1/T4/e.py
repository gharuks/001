#Задача №3532. Сумма кубов
a=int(input())
s=0
for x in range(1,a+1):
    s+=x**3
print(s)