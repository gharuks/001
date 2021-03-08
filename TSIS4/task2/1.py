#Detect Floating Point Number
import re
n=int(input())
for i in range(n):
    print(bool(re.search(r"(^[-+]?\d*\.\d+$)", input())))