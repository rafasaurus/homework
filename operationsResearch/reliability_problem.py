#!/usr/bin/python3
import numpy as np
import time
import copy
import matplotlib.pyplot as plt
l = [0.001, 0.0008, 0., 0.0001, 0.00001, 0.00000001, 0.1, 0.01]

# ****************** input data *******************
#__lambda__ = 0.0008
#p = np.array([0.9, 0.75, 0.65, 0.8, 0.85], dtype=float)
#weight = np.array([5, 4, 9, 7, 7], dtype=int)
#cost = np.array([8, 9, 6, 7, 8], dtype=int)
#N = 5
#index = N
#C = 104
#W = 100

__lambda__ = 0.00022
p = np.array([0.9, 0.85, 0.88, 0.75, 0.9, 0.8], dtype=float)
weight = np.array([4, 8, 7, 3, 5, 3], dtype=int)
cost = np.array([4, 6, 12, 10, 5, 8], dtype=int)
N = 6
index = N
C = 130
W = 120
wm = np.dot(np.zeros(N)+1, weight) 
cm = np.dot(np.zeros(N)+1, cost)
#W-=wm
#C-=cm


# p = np.array([0.9, 0.85, 0.88, 0.75, 0.9, 0.8, 0.75], dtype=float)
# weight = np.array([4, 8, 7, 3, 5, 3, 6], dtype=int)
# cost = np.array([4, 6, 12, 10, 5, 8, 10], dtype=int)
# N = 7
# index = N
# C = 120
# W = 100
# *************************************************

def prob(p, m):
    return 1-pow(1-p, 1+m)


def compute_global_prob(dictionary):
    answer = 1
    # print(dictionary)
    print("))))))))))))))))))))))))))))))))))))))))))):", dictionary["m"].shape)
    for i in range(N):
        answer = answer * prob(p[i],  dictionary["m"][i]) * np.exp(-dictionary["lambda"]*dictionary["m"][i]*cost[i])

    wm = np.dot(dictionary["m"], weight) 
    cm = np.dot(dictionary["m"], cost)

    return_dict = { "prob": answer*np.exp(dictionary["lambda"]*np.dot(cost, dictionary["m"])),
                    "wm":wm, 
                    "cm":cm, 
                    "m":dictionary["m"], 
                    "lambda": dictionary["lambda"]}
    return return_dict 


def func(index, W, m, __lambda__):
    """
    Bellman recurrent function
    """
    m_arr = np.array([])
    arr = np.array([], dtype=float)
    if index == 0:
        for i in range(int((W)/weight[index]+1)):
            arr = np.append(arr, prob(p[index], i)*np.exp(-__lambda__*i*cost[index]))

        m = np.append(m, np.argmax(arr))  # arr comes with none so you should continue in line 72
        dictionary = {
                        "arr_max": np.max(arr),  # F(index)(C) 
                        "m": m, 
                        "lambda": __lambda__
                     }
        return dictionary
    else:
        for i in range(int((W)/weight[index]+1)):  # mj = C/cj # +1 
            m = np.append(m, i)
            dictionary = func(index-1, W-i*weight[index], m, __lambda__)
            arr = np.append(arr, prob(p[index], i) * np.exp(-__lambda__*i*cost[index])*dictionary["arr_max"])
            m = m[:-1]
            m_arr = np.append(m_arr, dictionary)
        #
        #m = np.append(m, np.argmax(arr))     
        dictionary = {
                        "arr_max": np.max(arr),
                        "m": m_arr[np.argmax(arr)]["m"],#  
                        "lambda": __lambda__
                     }
        return dictionary

boolean = True
global_dictionary = {}
m = np.array([], dtype=int)

plot_prob_arr = np.array([])
plot_index_arr = np.array([])
plot_lambda_arr  = np.array([])
plot_cm = np.array([])

best_dict = compute_global_prob(func(index-1, W, m, __lambda__))
print("\n\n\n\n***************** found the best labmda dict ******************\n\n")
print("the best dict: ", best_dict)

print("\n\n\nW:", W)
print("C:", C, " +/- " + str(min(cost)))
print("cost:", cost)
print("weight:", weight)
print("[3, 3, 2, 4, 2, 3] 1.002668855821113 128 81")
