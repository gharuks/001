#Задача №3850. Сжатие списка
a=input().split()
for x in a:
    if x!='0':
        print(x)
for x in a:
    if x=='0':
        print(x)
