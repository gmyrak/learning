import time
from num import *

start = time.time()

p = 0
f = 0

N = 2
Delta = 1_000_000


for k in range(N, N + Delta):
    #if k % 100 == 0:
    #    print(k, '\r', end='' )
    if ferma(k):
        f += 1
        if prime(k):
            p += 1
        else:
            print('{} = {}'.format(k,  ' * '.join(map(str, factor(k)))))


print(
'''В диапазоне {} чисел Ферма, из них {} простых ({} псевдо)
Доля псевдопростых составляет: {}
'''.format(f, p, f-p, (f-p)/p))

print('\nTime: {} c'.format( round(time.time() - start, 2) ))