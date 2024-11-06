import time
import threading
from multiprocessing import Process

def cpu_bound_task():
  count = 0
  
  # Tries to add a number for a humongous amount of time
  for i in range(10**7):
    count += i
  
  print(f'count: {count}')

# This is without multithreading
def main_default():
  start_time = time.time()

  # Run the task 4 times
  for _ in range(4):
    cpu_bound_task()

  print(f'Time elapsed: {(time.time() - start_time):.3f} seconds')

# Use multithreading
def main_multithread():
  start_time = time.time()

  threads = [threading.Thread(target=cpu_bound_task) for _ in range(4)]

  for thread in threads:
    thread.start()
  for thread in threads:
    thread.join()

  print(f'Time elapsed: {(time.time() - start_time):.3f} seconds')

# Use multiprocessing
def main_multiproc():
  start_time = time.time()
  processes = [Process(target=cpu_bound_task) for _ in range(4)]

  for process in processes:
    process.start()
  for process in processes:
    process.join()

  print(f'Time elapsed: {(time.time() - start_time):.3f} seconds')


if __name__ == '__main__':
  # main_default()
  # main_multithread()
  main_multiproc()