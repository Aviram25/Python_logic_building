# ------------------------------------------------------------
# Program: Employee Skill Tracker 
# Author: Aviram Dhagat
# Description:
#   This program demonstrates basic dictionary operations in Python
#   using a sample dataset of employees and their programming skills.
#
#   Features:
#     - Displaying employee names and skill sets
#     - Searching for employees with a specific skill (e.g., Java)
#     - Updating, adding, and removing employee entries
# ------------------------------------------------------------

# ------------------------------------------------------------
# Step 0: Define dictionary of employees and their skills
# ------------------------------------------------------------
employees = {
    'Amol': ['C', 'C++', 'Java'],
    'Ishaan': ['Python', 'SQL', 'JavaScript'],
    'Vineet': ['Go', 'Rust', 'C'],
    'Khush': ['HTML', 'CSS', 'JavaScript'],
    'Nikhil': ['Java', 'Spring', 'Hibernate'],
    'Aviram': ['Python', 'Django', 'Flask'],
    'Sneha': ['R', 'Python', 'Data Visualization'],
    'Ravi': ['C#', '.NET', 'Azure']
}

# ------------------------------------------------------------
# Step 1: Print all employee names (dictionary keys)
# ------------------------------------------------------------
print(employees.keys())

# ------------------------------------------------------------
# Step 2: Print all skill sets (dictionary values)
# ------------------------------------------------------------
print(employees.values())

# ------------------------------------------------------------
# Step 3: Search for employees who know 'Java'
#   Loop through each employee and check if 'Java' is in their skill list
# ------------------------------------------------------------
for key, val in employees.items():
    for i in val:
        if i == "Java":
            print(key)

# ------------------------------------------------------------
# Step 4: Update Ishaan's skills to only include 'AI'
# ------------------------------------------------------------
employees.update({'Ishaan': ['AI']})
print(employees.values())

# ------------------------------------------------------------
# Step 5: Add a new employee 'Kaku' with a humorous skill set
# ------------------------------------------------------------
employees['Kaku'] = ['Sab Kuch']
print(employees)

# ------------------------------------------------------------
# Step 6: Remove 'Kaku' from the dictionary
# ------------------------------------------------------------
employees.pop('Kaku')
print(employees)
