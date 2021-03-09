#Задача №3792. Принадлежит ли точка квадрату - 1
def IsPointInSquare(x, y):
    return -1<=x<=1 and -1<=y<=1 
if IsPointInSquare(float(input()),float(input()))==True:
    print("YES")
else:
    print("NO")