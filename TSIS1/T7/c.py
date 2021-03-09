#Задача №3644. Список степеней двойки
n=int(input())
res=1
i=2
print(res, end=" ")
while(res<n):
    res*=i
    print(res, end=" ")