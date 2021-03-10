import re
txt=input()
word=input()
if re.search(word, txt):
    x = re.search(word, txt)
    res= "First time Polinoma occured in position: {}"
    print(res.format(x.start()))
else:
    print("Not found")