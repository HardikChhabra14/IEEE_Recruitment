# BITSAT 2024 Cutoff Marks Data
# Based on approximate cutoff trends for the specified branches

# Create the cutoff list in tuple format
cutoff_list = [
    # Pilani Campus
    ("Pilani", "CS", 327),
    ("Pilani", "Eco", 275),
    ("Pilani", "Chemical", 285),
    ("Pilani", "Bio", 268),
    
    # Goa Campus
    ("Goa", "CS", 315),
    ("Goa", "Eco", 265),
    ("Goa", "Chemical", 270),
    ("Goa", "Bio", 258),
    
    # Hyderabad Campus
    ("Hyderabad", "CS", 310),
    ("Hyderabad", "Eco", 260),
    ("Hyderabad", "Chemical", 265),
    ("Hyderabad", "Bio", 252)
]

print("Cutoff List:")
print("=" * 50)
for item in cutoff_list:
    print(f'("{item[0]}", "{item[1]}", {item[2]})')

print("\n" + "=" * 50)

# Convert list to dictionary format
cutoff_dict = {}

for campus, branch, marks in cutoff_list:
    if campus not in cutoff_dict:
        cutoff_dict[campus] = {}
    cutoff_dict[campus][branch] = marks

print("\nCutoff Dictionary:")
print("=" * 50)
print("{")
for campus, branches in cutoff_dict.items():
    print(f'    "{campus}": {{', end="")
    branch_items = []
    for branch, marks in branches.items():
        branch_items.append(f'"{branch}": {marks}')
    print(", ".join(branch_items), end="")
    print("},")
print("}")

# Alternative: Pretty print the dictionary
print("\n" + "=" * 50)
print("Pretty Printed Dictionary:")
print("=" * 50)

import json
print(json.dumps(cutoff_dict, indent=4))

# Function to easily access cutoffs
def get_cutoff(campus, branch):
    """
    Function to get cutoff marks for a specific campus and branch
    
    Args:
        campus (str): Campus name ("Pilani", "Goa", "Hyderabad")
        branch (str): Branch name ("CS", "Eco", "Chemical", "Bio")
    
    Returns:
        int: Cutoff marks or None if not found
    """
    return cutoff_dict.get(campus, {}).get(branch)

# Example usage of the function
print("\n" + "=" * 50)
print("Example Usage:")
print("=" * 50)
print(f"CS Pilani cutoff: {get_cutoff('Pilani', 'CS')}")
print(f"Eco Goa cutoff: {get_cutoff('Goa', 'Eco')}")
print(f"Chemical Hyderabad cutoff: {get_cutoff('Hyderabad', 'Chemical')}")

# Display all cutoffs in a formatted table
print("\n" + "=" * 60)
print("BITSAT 2024 Cutoff Summary Table:")
print("=" * 60)
print(f"{'Campus':<12} {'CS':<6} {'Chemical':<10} {'Eco':<6} {'Bio':<6}")
print("-" * 60)

for campus in ["Pilani", "Goa", "Hyderabad"]:
    cs_cutoff = cutoff_dict[campus]["CS"]
    chem_cutoff = cutoff_dict[campus]["Chemical"]
    eco_cutoff = cutoff_dict[campus]["Eco"]
    bio_cutoff = cutoff_dict[campus]["Bio"]
    print(f"{campus:<12} {cs_cutoff:<6} {chem_cutoff:<10} {eco_cutoff:<6} {bio_cutoff:<6}")
