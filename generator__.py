newlist = [x for x in range(10)]
newlist1 = (x for x in range(10))
print(type(newlist))
print(type(newlist1))
print(newlist1.__next__())
print(next(newlist1))
print('@@'*20)

def generator1():
    n = 0
    while True:
        n += 1
        temp = yield n
        print('temp', temp)


g = generator1()

print(g.send(None))
print(g.send(1))

a = 2 if 4>3 else 1
print(a)

names = ['qq','wanli','tjm']
result = [name for name in names if len(name)>3 ]
print(result)
print(type(result))
wanli = {'name':'wanli','age':'18'}
print(*wanli.items())
