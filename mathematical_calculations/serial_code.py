import time


def complex_calculation(data):
    result = 0
    for number in range(1000000):
        result += data ** (1/2) + data ** (1/3)
    return result


start_time = time.time()
result = complex_calculation(5)
end_time = time.time()
execution_time = end_time - start_time
print(f"Result: {result}")
print(f"Execution time of program: {execution_time} seconds")
