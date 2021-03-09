import re
with open('input.txt', 'r', encoding='utf-8') as s:
    txt = s.read()
# bin_pattern = re.compile('\d{12}')
bin_pattern = r"\nБИН.*(?P<BIN>\b[0-9]+)"
result = bin_pattern.findall(txt)
print(result)