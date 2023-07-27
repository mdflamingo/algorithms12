# 89306121

class Deque:
    def __init__(self, length):
        self.buffer = [None] * length
        self.head = 0
        self.tail = 0
        self.max_length = length
        self.cur_length = 0

    def push_back(self, value):
        if self.cur_length != self.max_length:
            self.buffer[self.tail] = value
            self.tail = (self.tail + 1) % self.max_length
            self.cur_length += 1
        else:
            raise IndexError

    def push_front(self, value):
        if self.cur_length != self.max_length:
            self.buffer[self.head - 1] = value
            self.head = (self.head - 1) % self.max_length
            self.cur_length += 1
        else:
            raise IndexError

    def pop_front(self):
        if self.cur_length <= 0:
            raise IndexError
        result = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head = (self.head + 1) % self.max_length
        self.cur_length -= 1
        return result

    def pop_back(self):
        if self.cur_length <= 0:
            raise IndexError
        result = self.buffer[self.tail - 1]
        self.buffer[self.tail - 1] = None
        self.tail = (self.tail - 1) % self.max_length
        self.cur_length -= 1
        return result


if __name__ == '__main__':
    with open('input.txt') as input:
        num_of_commands = int(input.readline())
        deck = Deque(int(input.readline()))
        for line in range(num_of_commands):
            commands = input.readline().split()
            try:
                if commands[0] == 'push_front':
                    deck.push_front(commands[1])
                elif commands[0] == 'push_back':
                    deck.push_back(commands[1])
                elif commands[0] == 'pop_front':
                    print(deck.pop_front())
                elif commands[0] == 'pop_back':
                    print(deck.pop_back())
            except IndexError:
                print('error')
