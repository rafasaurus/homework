import numpy as np
import time
# input data
p = np.array([0.9, 0.75, 0.65, 0.8, 0.85], dtype=float)
cost = np.array([5, 4, 9, 7, 7], dtype=int)
weight = np.array([8, 9, 6, 7, 8], dtype=int)

__lambda__ = 0.001
N = 5
index = N
C = 100

m = np.array([], dtype=int)
arr_global = np.array([], dtype=int)

def prob(p, m):
    return 1-pow(1-p, 1+m)


def func(index):
    arr = np.array([], dtype=float)
    global m
    global arr_global
    global C
    index -= 1
    # print("C=",C)
    # arr_global = np.append(arr_global) = np.array([],dtype=float)
    # print("type of m============",type(m))
    if index == 0:
        for i in range(int(C/cost[index])+1): # C/ci
            arr = np.append(arr, prob(p[index], i)*np.exp(-__lambda__*i*weight[index]))
        arr_global = np.append(arr_global, np.max(arr))
        m = np.append(m, np.argmax(arr))
        C -= m[index]*cost[index]
        print("C=", C)
        dictionary = {"arr_max": np.max(arr), "m": m}
        print("index",index,"th dictionary=", dictionary, "**********************")
        #print("m=============", m)
        return dictionary
    else:
        dictionary = func(index)
        for i in range(int(C/cost[index])+1):  # C/c
            arr = np.append(arr, prob(p[index], i)*np.exp(-__lambda__*i*weight[index])*dictionary["arr_max"])
        arr_global = np.append(arr_global, np.max(arr)) 
        m = np.append(m, np.argmax(arr))
        C -= m[index]*cost[index]
        print("C=", C)
        print("index",index,"th dictionary=", dictionary, "**********************") 
        #print("m=============", m)
        dictionary = {"arr_max": np.max(arr), "m": m}
        return dictionary

start_time = time.time()
global_dictionary = func(index)
elapsed_time = time.time()-start_time

print("\n------------------------------------------------------------")
print("m = ", global_dictionary["m"])
print("arr_global = ", arr_global)
print("------------------------------------------------------------\n")

answer = 1 
# calculating the answer
for i in range(N):
    answer = answer * prob(p[i],  global_dictionary["m"][i]) * np.exp(-__lambda__*global_dictionary["m"][i]*weight[i])

print("answer", answer)
print("total weight is ", np.dot(weight, global_dictionary["m"]))
print("total cost is", np.dot(cost, global_dictionary["m"]),"\n")
print("time elapsed for the program in ms ",elapsed_time*1000)