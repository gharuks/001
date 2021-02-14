#Задача №3850. Сжатие списка
a=input().split()
cnt=0
for x in range(len(a)):
    if a[x]==0:
        cnt+=1
        a.remove(a[x])
for x in range(cnt):
    a.append(0)
print(*a)
