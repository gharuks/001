#Задача №3751. Пересечение множеств
print(*sorted(set(input().split()).intersection(set(input().split())), key=int))