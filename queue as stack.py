import queue


class Queue_as_stack:

    def __init__(self):

        self.q1 = queue.Queue(maxsize=10)
        self.q2 = queue.Queue(maxsize=10)
        self.stack_size = 0

    def push(self, x):
        self.stack_size += 1
        self.q2.put(x)

        while not self.q1.empty():
            self.q2.put(self.q1.queue[0])
            self.q1.get()

        self.temp = self.q1
        self.q1 = self.q2
        self.q2 = self.temp

    def pop(self):
        if self.q1.empty():
            return
        self.q1.get()
        self.stack_size -= 1

    def top(self):
        if self.q1.empty():
            return -1
        return self.q1.queue[0]

    def size(self):
        return self.stack_size


def main():
    no_ele = int(input("How many elements you want to push in stack:"))
    if no_ele > 10:
        case = False

    else:
        s = Queue_as_stack()
        for i in range(no_ele):
            take_input = input(f"Enter the {i} element to be pushed:")
            s.push(take_input)

        print("Stack size: ", s.size())
        for i in range(no_ele):
            print(s.top())
            s.pop()

        print("Stack size: ", s.size())
        case = True
    return case


if __name__ == '__main__':
    while True:
        a = main()
        if a == False:
            print('Sorry maximum size of stack is 10..')

        choice = input("Want to continue(y/n):")
        if choice.lower() == 'y':
            continue
        else:
            break