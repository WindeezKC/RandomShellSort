import random
import time

def knuth_shell_sort(a):
    n = len(a)
    h = 1
    while h < n // 3:
        h = 3 * h + 1

    while h >= 1:
        for i in range(h, n):
            temp = a[i]
            j = i
            while j >= h and a[j - h] > temp:
                a[j] = a[j - h]
                j -= h
            a[j] = temp
        h //= 3

def read_numbers_from_file(file_path):
    with open(file_path, 'r') as file:
        return [int(line.strip()) for line in file if line.strip().isdigit()]

file_path = 'random_numbers12.txt'
arr = read_numbers_from_file(file_path)

start_time = time.time()
knuth_shell_sort(arr)
end_time = time.time()

sorting_time_ms = (end_time - start_time) * 1000
print(f"Sorting time: {sorting_time_ms:.3f} milliseconds")
