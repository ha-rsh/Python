import queue                                           

def main():
    q = queue.Queue()                                  

    for i in range(0, 10, 2):
        q.put(i)                                       

    while not q.empty():
        print("Removed item from queue:", end=' ')
        print(q.get())                                 


if __name__ == "__main__":
    main()             