import threading
import time

# Subclass the Thread class


class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            print(f"Thread is printing: {i}")
            time.sleep(1)


# Create an instance of MyThread
thread = MyThread()

# Start the thread
thread.start()

# Wait for the thread to finish
thread.join()

print("MyThread has finished execution")
