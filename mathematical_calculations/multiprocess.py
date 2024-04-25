from multiprocessing import Process
import time
import os


cpu = os.cpu_count()


def math_function():
    result = 0
    for i in range(100000):
        result = abs(1/2 ** 3) + (i / (1/3))
    print(f"Result {result}")


def run_process():
    start = time.time()

    processes = [Process(target=math_function) for i in range(cpu)]
    for process in processes:
        process.start()
    for process in processes:
        process.join()

    end = time.time()
    time_delta = end - start
    print(f'Time {time_delta}')


if __name__ == '__main__':
    run_process()
