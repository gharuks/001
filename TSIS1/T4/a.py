#Задача №3528. Ряд - 1
#Даны два целых числа A и B (при этом A≤B). Выведите все числа от A до B включительно.
a=int(input())
b=int(input())
s=""
for x in range(a,b+1): 
    m=str(x)
    s+=m+" "
print(s)