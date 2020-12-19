input_string = '''1 + 2 * 3 + 4 * 5 + 6'''


def evaluate(expression):
    total = 0
    next_operation = '+'
    i = 0
    while i < len(expression):
        c = expression[i]
        if c in ('+', '*'):
            next_operation = c

            if c == '*' and i < len(expression) - 2:
                to_search = i + 1
                brackets = 0

                while to_search < len(expression):
                    e = expression[to_search]
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

                    if brackets == 0:
                        break

                    to_search += 2

                if to_search < len(expression) - 1 and expression[to_search + 1] == '+':
                    expression[i + 1] = '(' + expression[i + 1]
                    expression[-1] = expression[-1] + ')'
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
