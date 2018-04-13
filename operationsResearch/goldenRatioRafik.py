# https://www.encyclopediaofmath.org/index.php/Dichotomy_method
# Dichotomy method finds min(max) of f(x) convex(concave) function "in the range of [a,b]" 
import numpy as np
import math

def f(x):
        return 5*np.tan(pow(x,2))+12*pow(x,2)-6*x+3

def dicho(XL, XR, extr = "max"):
    for i in range(10):
        x1 = float(XL+0.382*(XR-XL))
        x2 = float(XR-0.382*(XR-XL))
        f1 = f(x1)
        f2 = f(x2)
        if extr == "max":
            if f(x1) >= f(x2):
                XR = x2 
            elif f(x1) < f(x2):
                XL = x1
        elif extr == "min":
            if f(x1) >= f(x2):
                XL = x1
            elif f(x1) < f(x2):
                XR = x2
        print(x1)
    return x1


extr = "min"
a = -1
b = 1

print("in range " + "[" + str(a) +  "," + str(b) + "]")
dicho_ = dicho(a, b, extr)
print(extr, "=", dicho_)
print("f_extr:", f(dicho_))


