#function that takes a number as a parameter and check the number is prime or not
def prime(n):
    if n==1:
        return False
    if n==2: 
        return True
    for i in range(2,n):
        if n%i==0:
            return False
    return True
print(prime(int(input())))