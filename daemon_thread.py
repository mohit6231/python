import time

import threading


def background_task():
    while True:
        print("Background task running...")
        time.sleep(2)


# Create a daemon thread
daemon_thread = threading.Thread(target=background_task, daemon=True)

# Start the daemon thread
daemon_thread.start()

# Main thread sleeps for 5 seconds and then exits
time.sleep(5)
print("Main thread exiting, background task will stop.")
