import threading
import time

# Define a function to be run in a separate thread


def print_numbers():
    for i in range(5):
        print(f"Number: {i}")
        time.sleep(1)


# Create two threads targeting the same function
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_numbers)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish execution
thread1.join()
thread2.join()

print("Both threads have finished execution")
