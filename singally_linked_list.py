from sys import stdin
from tkinter import N

from soupsieve import select

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return "Create node"


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insert_at_the_beginning(self, data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    def insert_at_the_end(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = newnode

    def insert_at_specific_position(self, data, length):
        temp = self.head
        i = 1
        print("Enter the position: ", end=" ")
        position = int(input())
        if position < 0 or position > length:
            print("Invalid position")

        while i < position - 1:
            i += 1
            temp = temp.next

        newnode = Node(data)
        newnode.next = temp.next
        temp.next = newnode


    def len(self):
        temp = self.head
        count = 0
        while temp.next != None:
            count += 1
            temp = temp.next

        return count + 1

    def reverse(self):
        prevnode = None
        currentnode = self.head
        while currentnode is not None:
            nextnode = currentnode.next
            currentnode.next = prevnode
            prevnode = currentnode
            currentnode = nextnode

        self.head = prevnode

    def display(self):
        temp = self.head
        elements = []
        if temp is None:
            print("Linked list empty")

        while temp:
            elements.append(temp.data)
            elements.append(" --> ")
            temp = temp.next

        elements.append(None)
        print("Linked list is as follows: ", *elements)


insert_data = LinkedList()
while True:
    print()
    print("********************MAIN MENU**********************")
    print()
    print("1. Insert at the beginning")
    print("2. Insert at the end")
    print("3. Insert at the specific position")
    print("4. Reverse linked list")
    print()
    print("Enter your choice: ", end=" ")
    choice = int(input())
    while True:
        if choice in [1,2,3]:
            print("enter data for thr node:", end=" ")
            data = int(input())

            # INSERT NODE AT THE BEGINNING
            if choice == 1: insert_data.insert_at_the_beginning(data)

            # INSERT NODE AT THE END
            elif choice == 2: insert_data.insert_at_the_end(data)

            # INSERT AT SPECIFIC POSITION
            elif choice == 3: insert_data.insert_at_specific_position(data, insert_data.len())

            print("want to insert more data? :", end=" ")
            make_choice = input()
            if make_choice in ["y", "Y"]: continue
            
            else:
                insert_data.display()
            
                # LENGTH OF LINKED LIST
                length = insert_data.len()
                print(f"Length of linked list: {length}")
                print()
                break

        else:
            insert_data.reverse()
            insert_data.display()
            print()
            break
        
    print("want to continue or exit(y/n): ", end=" ")
    c = input()
    if c in ["y", "Y"]: continue
    else: break
