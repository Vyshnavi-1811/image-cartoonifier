#Part A
import numpy as np

my_list = [[40, 42, 46, 104], [5, 6, 7, 8], [6, 7, 9, 10], [1, 3, 5, 7]]

my_array = np.array(my_list)

diagonal = np.diag(my_array)

trace = np.trace(my_array)

max_row = np.max(my_array, axis=1)
min_row = np.min(my_array, axis=1)

print("Part A:")
print(f"Diagonal elements: {diagonal}")
print(f"Trace: {trace}")
print(f"Max element of each row: {max_row}")
print(f"Min element of each row: {min_row}")

#Part B
my_array_2 = np.random.uniform(0, 1, size=(4, 4))

print("\nPart B:")
print(my_array_2)

#Part C
result_array = my_array * my_array_2

print("\nPart C:")
print(result_array)