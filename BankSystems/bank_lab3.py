import numpy as np

arr = np.array([19, 11, 4, 3.5, 3, 1.5, 1], dtype=float)
p = np.sort(arr,kind='quicksort',order=None,axis=-1)[::-1]

def f0(global_i):
    for local_i in range(arr.size,global_i, -1):
        debug = np.sum(arr[local_i:])
        #print(debug)
        #print()
        if arr[global_i] < debug:
            #print("arrf0=", arr[global_i])
            #print("arr_f0_index=", global_i)
            return 1

if p.any() == arr.any():
    for i in range(arr.size-2, -1, -1):
        f0(i)
        print("++++++++++++++")
        if f0(i) == 1:
            print("for i=", i)
            print("arr=", arr[i])

            #break
