from scipy.stats.stats import pearsonr
import scipy.signal
import numpy as np
A = np.array([17, 14, 17, 14, 17, 19, 16, 15, 12, 19])
B = np.array([13, 19, 17, 16, 13, 13, 20, 16, 16, 11])
C = np.array([18, 19, 16, 13, 18, 16, 15, 10, 16, 15])

P1 = 25000
P2 = 18000
P3 = 22000
thetaA = P1/(P1+P2+P3)
thetaB = P2/(P1+P2+P3)
thetaC = P3/(P1+P2+P3)
theta = np.array([thetaA, thetaB, thetaC])

sum = 0
print("theta:", theta)
Er= np.array([np.mean(A), np.mean(B), np.mean(C)])
Erp = np.dot(Er, theta)
print("risks:", np.array([np.std(A), np.std(B), np.std(C)]))
__cov__ = np.array([np.cov(A, A)[0][1],
                     np.cov(A, B)[0][1],
                     np.cov(A, C)[0][1],
                     np.cov(B, A)[0][1],
                     np.cov(B, B)[0][1],
                     np.cov(B, C)[0][1],
                     np.cov(C, A)[0][1],
                     np.cov(B, A)[0][1],
                     np.cov(C, C)[0][1]])
__cov__ = __cov__.reshape(3, 3)

print("corr:", __cov__)
for i in range(3):
    for j in range(3):
        sum += theta[i]*theta[j]*__cov__[i][j]
print("\nsigma_portolio:", pow(sum, 0.5))
print("portfel_examtaberutyun:", Erp)
print("spasvox ekamuti shexman astichan: sigma +- Erp",  Erp, "+-", pow(sum, 0.5))
#print("sigma_porfolio:", sigma_porfolio)
