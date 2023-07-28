# 89306121
from exceptions import EmptyDequeError, DequeOverflowError


class Deque:
    def __init__(self, length):
        self._buffer = [None] * length
        self._head = 0
        self._tail = 0
        self._max_length = length
        self._cur_length = 0

    def push_back(self, value):
        if self._cur_length == self._max_length:
            raise DequeOverflowError
        self._buffer[self._tail] = value
        self._tail = (self._tail + 1) % self._max_length
        self._cur_length += 1

    def push_front(self, value):
        if self._cur_length == self._max_length:
            raise DequeOverflowError
        self._buffer[self._head - 1] = value
        self._head = (self._head - 1) % self._max_length
        self._cur_length += 1

    def pop_front(self):
        if self._cur_length <= 0:
            raise EmptyDequeError
        result = self._buffer[self._head]
        self._buffer[self._head] = None
        self._head = (self._head + 1) % self._max_length
        self._cur_length -= 1
        return result

    def pop_back(self):
        if self._cur_length <= 0:
            raise EmptyDequeError
        result = self._buffer[self._tail - 1]
        self._buffer[self._tail - 1] = None
        self._tail = (self._tail - 1) % self._max_length
        self._cur_length -= 1
        return result


if __name__ == '__main__':
    with open('input.txt') as input:
        num_of_commands = int(input.readline())
        deque = Deque(int(input.readline()))
        for line in range(num_of_commands):
            commands = input.readline().split()
            try:
                if commands[0] == 'push_front':
                    deque.push_front(commands[1])
                elif commands[0] == 'push_back':
                    deque.push_back(commands[1])
                elif commands[0] == 'pop_front':
                    print(deque.pop_front())
                elif commands[0] == 'pop_back':
                    print(deque.pop_back())
            except DequeOverflowError:
                print('error')
            except EmptyDequeError:
                print('error')

