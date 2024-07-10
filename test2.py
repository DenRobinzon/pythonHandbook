n = int(input())
c = n
k = 1
while True:
    if c <= k:
        break
    c -= k
    k += 1
print(c, k)