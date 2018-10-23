# https://www.encyclopediaofmath.org/index.php/Dichotomy_method
# Dichotomy method finds min(max) of f(x) convex(concave) function "in the range of [a,b]" 
import numpy as np

def f(x):
    #return -9*pow(x,3)+16*pow(x,2)+24*x+15
    #return -9*pow(x,3)+16*pow(x,2)+24*x+15
    return np.exp(x)-2*x**2+4
def dicho(a, b, extr = "max"):
    for i in range(40):
        delta = 0.001
        x1 = (a+b-delta)/2
        x2 = (a+b+delta)/2
        f1 = f(x1)
        f2 = f(x2)
        if extr == "max":
            if f(x1) >= f(x2):
                b = x2 
            elif f(x1) < f(x2):
                a = x1
        elif extr == "min":
            if f(x1) >= f(x2):
                a = x1
            elif f(x1) < f(x2):
                b = x2
        # print(x1)
    return x1


extr = "min"
a = 1
b = 3

print("in range " + "[" + str(a) +  "," + str(b) + "]")
dicho_ = dicho(a, b, extr)
print(extr, "=", dicho_)
print("f_extr:", f(dicho_))
