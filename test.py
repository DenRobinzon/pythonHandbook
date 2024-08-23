sum_result = 0

with open('numbers.num', 'rb') as file_in:
    while (number := int.from_bytes(file_in.read(2))):
        sum_result += number

print(sum_result % 65536)

