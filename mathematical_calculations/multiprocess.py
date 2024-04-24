from multiprocessing import Process, cpu_count
import time


def complex_calculation(data):
    result = 0
    for i in range(1000000):
        result += data ** (1/2) + data ** (1/3)
    print(f"Result: {result}")


def run_process_calculation(data):
    processes = []
    for i in range(cpu_count()):
        process = Process(target=complex_calculation, args=(data, ))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()


if __name__ == '__main__':
    start_time = time.time()
    data = 5
    run_process_calculation(data)
    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time of program:", execution_time, "seconds")
