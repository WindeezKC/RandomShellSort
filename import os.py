import os

def shell_sort(arr):
    n = len(arr)

    # Generate Knuth's Sequence
    gap = 1
    while gap <= n // 3:
        gap = gap * 3 + 1  # (3^k - 1) // 2

    # Start Shell sort with Knuth's Sequence
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap = (gap - 1) // 3  # Move to the next gap in Knuth's Sequence

    return arr

def read_array_from_file(filename):
    with open(filename, 'r') as reader:
        line = reader.readline().strip()
        tokens = line[1:-1].split(', ')
        array = [int(token) for token in tokens]
    return array

def main():
    try:
        arr = read_array_from_file('RN.txt')

        # Start timing
        start_time = os.time()

        shell_sort(arr)

        # Stop timing
        end_time = os.time()

        # Calculate and print the elapsed time
        elapsed_time = end_time - start_time
        print(f"Elapsed time: {elapsed_time} milliseconds")

        print()  # Print a new line after the array

    except IOError as e:
        print(f"Error reading file: {e}")

if __name__ == "__main__":
    main()

