import time

def exchange(a, i, j):
    a[i], a[j] = a[j], a[i]

def compare_exchange(a, i, j):
    if 0 <= i < len(a) and 0 <= j < len(a):
        if (i < j and a[i] > a[j]) or (i > j and a[i] < a[j]):
            exchange(a, i, j)

def shell_sort(a):
    n = len(a)
    gap = n // 2  # Start with a large enough gap and reduce it by half each time
    while gap > 0:
        for i in range(gap, n):
            temp = a[i]
            j = i
            while j >= gap and a[j - gap] > temp:
                a[j] = a[j - gap]
                j -= gap
            a[j] = temp
        gap //= 2  # Reduce the gap by half for the next step

def read_numbers_from_file(file_path):
    with open(file_path, 'r') as file:
        return [int(line.strip()) for line in file if line.strip().isdigit()]

file_path = 'random_numbers12.txt'
arr = read_numbers_from_file(file_path)

start_time = time.time()
shell_sort(arr)
end_time = time.time()

sorting_time_ms = (end_time - start_time) * 1000
print(f"Sorting time: {sorting_time_ms:.3f} milliseconds")
#print("Sorted array:", arr)
