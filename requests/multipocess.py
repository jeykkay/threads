import requests
import time
from multiprocessing import Process


def make_get_request(url):
    response = requests.get(url)
    print(f"Response from {url}: {response.status_code}")


def run(urls):
    start_time = time.time()

    processes = []
    for url in urls:
        p = Process(target=make_get_request, args=(url, ))
        processes.append(p)
        p.start()

    for process in processes:
        process.join()

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Total execution time for processes: {execution_time} seconds")


urls = ["https://www.google.com", "https://www.facebook.com"]

run(urls)
