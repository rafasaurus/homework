import numpy as np
import matplotlib.pyplot as plt
miu = 10# for mixed version
n0 = 12947 
exponent_dist_lambda = 0.4
poisson_lambda = 3
# for t in range(10):
t = 2
__lambda__ = 8*t+3

k = 10
m = pow(2, k)
randoms = np.array([])
randoms_mixed = np.array([])
last_n = 1
last_n_mixed = 1
index__ = np.array([])
S = 1
J = 0
poisson_randoms = np.array([])
poison_index_plot = np.array([])
index_poison = 0
for i in range(pow(2, k-2)):
    index__ = np.append(index__, i)
    n = (last_n * __lambda__) % m
    n_mixed = (last_n_mixed * __lambda__ + miu) % m
    last_n = n
    last_n_mixed = last_n
    randoms = np.append(randoms, n/m)
    randoms_mixed = np.append(randoms_mixed, n_mixed/m)

    r = n_mixed/m
    S = S * r

    if S < np.exp(-poisson_lambda):
        poisson_randoms = np.append(poisson_randoms, J)    
        J = 0
        S = 1
        index_poison += 1
        poison_index_plot = np.append(poison_index_plot, index_poison)
    else:
        J = J+1

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
plt.scatter(poison_index_plot, poisson_randoms)

plt.show()
print(poisson_randoms)
