input_data = input().split()
numbers = []

for i in input_data:
    if i.lstrip('-').isdigit():
        numbers.append(int(i))
    else:
        match i:
            case '*':
                numbers.append(numbers.pop() * numbers.pop())
            case '-':
                numbers.append(numbers.pop(-2) - numbers.pop())
            case '+':
                numbers.append(numbers.pop() + numbers.pop())
            case '/':
                numbers.append(numbers.pop(-2) // numbers.pop())
            case '~':
                numbers[-1] = -numbers[-1]
            case '!':
                number = numbers[-1]
                factorial = 1
                for j in range(2, number + 1):
                    factorial *= j
                numbers[-1] = factorial
            case '#':
                numbers.append(numbers[-1])
            case '@':
                numbers[-3], numbers[-2], numbers[-1] = numbers[-2], numbers[-1], numbers[-3]

print(numbers[0])
