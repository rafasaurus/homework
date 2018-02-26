import numpy as np
w = np.array([0.2, 0.4, 0.3, 0.1])
f = np.array([10,20,35,98,73,12,46,33,2,14,
              1000,4444,2313,8891,5839,1922,9982,3412,5673,7999,
              4,2,6,14,2,8,5,19,13,16,
              8,2,1,3,2,7,2,1,2,9])

f = f.reshape((4,10))
print(f)
print()

f_max = np.zeros((4, 1))
f0 = np.zeros((4, 10))
for i in range(f.shape[0]):
    f_max[i] = max(f[i])
    for j in range(f.shape[1]):
        f0[i][j] = np.sum((f_max[i] - f[i][j])/(abs(f_max[i])))*w[i]
    print(f_max[i])#= max()
print(f0)
print()
arr = np.zeros(shape=(4,1))
print(arr)

for i in range(f0.shape[0]):
    arr[i] = np.sum(f0[i])
    print(type(arr[i]))
    print(arr[i])
min = min(arr)
print("minimum=",min)