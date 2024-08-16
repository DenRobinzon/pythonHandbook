import itertools

expression = input()

variables = sorted({var for var in expression.split() if var.isupper()})

print(*variables, 'F')

for values in itertools.product((0, 1), repeat=len(variables)):
    print(*values, int(eval(expression, dict(zip(variables, values)))))
