import numpy as np
# Create 5x5 matrix with random integers between 1 and 100
matrix = np.random.randint(1, 101, size=(5, 5))
print("Original 5x5 Matrix:")
print(matrix)
# Step 1: Extract middle 3x3 matrix
middle_3x3 = matrix[1:4, 1:4]  # rows 1-3, cols 1-3
print("\nMiddle 3x3 Matrix:")
print(middle_3x3)
# Step 2: Extract first row and last column of the 3x3
first_row = middle_3x3[0, :]       # first row
last_column = middle_3x3[:, -1]    # last column
print("\nFirst row of 3x3:", first_row)
print("Last column of 3x3:", last_column)
# Step 3: Dot product
dot_product = np.dot(first_row, last_column)
print("\nDot Product of first row and last column:", dot_product)
