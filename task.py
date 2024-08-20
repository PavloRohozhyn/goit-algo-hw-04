""" Task """

import timeit
import random


def merge_sort(arr):
    """ Merge Sort """

    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def insertion_sort(arr):
    """ # Insertion Sort """

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def measure_time(sort_func, arr):
    """ time handler """

    start_time = timeit.default_timer()
    sort_func(arr)
    return timeit.default_timer() - start_time


# Dataset
sizes = [1000, 5000, 10000, 50000]
results = []
# generate randome array
for size in sizes:
    arr = random.sample(range(size * 2), size)
    # timing for Mergesoft
    arr_copy = arr.copy()
    merge_time = measure_time(merge_sort, arr_copy)
    # timing for Insertion
    arr_copy = arr.copy()
    insertion_time = measure_time(insertion_sort, arr_copy)
    # timing for Timsort
    arr_copy = arr.copy()
    timsort_time = measure_time(sorted, arr_copy)
    results.append((size, merge_time, insertion_time, timsort_time))

# show result
print(f"{'Size':<10}{'Merge Sort':<15}{'Insertion Sort':<15}{'Timsort':<15}")
for size, merge_time, insertion_time, timsort_time in results:
    print(f"{size:<10}{merge_time:<15.6f}{insertion_time:<15.6f}{timsort_time:<15.6f}")
