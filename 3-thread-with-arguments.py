import threading
import time

# This file contains the implementation of a basic threading: no join

def print_message(name, count):
  for i in range(count):
    print(f"{name} says: {i}")
    time.sleep(0.5)

def main():
  thread = threading.Thread(
    target=print_message,
    args=('Fawwaz', 5)
  )
  thread.start()
  thread.join()
  print("Main thread finished!")

if __name__ == '__main__':
  main()

# The output:
# Fawwaz says: 0
# Fawwaz says: 1
# Fawwaz says: 2
# Fawwaz says: 3
# Fawwaz says: 4
# Main thread finished!

# This is the same as thread with join, but now we can specify the arguments
# Note that the arguments are represented in position arguments
# We can't specify it using keyword arguments