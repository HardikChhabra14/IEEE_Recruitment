# Define two lists
list1 = [3, 4, 5, 1, 4, 6, 1, 7, 7]
list2 = [5, 8, 2, 9, 9, 4, 6, 3]

# Find intersection without duplicates
intersection = list(set(list1) & set(list2))

# Print result
print("List 1:", list1)
print("List 2:", list2)
print("Intersection (no repeats):", intersection)
