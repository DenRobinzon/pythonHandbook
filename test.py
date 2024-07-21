objects = set()
for _ in range(int(input())):
    objects = objects.union(set(input().split()))

print('\n'.join(objects))
