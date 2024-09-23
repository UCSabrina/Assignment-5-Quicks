import time
import random

# Deterministic Quicksort Implementation
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

# Randomized Quicksort Implementation
def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[random.randint(0, len(arr) - 1)]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return randomized_quicksort(left) + middle + randomized_quicksort(right)
    
# Helper function to time the execution of both implementations
def time_execution(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    end_time = time.time()
    return end_time - start_time

# Generate test arrays
def generate_test_arrays(size):
    return {
        'random': [random.randint(0, size) for _ in range(size)],
        'sorted': sorted([random.randint(0, size) for _ in range(size)]),
        'reverse_sorted': sorted([random.randint(0, size) for _ in range(size)], reverse=True)
    }

# Run performance analysis
def run_performance_analysis():
    sizes = [100, 1000, 5000, 10000]
    for size in sizes:
        test_arrays
