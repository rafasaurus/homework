import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(sum(map(ord, "distributions")))
sns.set(color_codes=True)


def binomial_dist(randoms_mixed, P):
    condition = randoms_mixed <= P
    print(condition.shape)
    print(randoms_mixed.shape)
    plt.subplot(428)
    plt.title("binomial")
    binomial__ = np.extract(condition, randoms_mixed)
    sns.distplot(binomial__)


def sigmoid(z):
    plt.subplot(428)
    plt.title("sigmoid")
    __sigmoid__ = 1/(1+np.exp(-z))
    sns.distplot(__sigmoid__, bins = 100)


def __randn__log__(randoms_mixed, expectaion, sigma):  # normal distribution rand
    length = int(randoms_mixed.shape[1]/12)
    print(length)
    randoms_mixed = randoms_mixed[0, :length*12]
    print(randoms_mixed)
    randoms_mixed = randoms_mixed.reshape((length, 12))
    print(randoms_mixed)
    S = 0
    randoms_normal_log = np.array([])
    x_axis = np.array([])
    x_axis_index = 0
    for randoms_mixed_i in randoms_mixed:
        S = 0
        x_axis_index += 1
        x_axis = np.append(x_axis, x_axis_index)
        for j in range(12):
            S += randoms_mixed_i[j]
        randoms_normal_log = np.append(randoms_normal_log, np.exp(expectaion + sigma*(S-6)))

    plt.subplot(427)
    plt.title("normal log dist")
    plt.xlabel('number of points')
    plt.ylabel('P(X)')
    print("x_axis_index.shape", x_axis.shape, randoms_normal_log.shape)
    # plt.scatter(x_axis, randoms_normal_log)

    sns.distplot(randoms_normal_log, bins=100)
    return randoms_normal_log

def __randn__(randoms_mixed, expectaion, sigma):  # normal distribution rand
    length = int(randoms_mixed.shape[1]/12)
    print(length)
    randoms_mixed = randoms_mixed[0, :length*12]
    print(randoms_mixed)
    randoms_mixed = randoms_mixed.reshape((length, 12))
    print(randoms_mixed)
    S = 0
    randoms_normal = np.array([])
    x_axis = np.array([])
    x_axis_index = 0
    for randoms_mixed_i in randoms_mixed:
        S = 0
        x_axis_index += 1
        x_axis = np.append(x_axis, x_axis_index)
        for j in range(12):
            S += randoms_mixed_i[j]
        randoms_normal = np.append(randoms_normal, expectaion + sigma*(S-6))

    plt.subplot(423)
    plt.title("nomrla dist")
    plt.xlabel('number of points')
    plt.ylabel('P(X)')
    print("x_axis_index.shape", x_axis.shape, randoms_normal.shape)
    # plt.scatter(randoms_normal, x_axis)
    sns.distplot(randoms_normal, bins=100)
    return randoms_normal


def erlang_rand(randoms_mixed):
    length = int(randoms_mixed.shape[1]/12)
    randoms_mixed = randoms_mixed[0, :length*12]
    randoms_mixed = randoms_mixed.reshape((length, 12))
    randoms_erlang = np.array([])
    erlang_alpha = 0.5
    x_axis = np.array([])
    x_axis_index = 0
    for randoms_mixed_i in randoms_mixed:
        x_axis_index += 1
        x_axis = np.append(x_axis, x_axis_index)
        randoms_erlang = np.append(randoms_erlang, -1/erlang_alpha * np.log(np.prod(randoms_mixed_i))) 

    plt.subplot(426)
    plt.title("erlang distribution")
    plt.xlabel('number of points')
    plt.ylabel('P(X)')
    # plt.scatter(randoms_erlang, x_axis)
    sns.distplot(randoms_erlang, bins=100)
    return randoms_erlang
miu = 10  #  for mixed version
n0 = 12947 
exponent_dist_lambda = 0.4
poisson_lambda = 3
# for t in range(10):
t = 2
__lambda__ = 8*t+3

k = 14
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
    # poisson ditribution 
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
    # poisson distribution
    #
print(randoms)
print(np.mean(randoms))
print("================\n", randoms_mixed)
print(np.mean(randoms_mixed))
###
exponent_dist = (-1/exponent_dist_lambda) * np.log(randoms_mixed)
# veibul page 139 Chilingaryan
veibul_alpha = 1
veibul_beta = 1
veibul_dist = (pow(-1/veibul_alpha*np.log(randoms_mixed),1/veibul_beta))

print("exponent_dist mean :", np.mean(exponent_dist))
plt.figure(1)
plt.subplot(421)
plt.xlabel('number of points')

plt.ylabel('P(X)')
plt.title("log distribution")
#plt.scatter(index__, exponent_dist)
sns.distplot(exponent_dist, bins=100)
plt.grid(True)

randoms_mixed = np.random.rand(1, pow(2, k-2))
exponent_dist = (-1/exponent_dist_lambda) * np.log(randoms_mixed)
plt.subplot(422)
plt.xlabel('number of points')
plt.ylabel('P(X)')
plt.title("poisson distribution")
# plt.scatter(poison_index_plot, poisson_randoms)
sns.distplot(poisson_randoms, bins=100, kde = False)

plt.subplot(424)
plt.xlabel('number of points')
plt.ylabel('P(X)')
plt.title("random vars")
# plt.scatter(index__, randoms_mixed)
sns.distplot(randoms_mixed, bins=100,  kde=False)

print(poisson_randoms)
sigma = 1
expectaion = 0
randoms_normal = __randn__(randoms_mixed, expectaion, sigma)
print("randoms_normal:", randoms_normal)

plt.subplot(425)
plt.xlabel('number of points')
plt.ylabel('P(X)')
plt.title("veibul")
# plt.scatter(index__, veibul_dist)
sns.distplot(veibul_dist, bins=100)
print("veibul dist:", veibul_dist)

randoms_erlang_dist = erlang_rand(randoms_mixed)
print("randoms_erlang:", randoms_erlang_dist)



randoms_normal_log = __randn__log__(randoms_mixed, expectaion, sigma)
print("randoms_erlang:", randoms_normal_log)
'''
sigmoid(randoms_mixed)
'''
P_binomial = 0.3
binomial_dist(randoms_mixed, P_binomial)
plt.show()
