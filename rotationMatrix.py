import numpy as np
arr= np.array([1,7,2,2,
               3,0,0,9,
               1,0,0,5,
               4,4,0,3],dtype=int)
arr = arr.reshape((4,4))
print(arr)
n=arr.shape[0]-1
for i in range(int(n)):
    for j in range(int(n/2)+1):
        for k in range(int(n/2)+1):
            temp = arr[iubuntu, k]

            arr[i, k] = arr[i, j]

            arr[n-k, j] = arr[n-k, n-k]

            arr[n-k, n-k] = arr[k, n-k]

            arr[k, n-k] = temp

            print(k)
        break
    break
print()
print(arr)
