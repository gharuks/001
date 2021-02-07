#Задача №3530. Ряд - 3
#Дано натуральное число n. Напечатайте все n-значные нечетные натуральные числа в порядке убывания.
a=int(input())
s=""
t=10*a
if a%2==0:
    for x in range(a+1,t,2): 
        if x>a+1:
            s+=" "
        m=str(x)
        s+=m
else: 
    for x in range(a,t,2): 
            if x>a:
                s+=" "
            m=str(x)
            s+=m
res=s[::-1]
print(res)