import random

def f(x):
    return pow(x,2)-x-6
a = -2
b = 3
f_derivative = 6.25

N2 = 0
N1 = 1000
for k in range(N1):
    rx = random.uniform(a, b)
    ry = random.uniform(-6.25, 0)

    if (f(rx) < ry):
        N2 = N2 + 1

print(N2)
print(N1)
print("answer = ", f_derivative*(b-a)*N2/N1)