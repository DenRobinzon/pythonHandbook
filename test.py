import itertools

height = int(input())
width = int(input())
ln = len(str(height * width))

nums = itertools.count(1)

for i in range(height * width):
    num = next(nums)
    print(f'{num:>{ln}}', end=' ')
    if num % width == 0:
        print()
