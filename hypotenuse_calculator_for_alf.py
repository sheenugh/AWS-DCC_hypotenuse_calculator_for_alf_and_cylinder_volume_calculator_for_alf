# ========== IMPORT/S ==========
from math import sqrt

# ========== PSEUDO CODE ==========
# - Printing the 'HYPOTENUSE CALCULATOR FOR ALF"
print("HYPOTENUSE CALCULATOR FOR ALF")

# - Asking the user for his/her desire value for the two legs of the right triangle
opposite_side = float(input("Enter a number for the length of opposite side:"))
adjacent_side = float(input("Enter a number for the length of adjacent side:"))

# - Calculation of the right triangle's hypotenuse using Pythagorean Theorem
hypotenuse_side_result = sqrt(opposite_side**2 + adjacent_side**2)

# - Display the calculated hypotenuse
print("The hypotenuse of the right triangle is", "%.2f" % hypotenuse_side_result)