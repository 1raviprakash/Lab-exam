import My_lib
import math

# p = math.exp(x)


def fun(n):
    return (math.exp(n)*(n-5)+5)


x = 1

print("If value of X is ", x)
print("Root using Newton Raphson = ", My_lib.newtonraphson_Root(fun, x))

print("Value of b is", (6.626*(10**(-34))*3*10**(8)) /
      (1.381*10**(-23)*My_lib.newtonraphson_Root(fun, x)), "m-k")

# Output
# If value of X is  1
# Root using Newton Raphson =  4.587857311020147e-16
# Value of b is 31373943161980.71 m-k
