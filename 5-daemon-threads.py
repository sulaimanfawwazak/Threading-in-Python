import threading
import time

counter = 0

def infinite_task():
  start_time = time.time()
  while True:
    print(f'[t={int(time.time() - start_time)}] Running...')
    time.sleep(1)

def main():
  occur_time = 5 # How long the main thread will be run (seconds)
  print(f'Occuring time: {occur_time}')
  daemon_thread = threading.Thread(target=infinite_task)
  daemon_thread.daemon = True
  daemon_thread.start()
  time.sleep(occur_time) # This what "defines" the main thread

  print(f'Main thread is finished!')

if __name__ == '__main__':
  main()

# OUTPUT:
# Occuring time: 5
# [t=0] Running...
# [t=1] Running...
# [t=2] Running...
# [t=3] Running...
# [t=4] Running...
# Main thread is finished!
# [t=5] Running...
