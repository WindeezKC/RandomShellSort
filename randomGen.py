import random

def generate_random_numbers_to_file(num_count, filename):
    with open(filename, 'w') as file:
        for _ in range(num_count):
            num = random.randint(1, 2000000)
            file.write(f"{num}\n")

# Generate 1 million random numbers and write them to random_numbers.txt
generate_random_numbers_to_file(1000000, 'random_numbers15.txt')



#11 = 100000000
#12 = 10000000
#13 = 50000
#14 = 1000
#15 = 1000000
