import threading
import time

# This file contains the implementation of a basic threading: no join

def print_message():
  for i in range(5):
    print("Hello from the thread!")
    time.sleep(1)

def main():
  thread = threading.Thread(target=print_message)
  thread.start()
  thread.join()
  print("Main thread finished!")

if __name__ == '__main__':
  main()

# The output:
# Hello from the thread!
# Hello from the thread!
# Hello from the thread!
# Hello from the thread!
# Hello from the thread!
# Main thread finished!

# We can see that the main thread is started
# And then it runs all the threads
# And then the main thread is executed

# main --> threads --> main