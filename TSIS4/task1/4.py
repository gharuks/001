import re
with open('input.txt', 'r', encoding='utf-8') as s:
    txt = s.read()
date_pattern = re.compile('\d{2}\.\d{2}\.\d{2,4} \d{2}\:\d{2}\:\d{2}')
result = date_pattern.findall(txt)
print(result)