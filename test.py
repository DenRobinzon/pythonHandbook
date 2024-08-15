import itertools

slices = int(input())

options = itertools.combinations_with_replacement('АБВ', slices - 3)

print('А Б В')

for option in sorted(options, reverse=True):
    print(f'{option.count('А') + 1} {option.count('Б') + 1} {option.count('В') + 1}')