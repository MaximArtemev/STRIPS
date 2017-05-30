"""
from threading import Lock, Thread
import time

lock = Lock()
queue = [1, 2, 3]


class Wait(Thread):
    def run(self):
        global queue
        try:
            while True:
                lock.acquire()
                print('aquered')
                a = queue.pop()
                print(a)
                lock.release()
                print('released')
        except:
            print("lish empty")


class Trigger(Thread):
    global queue
    lock.acquire()
    print('aquered 111')
    queue.append(10)
    lock.release()
    time.sleep(1)
    lock.acquire()
    print('aquered 111')

    queue.append(20)
    lock.release()


Trigger().start()
Wait().start()
"""