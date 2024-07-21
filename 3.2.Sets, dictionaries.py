# A.Символическая выжимка

print(''.join(set(input())))

# B.Символическая разница

print(''.join(set(input()).intersection(set(input()))))

# C.Зайка — 8

objects = set()
for _ in range(int(input())):
    objects = objects.union(set(input().split()))

print('\n'.join(objects))

