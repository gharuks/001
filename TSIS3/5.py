#Задача №3760. Словарь синонимов
n=int(input())
d={}
for i in range(n):
    a,b=input().split()
    d[a]=b
s=input()
for key, value in d.items():
    if s==value:
        print(key)
    if s==key:
        print(value)
