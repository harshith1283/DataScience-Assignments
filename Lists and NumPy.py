import numpy as np
numbers = [10, 25, 5, 40, 60, 15, 35, 50, 20, 45]
print("Length of list:", len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
numbers.append(70)
numbers.remove(5)

print("Updated List:", numbers)
print("Ascending:", sorted(numbers))
print("Descending:", sorted(numbers, reverse=True))
arr = np.array(numbers)
print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))
