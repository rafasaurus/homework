import numpy as np
import matplotlib.pyplot as plt
miu = 10# for mixed version
n0 = 12947 
exponent_dist_lambda = 0.8
# for t in range(10):
t = 2
__lambda__ = 8*t+3
k = 12
m = pow(2, k)
randoms = np.array([])
randoms_mixed = np.array([])
last_n = 1
last_n_mixed = 1
index__ = np.array([])
for i in range(pow(2, k-2)):
    index__ = np.append(index__, i)
    n = (last_n * __lambda__) % m
    n_mixed = (last_n_mixed * __lambda__ + miu) % m
    last_n = n
    last_n_mixed = last_n
    randoms = np.append(randoms, n/m)
    randoms_mixed = np.append(randoms_mixed, n_mixed/m)
print(randoms)
print(np.mean(randoms))
print("================\n", randoms_mixed)
print(np.mean(randoms_mixed))

exponent_dist = (-1/exponent_dist_lambda) * np.log(randoms_mixed)
print("exponent_dist mean :", np.mean(exponent_dist))
plt.figure(1)
plt.subplot(211)
plt.title("mine")
plt.scatter(index__, exponent_dist)
plt.grid(True)

randoms_mixed = np.random.rand(1, pow(2, k-2))
exponent_dist = (-1/exponent_dist_lambda) * np.log(randoms_mixed)
plt.subplot(212)
plt.title("numpy")
plt.scatter(index__, exponent_dist)
plt.grid(True)

plt.scatter(index__, exponent_dist)
plt.show()
