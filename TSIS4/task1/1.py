import re
with open('raw.txt', 'r') as f:
    text = f.read()
bin_pattern = re.compile(r'\d{12}')
result = bin_pattern.findall(text)
for i in result:
    print(result(i))