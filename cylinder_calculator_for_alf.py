
# ========== IMPORT/S ==========
import math

# ========== VARIABLE/S==========


# ========== PSEUDO CODE ==========
# - Printing 'CYLINDER VOLUME CALCULATOR FOR ALF'
print("CYLINDER VOLUME CALCULATOR FOR ALF")


# - Asking the user for his/her desire value for the radius and height of the cylinder
radius_value_from_the_user = float(input("Enter a number for the cylinder's radius:"))
height_value_from_the_user = float(input("Enter a number for the cylinder's height:"))


# - Calculating the volume of the cylinder using the formula V = πr^2h.
volume = math.pi*pow(radius_value_from_the_user,2)*height_value_from_the_user


# - Displaying the the calculated volume with 2 decimal places.
print("The volume of the cylinder is", "%.2f" % volume)