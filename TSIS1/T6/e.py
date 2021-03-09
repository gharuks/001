#Задача №3739. Первое и последнее вхождение
s=input()
if s.count('f')==1:
    print(s.index('f'))
elif s.count('f')>=2:
    print(s.index('f'), s.rindex('f'))
else:
    pass
    