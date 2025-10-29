# ------------------------------------------------------------
# Program: Employee Skill Analyzer 
# Author: Aviram Dhagat
# Description:
#   This script demonstrates dictionary operations in Python
#   using employee skill data. It includes:
#     - Searching for employees with a specific skill
#     - Modifying skill lists
#     - Sorting employees by number of skills
# ------------------------------------------------------------

# ------------------------------------------------------------
# Step 1: Define dictionary of employees and their skills
# ------------------------------------------------------------
emp_data = {
    'Amol': ['C', 'C++', 'Java'],
    'Aditya': ['Angular', 'Java'],
    'Aditi': ['Python', 'PHP', 'Database']
}

# ------------------------------------------------------------
# Step 2: Search for employees who know 'Python'
#   Loop through each employee and check if 'Python' is in their skill list
# ------------------------------------------------------------
for k, v in emp_data.items():
    for i in v:
        if i == "Python":
            print(k)  # Output: Aditi

# ------------------------------------------------------------
# Step 3: Append "test" to every employee's skill list
#   Demonstrates in-place mutation of dictionary values
# ------------------------------------------------------------
for k, v in emp_data.items():
    v.append("test")

# ------------------------------------------------------------
# Step 4: Print updated dictionary with "test" added to each skill list
# ------------------------------------------------------------
print(emp_data)

# ------------------------------------------------------------
# Step 5: Sort employees by number of skills (ascending)
#   Uses lambda function to sort by length of skill list
# ------------------------------------------------------------
sorted_emp = dict(sorted(emp_data.items(), key=lambda item: len(item[1])))

# ------------------------------------------------------------
# Step 6: Print sorted dictionary
# ------------------------------------------------------------
print(sorted_emp)

# ------------------------------------------------------------
# Optional Step (commented out):
#   Intended to call a function named 'emplen' on each skill list
#   Uncomment and define 'emplen' if needed
# ------------------------------------------------------------
# for k, v in emp_data.items():
#     emplen(v)
