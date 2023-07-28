# 89299543
import re


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def calculate(sequence):
    operations = {
        '+': lambda num_1, num_2: num_2 + num_1,
        '-': lambda num_1, num_2: num_2 - num_1,
        '*': lambda num_1, num_2: num_2 * num_1,
        '/': lambda num_1, num_2: num_2 // num_1
    }

    stack = Stack()

    for el in sequence.split():
        if re.search('[0-9]+', el):
            stack.push(int(el))
        else:
            stack.push(operations[el](stack.pop(), stack.pop()))
    return stack.pop()


if __name__ == '__main__':
    sequence = input()
    print(calculate(sequence))
