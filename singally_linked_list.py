from os import link
from sys import stdin
from turtle import position
from types import NoneType

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
        if self.head is None:
            self.head = self.tail = newnode
            return

        temp = self.head
        self.head = newnode
        self.head.next = temp

    def insert_at_the_end(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = self.tail = newnode
            return

        self.tail.next = newnode
        self.tail = newnode

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

    def delete_from_the_beginning(self):
        if self.head is None:
            print("Linked list is empty")

        elif self.head != self.tail:
            self.head = self.head.next
            return

        self.head = self.tail = None

    def delete_from_the_end(self, length):
        if self.head is None:
            print("Linked list is empty")

        temp = self.head   
        if self.head != self.tail:
            while temp.next != self.tail:
                temp = temp.next

            self.tail = temp
            self.tail.next = None

    def delete_from_specific_position(self, length):
        if self.head is None:
            print("Linked list is empty")

        i = 1
        temp = self.head
        print("Enter the position:", end=" ")
        position = int(input())
        while i < position - 1:
            temp = temp.next
            nextnode = temp.next
            i += 1

        temp.next = nextnode.next
        nextnode = None
            
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


linked_data = LinkedList()
while True:
    print()
    print("********************MAIN MENU**********************")
    print()
    print("1. Insert at the beginning")
    print("2. Insert at the end")
    print("3. Insert at the specific position")
    print("4. Delete from the beginning")
    print("5. Delete from the end")
    print("6. Delete from the specific position")
    print("7. Reverse linked list")
    print()
    print("Enter your choice: ", end=" ")
    choice = int(input())
    while True:
        if choice in [1,2,3]:
            print("enter data for thr node:", end=" ")
            data = int(input())

            # INSERT NODE AT THE BEGINNING
            if choice == 1: linked_data.insert_at_the_beginning(data)

            # INSERT NODE AT THE END
            elif choice == 2: linked_data.insert_at_the_end(data)

            # INSERT AT SPECIFIC POSITION
            elif choice == 3: linked_data.insert_at_specific_position(linked_data, linked_data.len())

            print("want to insert more data? :", end=" ")
            make_choice = input()
            if make_choice in ["y", "Y"]: continue
            
            else:
                linked_data.display()
            
                # LENGTH OF LINKED LIST
                length = linked_data.len()
                print(f"Length of linked list: {length}")
                print()
                break

        else:
            # DELETE FROM THE BEGINNING
            if choice == 4: linked_data.delete_from_the_beginning()

            # DELETE FROM THE END
            elif choice == 5: linked_data.delete_from_the_end(linked_data.len())

            # DELETE FROM SPECIFIC POSITION
            elif choice == 6: linked_data.delete_from_specific_position(linked_data.len())
            
            # REVERSE THE LINKED LIST
            elif choice == 7: 
                linked_data.reverse()
                linked_data.display()
                break
    
            print("want to delete more data? :", end=" ")
            make_choice = input()
            if make_choice in ["y", "Y"]: continue
            else:
                linked_data.display()
            
                # LENGTH OF LINKED LIST
                length = linked_data.len()
                print(f"Length of linked list: {length}")
                print()
                break

    print("want to continue or exit(y/n): ", end=" ")
    c = input()
    if c in ["y", "Y"]: continue
    else: break
