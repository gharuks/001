#Задача №3457. Следующее и предыдущее
a=int(input())
b="The next number for the number {} is {}."
c="The previous number for the number {} is {}."
print(b.format(a, a+1))
print(c.format(a, a-1)) 