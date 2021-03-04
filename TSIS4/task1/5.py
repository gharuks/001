import re
with open('input.txt', 'r', encoding='utf-8') as s:
    txt = s.read()
address_pattern = re.compile('^[а-яА-Я0-9,\.\s]+$')
result = address_pattern.findall(txt)
print(result)