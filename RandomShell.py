import random
import time

def randomized_shell_sort(a):
    n = len(a)
    # Initial gap using a larger starting point with a random factor
    gap = n // random.randint(2, 3)
    gaps = []

    # Generate gaps using a diminishing factor that decreases
    while gap > 1:
        gaps.append(gap)
        # Randomly decide the next gap reduction within a range
        gap = int(gap // random.uniform(1.5, 2.5))

    #  ensure even small arrays are sorted well
    if gap < 1 and not gaps or gaps[-1] > 1:
        gaps.append(1)

    # Sorting using the generated gaps
    for gap in gaps:
        for i in range(gap, n):
            temp = a[i]
            j = i
            while j >= gap and a[j - gap] > temp:
                a[j] = a[j - gap]
                j -= gap
            a[j] = temp

def read_numbers_from_file(file_path):
    with open(file_path, 'r') as file:
        return [int(line.strip()) for line in file if line.strip().isdigit()]

file_path = 'random_numbers12.txt'
arr = read_numbers_from_file(file_path)

start_time = time.time()
randomized_shell_sort(arr)
end_time = time.time()

sorting_time_ms = (end_time - start_time) * 1000
print(f"Sorting time: {sorting_time_ms:.3f} milliseconds")
#print(arr)