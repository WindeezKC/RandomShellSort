import matplotlib.pyplot as plt

# Example data
sort_names = ['Randomized ShellSort', 'Knuth ShellSort', 'Hibbard ShellSort', 'ShellSort']
execution_times = [57.89, 97.52 , 98.44, 103.71]  # Milliseconds, replace with your actual data

# Creating the bar chart
plt.figure(figsize=(10, 6))
plt.bar(sort_names, execution_times, color=['blue', 'green', 'red', 'purple'])

plt.xlabel('ShellSort Implementations')
plt.ylabel('Execution Time (Seconds)')
plt.title('Comparison of ShellSort Implementations')
plt.ylim(30, 120)  # Adjust based on your data range

# Adding the text labels on the bars
for i in range(len(execution_times)):
    plt.text(i, execution_times[i] + 1, str(execution_times[i]), ha = 'center', color = 'black')

plt.show()
