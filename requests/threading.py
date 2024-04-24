import threading
import requests
import time


def make_get_request(url):
    response = requests.get(url)
    print(f"Response from {url}: {response.status_code}")


def run(urls):
    start_time = time.time()

    threads = []
    for url in urls:
        t = threading.Thread(target=make_get_request, args=(url, ))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"total execution time for threads: {execution_time} seconds")


urls = ['https://google.com', 'https://facebook.com']

run(urls)
