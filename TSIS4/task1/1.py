import re
with open('input.txt', 'r', encoding='utf-8') as s:
    txt = s.read()
noc_pattern = re.compile('([A-Za-z]{3,} ([A-Za-z]{3,})?)')
result = noc_pattern.findall(txt)
print(result)