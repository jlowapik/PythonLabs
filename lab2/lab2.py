def calc(data):
    def operation(op, x, y):
        operators = {
            'sum': x + y,
            'dif': x - y,
            'mul': x * y,
            'div': x / y
        }
        return operators[op]

    operators = {
        '+': 'sum',
        '-': 'dif',
        '*': 'mul',
        '/': 'div'
    }

    operator = ''
    for i in data:
        if i in operators:
            operator = i
    data = data.split(operator)
    return operation(operators[operator], int(data[0]), int(data[1]))

print(calc('9/3'))
print(calc('8    + 3'))
data = input('---')
print(calc(data))