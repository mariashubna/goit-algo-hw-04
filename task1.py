import random
import timeit

# Список рандломних значень
def random_list(length):
    return [random.randint(0, 1000) for _ in range(length)]

# Сортування злиття
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
   
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

# Сортування вставками
def insertion_sort(arr): 
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key 
    return arr

# Кількість чисел у масиві для сортування
num_lengths = [10, 30, 50, 80, 100, 500, 1000]

for length in num_lengths:
    arr = random_list(length)
    merge_sort_time = timeit.timeit(stmt='merge_sort(arr.copy())', globals=globals(), number=100)
    print(f"Час для сортування злиттям для кількості чисел {length}: {merge_sort_time}")
    insertion_sort_time = timeit.timeit(stmt='insertion_sort(arr.copy())', globals=globals(), number=100)
    print(f"Час для сортування вставками для кількості чисел {length}: {insertion_sort_time}")
    timsort_time = timeit.timeit(stmt='sorted(arr.copy())', globals=globals(), number=100)
    print(f"Час для сортування Timsort для кількості чисел {length}: {timsort_time}")
    print('-------------------------------------------------------------------------')



