import numpy as np
def get_congruent_randoms(N0=2923121):
   #congruent params
    t = 2
    __lambda__ = 8*t+3
    k = 14 
    m = pow(2, k)
    #last_n = 1
    last_n_mixed = N0
    miu = 10  #  for mixed version
    #n0 = 12947 
    #randoms = np.array([])
    randoms_mixed = np.array([]) #
    for i in range(pow(2, k-2)):
        #n = (last_n * __lambda__) % m
        n_mixed = (last_n_mixed * __lambda__ + miu) % m
        #last_n = n
        last_n_mixed = n_mixed
        #randoms = np.append(randoms, n/m)
        randoms_mixed = np.append(randoms_mixed, n_mixed/m)
        #r = n_mixed/m
        #S = S * r
    
        #if S < np.exp(-poisson_lambda):
        #    poisson_randoms = np.append(poisson_randoms, J)    
        #    J = 0
        #    S = 1
        #else:
        #    J = J+1
    return randoms_mixed

def get_exponential(randoms, exponent_dist_lambda = 0.8):
    exponent_dist = (-1/exponent_dist_lambda) * np.log(randoms)
    return exponent_dist

def get_poisson(poisson_lambda = 3, N0=2923121):
    t = 2
    __lambda__ = 8*t+3
    k = 14 
    m = pow(2, k)
    #last_n = 1
    last_n_mixed = N0
    miu = 10  #  for mixed version
    #n0 = 12947 
    #randoms = np.array([])
    poisson_randoms = np.array([])
    randoms_mixed = np.array([]) #
    S = 1
    J = 0
    for i in range(pow(2, k-2)):
        n_mixed = (last_n_mixed * __lambda__ + miu) % m
        last_n_mixed = n_mixed
        randoms_mixed = np.append(randoms_mixed, n_mixed/m)
        r = n_mixed/m
        S = S * r
    
        if S < np.exp(-poisson_lambda):
            poisson_randoms = np.append(poisson_randoms, J)    
            J = 0
            S = 1
        else:
            J = J+1
    return poisson_randoms