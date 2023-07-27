# 89299543
import re


def calculate(sequence):
    stack = []
    for el in sequence:
        if re.search('[0-9]+', el):
            stack.append(int(el))
        else:
            num_1 = stack.pop()
            num_2 = stack.pop()
            if el == '+':
                stack.append(num_2 + num_1)
            elif el == '-':
                stack.append(num_2 - num_1)
            elif el == '*':
                stack.append(num_2 * num_1)
            elif el == '/':
                stack.append(num_2 // num_1)

    return stack.pop()


if __name__ == '__main__':
    sequence = input().split()
    print(calculate(sequence))
