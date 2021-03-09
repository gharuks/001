#Задача №3643. Минимальный простой делитель
n=int(input())
min=2*10**9
for i in range(2,n+1):
    if n%i==0 and i<min:
        min=i
print(min)
    