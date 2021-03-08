def func(str):
    t=[]
    for i in str.split('-'):
        t.append(i)
    t.sort()
    print('-'.join(t))
func(input())
