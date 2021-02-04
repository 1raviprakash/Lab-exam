# Library
import My_lib
import math

# Function


def fun(x):
    return (1/(math.sqrt(1-(math.sin((math.pi)/8))**2*(math.sin(x))**2)))


# Limits
a = -((math.pi)/4)
b = ((math.pi)/4)

N = 10
print("Time period using Simpson integration technique is = ",
      (My_lib.simpson(a, b, fun, N))*4*math.sqrt(1/(9.8)))

# Output
# Time period using Simpson integration technique is =  2.034747435998019
