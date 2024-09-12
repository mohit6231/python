import threading

# Shared resource
counter = 0
lock = threading.Lock()


def increment_counter():
    global counter
    for _ in range(1000000):
        # Lock before modifying shared data
        lock.acquire()
        counter += 1
        # Release lock after modification
        lock.release()


# Create two threads that modify the shared resource
thread1 = threading.Thread(target=increment_counter)
thread2 = threading.Thread(target=increment_counter)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print(f"Final counter value: {counter}")
