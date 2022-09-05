from sys import stdin

class Stack_node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.root = None

    def isempty(self):
        return True if self.root is None else False

    def push(self, data):
        newnode = Stack_node(data)
        newnode.next = self.root
        self.root = newnode

    def pop(self):
        if self.isempty(): return float('-inf')
        temp = self.root
        self.root = self.root.next
        return temp.data

    def peek(self):
        if self.isempty(): return float('-inf')
        return self.root.data

op = Stack()
while True:
    print()
    print("********************MAIN MENU**********************")
    print()
    print("1. PUSH")
    print("2. POP")
    print("3. PEEK")
    print("4. ISEMPTY")
    print()
    while True:
        print("Enter your choice: ", end=" ")
        choice = int(input())
        if choice == 1: 
            while True:
                print("enter data for thr node:", end=" ")
                data = int(input())
                op.push(data)
                print("want to push more data(y/n)?: ", end=" ")
                make_choice = input()
                if make_choice in ["y", "Y"]: continue
                else: break

        elif choice == 2: 
            while True:
                ele = op.pop()
                print(f"popped data is: {ele}")
                print("want to pop more data(y/n)?: ", end=" ")
                make_choice = input()
                if make_choice in ["y", "Y"]: continue
                else:break

        elif choice == 3: 
            while True:
                op.peek()
                print(f"data at the top of the stack:  {ele}")
                print("want to peek more data(y/n)?: ", end=" ")
                make_choice = input()
                if make_choice in ["y", "Y"]: continue
                else:break

        elif choice == 4: 
            print(op.isempty())
        
        else: 
            print("Invalid choice")
        
        print("want to continue or exit(y/n): ", end=" ")
        c = input()
        if c in ["y", "Y"]: continue
        else: break