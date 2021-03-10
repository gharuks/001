n=int(input())
s=set()
a=[int(i) for i in input().split()]
for x in a:
    s.add(x)
#s.add(int(a) for i in input().split())
if len(s)==n:
    print("YES")
else:
    print("NO")