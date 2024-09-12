from threading import Thread
import threading


def evenNumber():
    for x in range(20):
        if x % 2 == 0:
            print(x)
    thread_name = threading.current_thread().getName()
    print(thread_name)


def oddNumber():
    for x in range(20):
        if x % 2 != 0:
            print(x)
    thread_name = threading.current_thread().getName()
    print(thread_name)


def even_odd():
    evenNumber()
    oddNumber()
    thread_name = threading.current_thread().getName()
    print(thread_name)


thread_name = threading.current_thread().getName()
print(thread_name)
t = Thread(target=evenNumber)
# t.start()

t = Thread(target=even_odd)
t.start()
