# ------------------------------------------------------------
# Program: Classify a Triangle by Its Angles
# Author: Aviram Dhagat
# Description:
#   This program accepts three angles of a triangle and determines:
#     1. If it forms a valid triangle.
#     2. If valid, identifies whether it is:
#         - Equilateral
#         - Isosceles
#         - Right-angled
#         - Scalene (normal) triangle
# ------------------------------------------------------------

# Take input for the three angles
a1 = int(input("First Angle: "))
a2 = int(input("Second Angle: "))
a3 = int(input("Third Angle: "))

# ------------------------------------------------------------
# Step 1: Check if the triangle is valid
# ------------------------------------------------------------
# The sum of the angles in a triangle must be exactly 180 degrees
if a1 + a2 + a3 != 180:
    print("❌ Not a valid triangle. The angles must sum to 180°.")
else:
    # --------------------------------------------------------
    # Step 2: Classify the triangle type
    # --------------------------------------------------------

    # All three angles are equal → Equilateral
    if a1 == a2 == a3:
        print("🔺 Equilateral Triangle")

    # Two angles are equal → Isosceles
    elif (a1 == a2) or (a2 == a3) or (a3 == a1):
        print("🔺 Isosceles Triangle")

    # One angle is 90° → Right-angled triangle
    elif (a1 == 90) or (a2 == 90) or (a3 == 90):
        print("🟩 Right-Angled Triangle")

    # All angles different → Scalene (normal) triangle
    else:
        print("🔹 Scalene (Normal) Triangle")

# ------------------------------------------------------------
# Example Input / Output
# Input:
#   First Angle : 60
#   Second Angle: 60
#   Third Angle : 60
# Output:
#   🔺 Equilateral Triangle
# ------------------------------------------------------------
