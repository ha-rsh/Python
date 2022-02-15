import queue

q = queue.PriorityQueue(maxsize=10)

for i in [10, 50, 16, 8, 15, 30, 20]:
    q.put(i)
while not q.empty():
    for i in ('First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth', 'Seventh'):
        print(f"{i} Priority:-", end=' ')
        print(q.get())