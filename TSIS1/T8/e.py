#Задача №3794. Принадлежит ли точка кругу
import math
def IsPointInCircle(x, y, xc, yc, r):
    return (x - xc)**2+(y - yc)**2<=r**2
if IsPointInCircle(float(input()), float(input()), float(input()), float(input()), float(input()))==True:
    print("YES")
else:
    print("NO")