import threading
import time


def number_task():
    for num in range(1, 6):
        print(f"Thread 1 - Number: {num}")
        time.sleep(1)


def alphabet_task():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(f"Thread 2 - Alphabet: {letter}")
        time.sleep(1)

def message_task():
    msg_list = ["Hello", "Welcome", "Python", "Multithreading", "Complete"]
    for text in msg_list:
        print(f"Thread 3 - Message: {text}")
        time.sleep(1)

# Create threads
thread1 = threading.Thread(target=number_task)
thread2 = threading.Thread(target=alphabet_task)
thread3 = threading.Thread(target=message_task)

# Start threads
thread1.start()
thread2.start()
thread3.start()

# Wait for all threads to finish
thread1.join()
thread2.join()
thread3.join()

print("\nAll threads have completed execution.")
