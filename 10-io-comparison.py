import requests
import time
import threading

def fetch_url(url):
  response = requests.get(url)
  print(f'Fetched {url}: {len(response.content)} bytes')

def run_fetch_url_seq():
  urls = [
    'https://bostondynamics.com/',
    'https://agilityrobotics.com/',
    'https://huggingface.co/',
    'https://www.python.org'
  ]

  start_time = time.time()

  for url in urls:
    fetch_url(url)

  end_time = time.time()
  print(f'Time taken (sequential): {end_time - start_time}')

def run_fetch_url_thread():
  urls = [
    'https://bostondynamics.com/',
    'https://agilityrobotics.com/',
    'https://huggingface.co/',
    'https://www.python.org'
  ]

  start_time = time.time()

  threads = []

  for url in urls:
    thread = threading.Thread(target=fetch_url, args=(url,))
    threads.append(thread)
    thread.start()

  for thread in threads:
    thread.join()

  end_time = time.time()
  print(f'Time taken (thread): {end_time - start_time}')


if __name__ == '__main__':
  # run_fetch_url_seq()
  run_fetch_url_thread()