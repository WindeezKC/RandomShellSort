import time

def shell_sort(arr):
    n = len(arr)

    # Generate Knuth's Sequence
    gap = 1
    while gap < n / 3:
        gap = 3 * gap + 1  # Properly implement the 3h + 1 sequence for gap sizing

    # Start Shell sort using Knuth's Sequence
    while gap >= 1:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap = int((gap - 1) / 3)  # Decrease the gap based on Knuth's reverse formula

    return arr

def read_array_from_file(filename):
    with open(filename, 'r') as file:
        # Read numbers from each line and convert them to integers
        array = [int(line.strip()) for line in file if line.strip().isdigit()]
    return array

def main():
    try:
        arr = read_array_from_file('random_numbers12.txt')

        # Start timing
        start_time = time.time()

        shell_sort(arr)

        # Stop timing
        end_time = time.time()

        # Calculate and print the elapsed time in milliseconds
        elapsed_time = (end_time - start_time) * 1000
        print(f"Elapsed time: {elapsed_time:.2f} milliseconds")

    except IOError as e:
        print(f"Error reading file: {e}")
    except ValueError as e:
        print(f"Error processing file: {e}")

if __name__ == "__main__":
    main()
