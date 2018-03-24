import numpy as np
import time
import matplotlib.pyplot as plt
import copy
# input data

p = np.array([0.9, 0.75, 0.65, 0.8, 0.85], dtype=float)
cost = np.array([5, 4, 9, 7, 7], dtype=int)
weight = np.array([8, 9, 6, 7, 8], dtype=int)
N = 5
index = N
C = 100
W = 104

# p = np.array([0.88, 0.88, 0.88, 0.88, 0.88, 0.88], dtype=float)
# weight = np.array([7, 7, 7, 7, 7, 7], dtype=int)
# cost = np.array([12, 12, 12, 12, 12, 12], dtype=int)
# N = 6
# index = N
# C = 130
# W = 120

m = np.array([], dtype=int)
arr_global = np.array([], dtype=int)
debug_index = 0


def prob(p, m):
    return 1-pow(1-p, 1+m)


def compute_global_prob(dictionary):
    answer = 1
    # print(dictionary)
    for i in range(N):
        answer = answer * prob(p[i],  dictionary["m"][i]) * np.exp(-dictionary["lambda"]*dictionary["m"][i]*weight[i])
    wm = np.dot(dictionary["m"], weight) 
    cm = np.dot(dictionary["m"], cost)

    return_dict = {"prob": answer*np.exp(dictionary["lambda"]*np.dot(weight, dictionary["m"])),"wm":wm, "cm":cm, "m":dictionary["m"]}
    return return_dict 
m = np.array([])


def func(global_index, index, __lambda__, C, m):
    arr = np.array([], dtype=float)
    global debug_index
    # print("******************************index", index, "***************************:")
    global max_dictionary
    global boolean
    if index == 0:
        # max of the phi(mj1)*exp(-lambda*weight1)
        for i in range(int((C)/cost[index])+1):  # C/ci
            arr = np.append(arr, prob(p[index], i)*np.exp(-__lambda__*i*weight[index]))
            
        m = np.append(m, np.argmax(arr))  # arr comes with none so you should continue in line 72
        dictionary = {"arr_max": np.max(arr), "m": m, "lambda": __lambda__, "index:": index}
        # print("m:", m)

        debug_index += 1
        return dictionary
    else:

        for i in range(int((C)/cost[index])+1):  # mj = C/cj
            # m :w= []
            m = np.append(m, i)
            cm = i*cost[index]  # MN CN
            dictionary = func(global_index, index-1, __lambda__, C-cm, m)
            arr = np.append(arr, prob(p[index], i)*np.exp(-__lambda__*i*weight[index])*dictionary["arr_max"])
            m = m[:-1]
        # m = np.append(m, np.argmax(arr))

        # print(arr)
        m = dictionary["m"]
        m = m[:-1]
        m = np.append(m, np.argmax(arr))
        dictionary = {"arr_max": np.max(arr), "m": m,  "lambda": __lambda__, "index:": index}
        if boolean:
            boolean = False
            max_dictionary = dictionary
        if compute_global_prob(max_dictionary)['prob'] < compute_global_prob(dictionary)['prob']:
            max_dictionary = copy.deepcopy(dictionary)
        print("COMPUTE_GLOBAL_PROB:", compute_global_prob(dictionary))
        # print(dictionary)
        debug_index += 1
        return dictionary


start_time = time.time()
boolean = True
max_probability = 0
max_dictionary = {}

__lambda__ = 0
global_wm = 0
global_dictionary = {}
lambda_max_dict = {}
# -----------------------------------------------
the_best_dict = {}
# -----------------------------------------------
global_index = copy.copy(index)
for __lambda__ in np.arange(0.0008, 0.0009, 0.0001):  # for my problem
    print("-----------------------------------------------------------------------")
    print("lambda=", __lambda__)

    m = np.array([], dtype=int)
    
    global_dictionary = func(global_index, index-1, __lambda__, C, m)  ######
    print("max_dictionary:", max_dictionary)
        
elapsed_time = time.time()-start_time

print("\n\ntime elapsed for the program in ms ", elapsed_time*1000)
print("debug_index:", debug_index)

try:
    print("the best dictionary is ", the_best_dict)
    print("probability dicit:", compute_global_prob(the_best_dict))
    print("******************************* success ****************************** ")
except Exception:
    print("ExceptOion: ************************** can't find best dictionary ******************************")

