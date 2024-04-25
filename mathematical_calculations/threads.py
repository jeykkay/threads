import threading
import time
import os


cpu = os.cpu_count()


def solve_math_problem1():
    result = 0
    for i in range(1000000):
        result += abs(round(i ** 2 / 20) + i * 2.5)
    print(f"{result}")


def run():
    start_time = time.time()

    threads = [threading.Thread(target=solve_math_problem1) for _ in range(cpu)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"Total time: {end_time - start_time}")


if __name__ == "__main__":
    run()
