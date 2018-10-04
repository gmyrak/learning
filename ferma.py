import time
from num import *
'Вывод псевдопростых ферма'

start = time.time()

p = 0
f = 0

N = 1_000_000
Delta = 2_000_000


for k in range(N, N + Delta):
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

print('\nTime: {} c'.format( round(time.time() - start, 3) ))