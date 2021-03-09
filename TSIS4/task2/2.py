#Re.split()
import re
regex_pattern = r"[,.]"
s=str(input())
print("\n".join(re.split(regex_pattern, s)))
