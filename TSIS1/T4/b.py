#Задача №3529. Ряд - 2
#Даны два целых числа A и В. Выведите все числа от A до B включительно, в порядке возрастания, если A < B, или в порядке убывания в противном случае.
a=int(input())
b=int(input())
s=""
if a<b:
    for x in range(a,b+1):
        if x>a and x!=b+1:
            s+=" " 
        m=str(x)
        s+=m
else:
    for x in range(b,a+1): 
        if x>b and x!=a+1:
            s+=" "
        m=str(x)
        s+=m
    s=s[::-1]
print(s)