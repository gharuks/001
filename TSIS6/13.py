#function that prints out the first n rows of Pascal's triangle
def pasctr(n):
    k=[0]
    s=[1]
    for i in range(1,n+1):
        print(s)
        s=[a+b for a,b in zip(s+k, k+s)]
pasctr(int(input()))
# def tri(x):
#     old = [1]
#     for x in range(1, x + 1):
#         new = [1]*x
#         for i, each in enumerate(old):
#              if i > 0:
#                 new[i] = old[i] + old[i-1]
#         print(new)
#         old = new.copy()
  
# inp = int(input('Number of lines to caculate : '))
# tri(inp)
