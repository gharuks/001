#Задача №3791. Длина отрезка
from math import sqrt
def dis(a,b,c,d):
    return sqrt((a-c)**2+(b-d)**2)
print(dis(float(input()),float(input()),float(input()),float(input())))
