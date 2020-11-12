import os

dir = os.getcwd()
filename = 'test.py'
filepath = os.path.join(dir, filename)
print(os.path.split(filepath))
