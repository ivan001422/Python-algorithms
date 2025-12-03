import time

'------------'

start = time.time()

a = []

for i in range(10000000):
    a.append(i)

end = time.time()

print(end - start)

'------------'

start = time.time() 

a = [0] * 10000000

for i in range(10000000):
    a[i] = i

end = time.time()

print(end - start)

'------------'

start = time.time()

a = [s for s in range(10000000)]

end = time.time()

print(end - start)

'------------'
