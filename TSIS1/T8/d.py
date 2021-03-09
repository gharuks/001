#Задача №3792. Принадлежит ли точка квадрату - 2
def IsPointInSquare(x, y):
    return -0.5<=x<=0.5 and -0.5<=y<=0.5 or x==1 and y==0 or x==-1 and y==0 or x==0 and y==1 or x==0 and y==-1
if IsPointInSquare(float(input()),float(input()))==True:
    print("YES")
else:
    print("NO")