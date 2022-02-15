import threading
import queue
import time

def add_items(q, items):
    for x in range(items):
        q.put(x)
        print(f"Adding item: {x} Time:{time.strftime('%H:%M:%S')}")
        time.sleep(1)
        print(f"add_items - queue size: {q.qsize()} Remaining tasks: {q.unfinished_tasks}\n")
        print(f"Added item:{x} Time:{time.strftime('%H:%M:%S')}")
        print("\n")


def process_items(q):
    while True:
        '''
             Blocking get, no parameter provided 
             so, block = True
             timeout = None
         '''
        x = q.get()
        # Processing happens here
        print(f"Processing item: {x} Time:{time.strftime('%H:%M:%S')}")
        # simulate processing time. Much slower than insertion
        time.sleep(1)
        q.task_done()
        print(f"process_items - queue size: {q.qsize()}	Remaining tasks: {q.unfinished_tasks}\n")
        print(f"Item processed:{x}	Time:{time.strftime('%H:%M:%S')}")


def main():
    test_queue = queue.Queue(5)

    # insertion thread
    add = threading.Thread(target=add_items, args=(test_queue, 10), name="add_items_thread")
    add.start()

    # processing thread (new)
    process = threading.Thread(target=process_items, args=(test_queue,), name="process_items_thread")
    process.start()

    '''     Blocks until all items in the Queue have been gotten and processed.
            The count of unfinished tasks goes up whenever an item is added to the
            queue. The count goes down whenever a consumer thread calls task_done()
            to indicate the item was retrieved and all work on it is complete.
            When the count of unfinished tasks drops to zero, join() unblocks.
    '''
    add.join()
    process.join()


if __name__ == "__main__":
    main()