# import re
# with open('input.txt', 'r', encoding='utf-8') as s:
#     txt = s.read()
# title_pattern = re.compile('')
# cnt_attern = re.compile('')
# uprice__pattern = re.compile('')
# tprice_pattern = re.compile('')
# result = pattern.findall(txt)
# print(result)
import re
import csv
file = open('input.txt','r', encoding="utf8")
text = file.read()
BINPattern = r"\nБИН.*(?P<BIN>\b[0-9]+)"
NDSPattern = r"\nНДС.*(?P<NDS>\b[0-9]+)"
BINText = re.search(BINPattern, text).group("BIN")
NDSText = re.search(NDSPattern, text).group("NDS")
itemPatternText = r"(?P<name>.*)\n{1}(?P<count>.*)x(?P<price>.*)\n{1}(?P<total1>.*)\n{1}Стоимость\n{1}(?P<total2>.*)"
itemPattern = re.compile(itemPatternText)
items = [["БИН","НДС","Наименование товара","Кол-во","Цена за единиц","Время"]]
for m in re.finditer(itemPattern, text):
    items.append([BINText,NDSText, m.group("name").strip(),m.group("count").strip(), m.group("price").strip()])
with open('file.csv','w',newline='',encoding="utf8") as f:
    writer = csv.writer(f)
    writer.writerows(items)
for x in items:
    print(x)
file.close()