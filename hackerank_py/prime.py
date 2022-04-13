# def prime(x):
#     x = x + 1
#     primes = []
#     for a in range(1, 10000):
#         for b in range(2, a):
#             if a % b == 0:
#                 break
#             else:
#                 primes.append(a)
#         if len(primes) == x:
#             print(primes[1:])
#
# prime(5)

primegen = [1] * 10000
prime = []

for i in range(2, 10000):
    if primegen[i] == 1:
        for j in range(i, 10000, i):
            primegen[j] = 0
        prime.append(i)
print(prime)