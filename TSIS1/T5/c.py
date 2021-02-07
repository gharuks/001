#Задача №3610. Округление по российским правилам
a=float(input())
if int(a%1*10)<5:
    print(int(a))
else:
    print(int(a+1))