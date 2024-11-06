from concurrent.futures import ThreadPoolExecutor
from charminal import *
import time
import threading

start_time = time.time()

def task(n):
  print(f'{EMOJI_CHAT} Task {n} is being handled by {threading.current_thread().name}')
  print(f'{COLOR_GREEN}{EMOJI_BEGIN} [{int(time.time() - start_time)}] Task {n} is starting{RESET}')
  time.sleep(n)
  print(f'{COLOR_RED}{EMOJI_ERROR} [{int(time.time() - start_time)}] Task {n} is complete{RESET}')
  
  return n*n

def main():
  with ThreadPoolExecutor(max_workers=3) as executor: # Create 3 threads
    results = executor.map(task, range(1, 6)) # 1st arg: function name; 2nd-...th arg: functions argument

  print(f'Results: {list(results)}')
  print(f'Main thread is finished')

if __name__ == '__main__':
  main()

# OUTPUT:
# 💬 Task 1 is being handled by ThreadPoolExecutor-0_0
# 🚀 [0] Task 1 is starting
# 💬 Task 2 is being handled by ThreadPoolExecutor-0_1
# 🚀 [0] Task 2 is starting
# 💬 Task 3 is being handled by ThreadPoolExecutor-0_2
# 🚀 [0] Task 3 is starting
# 💥 [1] Task 1 is complete
# 💬 Task 4 is being handled by ThreadPoolExecutor-0_0
# 🚀 [1] Task 4 is starting
# 💥 [2] Task 2 is complete
# 💬 Task 5 is being handled by ThreadPoolExecutor-0_1
# 🚀 [2] Task 5 is starting
# 💥 [3] Task 3 is complete
# 💥 [5] Task 4 is complete
# 💥 [7] Task 5 is complete
# Results: [1, 4, 9, 16, 25]
# Main thread is finished