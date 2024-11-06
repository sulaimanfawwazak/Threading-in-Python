import threading
import time
import queue
from charminal import *

start_time = time.time()

def producer(queue):
  for i in range(5):
    item = f'item-{i}'
    print(f'{COLOR_GREEN}[{int(time.time() - start_time)}] {EMOJI_BEGIN} Producing: {item}{RESET}')
    queue.put(item)
    time.sleep(1)   # Purposedly make the sleep time faster

  queue.put(None) # Signal to consumer that production is done

def consumer(queue):
  while True:
    item = queue.get()
    if item is None:
      break
    print(f'{COLOR_RED}[{int(time.time() - start_time)}] {EMOJI_ERROR} Consuming: {item}{RESET}')
    time.sleep(2) # Purposedly make the sleep time slower

def main():
  q = queue.Queue()

  producer_thread = threading.Thread(target=producer, args=(q,))
  consumer_thread = threading.Thread(target=consumer, args=(q,))

  producer_thread.start()
  consumer_thread.start()

  producer_thread.join()
  consumer_thread.join()

if __name__ == '__main__':
  main()


# OUTPUT:
# [0] 🚀 Producing: item-0
# [0] 💥 Consuming: item-0
# [1] 🚀 Producing: item-1
# [2] 🚀 Producing: item-2
# [2] 💥 Consuming: item-1
# [3] 🚀 Producing: item-3
# [4] 🚀 Producing: item-4
# [4] 💥 Consuming: item-2
# [6] 💥 Consuming: item-3
# [8] 💥 Consuming: item-4

# We can see that the `producer` and `consumer` thread run in different speed
# The `consumer` uses the information (`item`) from `producer`
# Since both of them are in different thread, then we can use queue to pass the information