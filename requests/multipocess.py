from multiprocessing import Process
import time
import os
import requests

cpu = os.cpu_count()
urls = ["https://www.google.com", "https://www.facebook.com"]


def make_get_request():
    for url in urls:
        response = requests.get(url)
        print(f"Response from {url}: {response.status_code}")


def run():
    start_time = time.time()

    processes = [Process(target=make_get_request) for _ in range(cpu)]
    for process in processes:
        process.start()
    for process in processes:
        process.join()

    end_time = time.time()
    time_delta = end_time - start_time
    print(f"Time: {time_delta} seconds")


if __name__ == "__main__":
    run()
