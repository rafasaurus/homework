import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

### randoms_mixed = np.random.rand(1, pow(2, k-2))
np.random.seed(sum(map(ord, "distributions")))
sns.set(color_codes=True)
__bins__ = 50

def binomial_dist(randoms_mixed, P, N_experiments): # P binomial threshold
    condition = randoms_mixed[:N_experiments] <= P
    plt.subplot(428)
    plt.title("binomial")
    binomial__ = np.extract(condition, randoms_mixed)
    sns.distplot(binomial__)
    return binomial__

def __randn__log__(randoms_mixed, expectaion, sigma):  # normal distribution rand
    length = int(randoms_mixed.shape[0]/12)
    randoms_mixed = randoms_mixed[:length*12]
    randoms_mixed = randoms_mixed.reshape((length, 12))
    S = 0
    randoms_normal_log = np.array([])
    for randoms_mixed_i in randoms_mixed:
        S = 0
        for j in range(12):
            S += randoms_mixed_i[j]
        randoms_normal_log = np.append(randoms_normal_log, np.exp(expectaion + sigma*(S-6)))

    plt.subplot(427)
    plt.title("normal log dist")
    plt.ylabel('P(X)')

    sns.distplot(randoms_normal_log, bins=__bins__)
    return randoms_normal_log

def __randn__(randoms_mixed, expectaion, sigma):  # normal distribution rand
    length = int(randoms_mixed.shape[0]/12)
    print(length)
    randoms_mixed = randoms_mixed[:length*12]
    print(randoms_mixed)
    randoms_mixed = randoms_mixed.reshape((length, 12))
    print(randoms_mixed)
    S = 0
    randoms_normal = np.array([])
    for randoms_mixed_i in randoms_mixed:
        S = 0
        for j in range(12):
            S += randoms_mixed_i[j]
        randoms_normal = np.append(randoms_normal, expectaion + sigma*(S-6))

    plt.subplot(423)
    plt.title("normal dist")
    plt.ylabel('P(X)')
    sns.distplot(randoms_normal, bins=__bins__)
    return randoms_normal


def erlang_rand(randoms_mixed):
    length = int(randoms_mixed.shape[0]/12)
    randoms_mixed = randoms_mixed[:length*12]
    randoms_mixed = randoms_mixed.reshape((length, 12))
    randoms_erlang = np.array([])
    erlang_alpha = 0.5
    for randoms_mixed_i in randoms_mixed:
        randoms_erlang = np.append(randoms_erlang, -1/erlang_alpha * np.log(np.prod(randoms_mixed_i))) 

    plt.subplot(426)
    plt.title("erlang distribution")
    plt.ylabel('P(X)')
    sns.distplot(randoms_erlang, bins=__bins__)
    return randoms_erlang
miu = 10  #  for mixed version
n0 = 12947 
exponent_dist_lambda = 0.4
poisson_lambda = 3
t = 2
__lambda__ = 8*t+3

k = 14 
m = pow(2, k)
last_n = 1
last_n_mixed = 1
sigma = 1
expectaion = 1

veibul_alpha = 1
veibul_beta = 1
S = 1
J = 0
N_experiments_binomial = 10
P_binomial = 0.9

poisson_randoms = np.array([])
randoms = np.array([])
randoms_mixed = np.array([])
for i in range(pow(2, k-2)):
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
    else:
        J = J+1
    #
print("=================================\n\t-------------congruential mixed random number generator-------------", randoms_mixed)
print("mean of congruent:", np.mean(randoms_mixed))
exponent_dist = (-1/exponent_dist_lambda) * np.log(randoms_mixed)
# veibul page 139 Chilingaryan
veibul_dist = (pow(-1/veibul_alpha*np.log(randoms_mixed),1/veibul_beta))
print("\texponent distribution:")
print("exponent_dist mean :", np.mean(exponent_dist))
plt.figure(1)
plt.subplot(424)
plt.ylabel('P(X)')
plt.title("log distribution")
plt.grid(True)
log_dist= (-1/exponent_dist_lambda) * np.log(randoms_mixed)
sns.distplot(log_dist, bins=__bins__)
print("\tlog distribution:", log_dist)

plt.subplot(422)
plt.ylabel('P(X)')
plt.title("poisson distribution")
sns.distplot(poisson_randoms, bins=__bins__, kde = False)
print("\tpoisson randoms:", poisson_randoms)

plt.subplot(421)
plt.ylabel('P(X)')
plt.title("random vars")
sns.distplot(randoms_mixed, bins=__bins__,  kde=False)

randoms_normal = __randn__(randoms_mixed, expectaion, sigma)
print("\trandoms_normal:", randoms_normal)

plt.subplot(425)
plt.ylabel('P(X)')
plt.title("veibul")
sns.distplot(veibul_dist, bins=__bins__)
print("\tveibul dist:", veibul_dist)

randoms_erlang_dist = erlang_rand(randoms_mixed)
print("\trandoms_erlang:", randoms_erlang_dist)
randoms_normal_log = __randn__log__(randoms_mixed, expectaion, sigma)
print("\trandom_normal_log:", randoms_normal_log)

# configurations of binomial distribution
binomial_dist = binomial_dist(randoms_mixed, P_binomial, N_experiments_binomial)
print("binomial_dist:", binomial_dist)

monte = np.array([])
P_last = 0

step = 0.001
for P in np.arange(int(min(randoms_normal))-1, int(max(randoms_normal)+1), step):
    condition = randoms_normal > P-step
    monte_arr = np.extract(condition, randoms_normal)

    condition1 = monte_arr <= P
    monte_arr = np.extract(condition1, monte_arr)
    print(P)
    monte = np.append(monte, monte_arr.shape)

print(monte)

plt.figure(2)
sns.distplot(monte)
#plt.hist(monte)
plt.show()

