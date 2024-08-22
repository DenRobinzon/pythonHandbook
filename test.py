even_numbers = ''
odd_numbers = ''
eq_numbers = ''
evens = '08642'
with open(input(), 'r', encoding='UTF-8') as file_in:
    for line in file_in:
        even_line = ''
        odd_line = ''
        eq_line = ''
        for number in line.split():
            even_digits, odd_digits = 0, 0
            for digit in number:
                if digit in evens:
                    even_digits += 1
                else:
                    odd_digits += 1
            if even_digits > odd_digits:
                even_line += number + ' '
            elif even_digits < odd_digits:
                odd_line += number + ' '
            else:
                eq_line += number + ' '
        even_numbers += even_line + '\n'
        odd_numbers += odd_line + '\n'
        eq_numbers += eq_line + '\n'

with open(input(), 'w', encoding='UTF-8') as file_out:
    file_out.write(even_numbers)

with open(input(), 'w', encoding='UTF-8') as file_out:
    file_out.write(odd_numbers)

with open(input(), 'w', encoding='UTF-8') as file_out:
    file_out.write(eq_numbers)
