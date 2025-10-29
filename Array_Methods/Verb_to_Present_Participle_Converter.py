# ------------------------------------------------------------
# Program: Verb to Present Participle Converter 
# Author: Aviram Dhagat
# Description:
#   This program converts a list of base verbs into their present
#   participle ("-ing") forms using basic English grammar rules.
#
#   Rules Implemented:
#     - If a verb ends with "ie", replace "ie" with "ying"
#     - If a verb ends with "e", replace "e" with "ing"
#     - Otherwise, simply append "ing"
#
#   Example:
#     Input: ["go", "be", "die"]
#     Output: {'go': 'going', 'be': 'bing', 'die': 'dying'}
# ------------------------------------------------------------

# ------------------------------------------------------------
# Step 1: Define the list of base verbs
# ------------------------------------------------------------
l = ["go", "be", "die"]

# ------------------------------------------------------------
# Step 2: Define function to convert verbs to "-ing" form
# ------------------------------------------------------------
def make_ing_form(list):
    d = {}        # Dictionary to store original → converted verb
    temp = ""     # Temporary variable to hold transformed verb

    for i in l:
        if i.endswith("ie"):
            temp = i.replace("ie", "ying")  # Rule 1: "ie" → "ying"
            d[i] = temp
        elif i.endswith("e"):
            temp = i.replace("e", "ing")    # Rule 2: "e" → "ing"
            d[i] = temp
        else:
            temp = i + "ing"                # Rule 3: default case
            d[i] = temp

    return d  # Return dictionary of converted verbs

# ------------------------------------------------------------
# Step 3: Call the function and print the result
# ------------------------------------------------------------
print(make_ing_form(l))  # Output: {'go': 'going', 'be': 'bing', 'die': 'dying'}

# ------------------------------------------------------------
# Alternate logic (commented out)
#   Shows a nested conditional approach using string indexing
# ------------------------------------------------------------
#         if i[-1] == "e":
#             if i[-2] == "i":
#                 temp = i.replace("ie","ying")
#                 d[i] = temp
#             else:
#                 temp = i.replace("e","ing")
#                 d[i] = temp
#         else:
#             temp = i + "ing"
#             d[i] = temp
#     return d
