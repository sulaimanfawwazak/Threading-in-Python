import threading
import time
from charminal import *

# This file contains the implementation of a basic threading: no join

def print_message(name, count):
  emoji_array = [EMOJI_BEGIN, EMOJI_ERROR, EMOJI_DEBUG]
  for i in range(count):
    print(f"{name} says: {i} {emoji_array[i]}")
    time.sleep(0.5)

def main():
  threads = []

  for i in range(5):
    thread = threading.Thread(
      target=print_message,
      args=(f'Thread-{i+1}', 3)
    )
    threads.append(thread)
    thread.start()

  for thread in threads:
    thread.join()

  print("Main thread finished!")

if __name__ == '__main__':
  main()

# OUTPUT
# Thread-1 says: 0 🚀
# Thread-2 says: 0 🚀
# Thread-3 says: 0 🚀
# Thread-4 says: 0 🚀
# Thread-5 says: 0 🚀
# Thread-1 says: 1 💥
# Thread-2 says: 1 💥
# Thread-3 says: 1 💥
# Thread-4 says: 1 💥
# Thread-5 says: 1 💥
# Thread-1 says: 2 🔔
# Thread-4 says: 2 🔔
# Thread-5 says: 2 🔔
# Thread-2 says: 2 🔔
# Thread-3 says: 2 🔔
# Main thread finished!

# Here, we try to make a for loop and for each loop we make a thread
# Once the thread is made, then we append the thread into the list of threads
# After that we start the thread
# And then, for each thread in the thread list, we join them


