import time
import threading

start_time = time.time()

def worker(event):
  print(f'[t={int(time.time() - start_time)}] Worker is waiting for event to start (in 3 seconds)')
  
  event.wait() # Wait until the event is set

  print(f'[t={int(time.time() - start_time)}] Worker is starting to work')

  for _ in range(5):
    print(f'[t={int(time.time() - start_time)}] Working...')
    time.sleep(1)
  print(f'[t={int(time.time() - start_time)}] Worker is finished')

def main():
  event = threading.Event()
  
  thread = threading.Thread(target=worker, args=(event,)) # Pass the event as the argument to the target fn
  thread.start()

  time.sleep(3)

  print(f'[t={int(time.time() - start_time)}] Main thread sets the event')
  event.set()
  thread.join()

  print(f'[t={int(time.time() - start_time)}] Main thread is finished')

if __name__ == '__main__':
  main()

# OUTPUT:
# [t=0] Worker is waiting for event to start (in 3 seconds)
# [t=3] Main thread sets the event
# [t=3] Worker is starting to work
# [t=3] Working...
# [t=4] Working...
# [t=5] Working...
# [t=6] Working...
# [t=7] Working...
# [t=8] Worker is finished
# [t=8] Main thread is finished