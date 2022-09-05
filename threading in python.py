import threading
import time
from threading import Thread

def test1():
    time.sleep(0.2)
    print("function 1")


def test2():
    time.sleep(0.1)
    print("function 2")

def test3():
    time.sleep(0.5)
    print("function 3")


def test4():
    time.sleep(0.4)
    print("function 4")
    return "ewee"


class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None
    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args,
                                                **self._kwargs)
    def join(self, *args):
        Thread.join(self, *args)
        return self._return

t1 = threading.Thread(target=test1)
t2 = threading.Thread(target=test2)
t3 = threading.Thread(target=test3)
t4 = ThreadWithReturnValue(target=test4)


t1.start()
t2.start()
t3.start()
t4.start()
start = time.time()
t1.join()
t2.join()
t3.join()
z = t4.join()
end = time.time()
print(z)
print(end-start)