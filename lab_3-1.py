# Author: RTS 10/25/21
import math
import time

t0 = time.perf_counter()

math.pow(2, 2)

t1 = time.perf_counter()

speed1 = t1 - t0
print(speed1)

t2 = time.perf_counter()

2 ** 2

t3 = time.perf_counter()

speed2 = t3 - t2
print(speed2)

print(speed2 - speed1)
