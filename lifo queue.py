import queue                                         #queue module is imported


def main():                                          #main function
    q = queue.LifoQueue(maxsize=5)                   #LifoQueue created with maximum size of 10
    print("Queue size:", q.qsize())

    for i in range(0, 10, 2):
        print("Full:", q.full())                     #To check queue is full or not
        q.put(i)                                     #put element into the queue
    print("Queue size:", q.qsize())                  #chech the size of the queue
    print("Full:", q.full())

    while not q.empty():                             # check if queue is empty
        print("Removed item from queue:", end=' ')
        print(q.get())                               #reterievr element from the queue
        print("Empty:", q.empty())
    print("Queue size:", q.qsize())


if __name__ == "__main__":
    main()                                           #main function called