input_string = '''1 + (2 * 3) + (4 * (5 + 6))'''


def evaluate(expression):
    total = 0
    next_operation = '+'
    i = 0
    while i < len(expression):
        c = expression[i]
        if c in ('+', '*'):
            next_operation = c
            i += 1
            continue

        if c[0] == '(':
            end = i + 1
            brackets = 0
            z = 0
            while c[z] == '(':
                brackets += 1
                z += 1
            while brackets > 0:
                e = expression[end]
                if e[0] == '(':
                    z = 0
                    while e[z] == '(':
                        brackets += 1
                        z += 1
                else:
                    z = -1
                    while e[z] == ')':
                        brackets -= 1
                        z -= 1
                end += 1
            expression[i] = expression[i][1:]
            expression[end - 1] = expression[end - 1][:-1]
            c = evaluate(expression[i:end])
            i = end
        else:
            i += 1

        if next_operation == '+':
            total += int(c)
        elif next_operation == '*':
            total *= int(c)

    return total


expressions = input_string.split('\n')

total_sum = 0
for ex in expressions:
    total_sum += evaluate(ex.split())

print(total_sum)
