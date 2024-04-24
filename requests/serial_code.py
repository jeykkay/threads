import requests
import time


def make_get_request(url):
    response = requests.get(url)
    print(f"response from {url}: {response.status_code}")


def run(urls):
    start_time = time.time()
    for url in urls:
        make_get_request(url)
    end_time = time.time()
    print(f"total execution time: {end_time - start_time} seconds")


urls = ['https://www.google.com', 'https://www.facebook.com']
run(urls)
