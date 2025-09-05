import numpy as np

# Step 1: Create 5x5 matrix with random integers between 1 and 100
matrix = np.random.randint(1, 101, size=(5, 5))
print("Original 5x5 Matrix:")
print(matrix)

# Step 2: Print max, min, and mean
print("\nMaximum:", matrix.max())
print("Minimum:", matrix.min())
print("Mean:", matrix.mean())

# Step 3: Normalize between 0 and 1
normalized = (matrix - matrix.min()) / (matrix.max() - matrix.min())
print("\nNormalized Matrix (0-1):")
print(normalized)

# Step 4: Flatten and sort
flattened_sorted = np.sort(matrix.flatten())
print("\nFlattened & Sorted Array:")
print(flattened_sorted)
