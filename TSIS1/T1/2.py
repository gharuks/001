#Задача №3444. Факториал. Тема 1
def func(n):
    if n==0:
        return 1
    else:
        return n*func(n-1)
print(func(20))
