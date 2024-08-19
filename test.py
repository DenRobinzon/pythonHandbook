with open(input(), 'r', encoding='UTF-8') as file_in:
    numbers = [int(num) for num in file_in.read().split()]

count = len(numbers)
positive = len([num for num in numbers if num > 0])
min_number = min(numbers)
max_number = max(numbers)
total_sum = sum(numbers)
average = round(total_sum / count, 2)

print(count, positive, min_number, max_number, total_sum, average, sep='\n')
