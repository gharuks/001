#Задача №3645. Точная степень двойки
n=int(input())
i=2
while(n>0):
    x=n/2
    if n==1:
        print("YES")
        break
    if x==0:
        print("NO")
        break
    elif x==1:
        print("YES")
        break
    n/=2