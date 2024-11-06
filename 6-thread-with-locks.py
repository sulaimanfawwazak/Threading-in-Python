import threading
import time

counter = 0
counter_lock = threading.Lock()

def increment():
  global counter
  with counter_lock:
    for i in range(10):
      print(f'i: {i}')
      counter += 1

def main():
  global counter
  threads = []

  for i in range(3):
    thread = threading.Thread(target=increment)
    threads.append(thread)
    thread.start()

  for thread in threads:
    thread.join()

  print(f'Main thread is finished!')

if __name__ == '__main__':
  main()

# OUTPUT:
# i: 0
# i: 1
# i: 2
# i: 3
# i: 4
# i: 5
# i: 6
# i: 7
# i: 8
# i: 9
# i: 0
# i: 1
# i: 2
# i: 3
# i: 4
# i: 5
# i: 6
# i: 7
# i: 8
# i: 9
# i: 0
# i: 1
# i: 2
# i: 3
# i: 4
# i: 5
# i: 6
# i: 7
# i: 8
# i: 9
# Main thread is finished!