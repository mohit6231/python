import threading

thread_name = threading.current_thread().getName()

if threading.current_thread() == threading.main_thread():
    for x in range(10):
        if x % 2 == 0:
            print(x)
else:
    print('The running thread is not a main thread')

print(thread_name)
