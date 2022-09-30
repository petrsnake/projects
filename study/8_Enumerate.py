# enumerate()
# enumerate() vytvoří ze sekvence iterátor

from os import wait
from time import time


testlist = ['první', 'druhy', 'treti', 'ctvrty']
testenumerate = list(enumerate(testlist, 10))
print(testenumerate)

# objekt enumerate nemá "tvar", musíme mu ho dát např. list()

# enumerate a iterace
testenumerate = enumerate(testlist, 10)
A = next(testenumerate)
print(A)
A = next(testenumerate)
print(A)

# příklad jak například list není iterátor
# testlist = ['jedna', 'dva', 'tri', 'ctyri']
# B = next(testlist)
# print(B)
# B = next(testlist)
# print(B)

# enumerate list
for i,j in enumerate(testlist):
    print(i,j)

# enumerate tuple
fruits = [(15,'fifteen'), (12, 'twelve'), (19, 'nineteen')]
for i,j in enumerate(fruits):
    print(i,j)

# čistý výstup u tuple
fruits = [(15,'fifteen'), (12, 'twelve'), (19, 'nineteen')]
for i,(price,name) in enumerate(fruits):
    print(f'index {i}, price {price} name {name}')

# enumerate string
teststring = 'toto je test enumerate'
for i,j in enumerate(teststring):
    print(i,j)

# enumerate dictionary
# nelze, není sequence. Můžeme například:
d = {'a':1, 'b':2, 'c':3}  
for i,j in d.items():
    print(i,j)




