#Задача №3753. Кубики
n,m=list(map(int, input().split()))
a=set()
b=set()
for i in range(n):
    a.add(int(input()))
for i in range(m):
    b.add(int(input()))
print(len(a.intersection(b)))
print(*sorted(a.intersection(b)))
print(len(a.difference(b)))
print(*sorted(a.difference(b)))
print(len(b.difference(a)))
print(*sorted(b.difference(a)))