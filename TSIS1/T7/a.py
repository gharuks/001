#Задача №3642. Список квадратов
a=int(input())
l=[]
i=1
while(i*i<=a):
    l.append(i*i)
    i+=1
print(*l)