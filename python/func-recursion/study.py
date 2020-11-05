'''
def sum(n):
    if n==0:
        return 0
    else:
        return n+sum(n-1)
print(sum(3))
'''

'''
def f1(n):
    if n > 0:
        print(n)
        f1(n - 1)


f1(5)
'''
def f1(n):
    if n>0:
        return n+f1(n-1)
    else:
        return 0
print(f1(5))