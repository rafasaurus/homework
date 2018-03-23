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

C_global = C
m = np.array([], dtype=int)
arr_global = np.array([], dtype=int)
debug_index = 0


def prob(p, m):





    return 1-pow(1-p, 1+m)


def compute_global_prob(dictionary):
    answer = 1

    for i in range(N):
        answer = answer * prob(p[i],  dictionary["m"][i]) * np.exp(-dictionary["lambda"]*dictionary["m"][i]*weight[i])
    wm = np.dot(dictionary["m"], weight) 
    cm = np.dot(dictionary["m"], cost)

    return_dict = {"prob": answer*np.exp(dictionary["lambda"]*np.dot(weight, dictionary["m"])),"wm":wm, "cm":cm, "m":dictionary["m"]}
    return return_dict 


def func(global_index, index, __lambda__, cm, C):
    arr = np.array([], dtype=float)
    global m
    global arr_global
    global debug_index
    index -= 1
    print("CCCC:", C) 
    # print("******************************index***************************:", index)
    m = np.array([])
    if index == 0:
        # max of the phi(mj1)*exp(-lambda*weight1)
        for i in range(int((C)/cost[index])+1):  # C/ci
            arr = np.append(arr, prob(p[index], i)*np.exp(-__lambda__*i*weight[index]))
        if arr == []:
            return None


        else:
            m = np.append(m, np.argmax(arr))  # arr comes with none so youshould continue in line 72
            dictionary = {"arr_max": np.max(arr), "m": m, "lambda": __lambda__}
            return dictionary
    else:
        for i in range(int((C)/cost[index])+1):  # C/c
            cm = i*cost[index]  # MN CN
            dictionary = func(global_index, index, __lambda__, cm, C-cm)
            if dictionary == None:
                continue
            arr = np.append(arr, prob(p[index], i)*np.exp(-__lambda__*i*weight[index])*dictionary["arr_max"])
        print("arr[", index, "]:", arr)
        m = np.append(m, np.argmax(arr))
        dictionary = {"arr_max": np.max(arr), "m": m,  "lambda": __lambda__}
        debug_index += 1
        print(debug_index)
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
max_dictionary_arr = np.array([])
# -----------------------------------------------
global_index = copy.copy(index)
for __lambda__ in np.arange(0.0008, 0.0009, 0.0001):  # for my problem
    print("-----------------------------------------------------------------------")
    print("lambda=", __lambda__)

    m = np.array([], dtype=int)
    arr_global = np.array([], dtype=int)
    C = C_global
    cm = 0
    
    global_dictionary = func(global_index, index, __lambda__, cm, C)  ######
    print("global_dict:", global_dictionary)
    lambda_min_dict = copy.deepcopy(lambda_max_dict)
    lambda_max_dict = copy.deepcopy(global_dictionary)

    # first assingment of max_probability
    if boolean:
        boolean = False
        max_dictionary = global_dictionary.copy()
        max_probability = compute_global_prob(max_dictionary)["prob"]

    # check if it is max probability 
    if compute_global_prob(global_dictionary)["prob"] > max_probability:
        max_dictionary = global_dictionary.copy()
        max_probability = compute_global_prob(max_dictionary)["prob"]

    print("probability:", compute_global_prob(global_dictionary)["prob"]) 
    global_wm = np.dot(global_dictionary["m"], weight)
    # ---------------------------------
    print("m:", (global_dictionary["m"]))
    max_dictionary_arr = np.append(max_dictionary_arr, global_dictionary)
    print("wm:", global_wm)
    print("cm:", np.dot(global_dictionary["m"], cost))

    if bool(global_wm - W == 0) is True:
        the_best_dict = global_dictionary        
        
elapsed_time = time.time()-start_time
print("debug_index:",debug_index)

print("\n\ntime elapsed for the program in ms ", elapsed_time*1000)
print("\nmax_dictionary:", max_dictionary)
print("compute_global_prob:", compute_global_prob(max_dictionary))
# plt.show()
print("\nlambda_min_dict=", lambda_min_dict)
print("lambda_max_dict=", lambda_max_dict)
print()
print("global_prob min:", compute_global_prob(lambda_min_dict))
print("global_prob_max:", compute_global_prob(lambda_max_dict))
print()


try:
    print("the best dictionary is ", the_best_dict)
    print("probability dicit:", compute_global_prob(the_best_dict))
    print("******************************* success ****************************** ")
except Exception:
    print("ExceptOion: ************************** can't find best dictionary ******************************")

