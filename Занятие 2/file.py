import time

start_time = time.time()

suma = 0
for i in range(10_000_000):
    suma = suma + i

print(suma)

print(time.time()-start_time)