import time

def factorize(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def process_numbers_sync(numbers):
    result = []
    for number in numbers:
        result.append(factorize(number))
    return result

if __name__ == "__main__":
    numbers_to_factorize = [36, 18, 24, 48, 64, 128, 256, 512]

    start_time = time.time()
    result_sync = process_numbers_sync(numbers_to_factorize)
    end_time = time.time()

    print(f"Synchronous result: {result_sync}")
    print(f"Synchronous execution time: {end_time - start_time} seconds")

from concurrent.futures import ProcessPoolExecutor

def process_numbers_parallel(numbers):
    result = []
    with ProcessPoolExecutor(max_workers=5) as executor:
        result = list(executor.map(factorize, numbers))
    return result

if __name__ == "__main__":
    start_time = time.time()
    result_parallel = process_numbers_parallel(numbers_to_factorize)
    end_time = time.time()

    print(f"Parallel result: {result_parallel}")
    print(f"Parallel execution time: {end_time - start_time} seconds")