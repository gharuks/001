#Задача №3447. Дзета-функция. Тема 1
import math
n=1
x=0
while n<11:
    x+=1/(n**2)
    n+=1
print(math.sqrt(6*x))