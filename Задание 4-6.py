from itertools import count
from math import factorial

def my_func():
    for el in count(1):
        yield factorial(el)

variable = my_func()
x = 0
for i in variable:
    if x < 10:
        print(i)
        x += 1
    else:
        break