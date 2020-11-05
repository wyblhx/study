'''
s=lambda a,b : a+b

print(s(1,2))


def func(x,y,func):
    print(x,y)
    s=func(x,y)
    print(s)
func(1,2,lambda a,b :a+b)

list1=[{'id':5,'type':1},{'id':3,'type':1},{'id':2,'type':1}]

m=max(list1,key=lambda x:x['id'])

print(m)
'''

from functools import reduce

tuple1 = (1, 2, 3)
result = reduce(lambda x, y: x + y, tuple1,10)
print(result)
