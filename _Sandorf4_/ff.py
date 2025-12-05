import random
import os
import time


x = [1,3,2,2,1,1,1]

y=random.randint(1,8)/100

while y<1:
    print(x)
    print('         |')
    time.sleep(y)
    os.system('cls')
    z = x[0]
    x.pop(0)
    x.append(z)
    y = y*1.2
print('выпало',x[3])
input()
