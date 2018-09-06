import numpy as np
N=12
rm = np.array([14, 16, 22, 18, 16, 10, 12, 13, 16, 14, 19, 10])
ra = np.array([11, 12, 10, 18, 15, 7, 12, 8, 13, 10, 10, 12])
print("beta:", (np.dot(rm-np.mean(rm ), ra-np.mean(ra))/sum(pow(rm-np.mean(rm), 2))))
