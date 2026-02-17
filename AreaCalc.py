# Author: Rosy Dhakal | Project: Wall Paint Estimator
import math
def paint_calc(height, width, coverage):
    # Fixed: Use the 'height' and 'width' parameters passed into the function
    numberOfCan = math.ceil((height * width) / coverage)
    print(f"You need {numberOfCan} cans.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

paint_calc(height=test_h, width=test_w, coverage=coverage)