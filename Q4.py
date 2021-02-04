import My_lib
import math


def givenFunction(x, y, z):
    g = 9.8
    return -g


data = My_lib.boundaryValueProblem(
    givenFunction, (0, 2), (5, 45), 100, 25, 0.0002, 0.1)


print("Velocity is :", data[0][2], "m/s")

# Output
# Velocity is : 33.059166666666634 m/s
