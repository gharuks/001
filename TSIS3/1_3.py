#Задача №3840. Переставить в обратном порядке
a=list(input().split())
# for x in range(-1,-len(a)-1,-1):
#     print(a[x])
print(*a[::-1])