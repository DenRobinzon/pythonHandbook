rle = [('a', 2), ('b', 3), ('c', 1)]
res = ''.join(char * number for char, number in rle)
print(res)