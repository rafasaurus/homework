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
#p = np.array([0.88, 0.88, 0.88, 0.88, 0.88, 0.88], dtype=float)
#cost = np.array([7, 7, 7, 7, 7, 7], dtype=int)
#weight = np.array([12, 12, 12, 12, 12, 12], dtype=int)
#N = 6
#index = N
#C = 130

C_global = C
m = np.array([], dtype=int)
arr_global = np.array([], dtype=int)



def prob(p, m):
    return 1-pow(1-p, 1+m)

def compute_global_prob(dictionary):
    answer = 1
    # calculating the answer
    #print("debug")
    #print(dictionary)
    for i in range(N):
        answer = answer * prob(p[i],  dictionary["m"][i]) * np.exp(-dictionary["lambda"]*dictionary["m"][i]*weight[i])
    wm = np.dot(dictionary["m"], weight) 
    cm = np.dot(dictionary["m"], cost)
    #print("m", dictionary["m"])
    #print("the probability of successful operation is", answer*np.exp(dictionary["lambda"]*np.dot(weight, dictionary["m"]))) 
    return_dict = {"prob":answer*np.exp(dictionary["lambda"]*np.dot(weight, dictionary["m"])),"wm":wm, "cm":cm, "m":dictionary["m"]}
    return return_dict 

def func(index, __lambda__):
    arr = np.array([], dtype=float)
    global m
    global arr_global
    global C
    index -= 1
    # print("C=",C)
    # arr_global = np.append(arr_global) = np.array([],dtype=float)
    # print("type of m============",type(m))
    if index == 0:
        for i in range(int(C/cost[index])+1):  # C/ci
            arr = np.append(arr, prob(p[index], i)*np.exp(-__lambda__*i*weight[index]))
        arr_global = np.append(arr_global, np.max(arr))
        m = np.append(m, np.argmax(arr))
        C -= m[index]*cost[index]
        # print("C=", C)
        dictionary = {"arr_max": np.max(arr), "m": m, "lambda":__lambda__}
        # print("index", index, "th dictionary=", dictionary, "**********************")
        # print("m=============", m)
        return dictionary
    else:
        dictionary = func(index,__lambda__)
        for i in range(int(C/cost[index])+1):  # C/c
            arr = np.append(arr, prob(p[index], i)*np.exp(-__lambda__*i*weight[index])*dictionary["arr_max"])
        arr_global = np.append(arr_global, np.max(arr)) 
        m = np.append(m, np.argmax(arr))
        C -= m[index]*cost[index]
        # print("C=", C)
        # print("index", index, "th dictionary=", dictionary, "**********************") 
        # print("m=============", m)
        dictionary = {"arr_max": np.max(arr), "m": m, "lambda":__lambda__}
        return dictionary


start_time = time.time()
boolean = True
max_probability = 0
max_lambda = 0 
max_dictionary = {}
global_wm = 0

lambda_array = np.array([])
wm_array = np.array([])
lambda_last = 0
lambda_current = 0
lambda_min = 0
lambda_max = 0
lambda_min_wm = 0
lambda_max_wm = 0
lambda_max_dict = {}
__lambda__ = 0
global_wm = 0
global_dictionary = {}
lambda_min_dict = {}
lambda_exceeded_status = False # if true then it exceeded from >0 to <0
for i in np.arange(0.00001, 0.0005, 0.00001):
    
    lambda_last = __lambda__ 
    print(bool(global_wm - W <= 0))
    __lambda__ = i
    lambda_current = __lambda__
    print("lambda=", __lambda__)
    m = np.array([], dtype=int)
    arr_global = np.array([], dtype=int)
    C = C_global

    global_dictionary = func(index, __lambda__)######

    lambda_min_dict = copy.deepcopy(lambda_max_dict)
    lambda_max_dict = copy.deepcopy(global_dictionary)
    answer = 1
    # calculating the answer
    for i in range(N):
        answer = answer * prob(p[i],  global_dictionary["m"][i]) * np.exp(-__lambda__*global_dictionary["m"][i]*weight[i])


    



    print("m", global_dictionary["m"])
    print("wm=", global_wm) 
    print("cm", np.dot(global_dictionary["m"], cost))
    print("the probability of successful operation is", answer*np.exp(__lambda__*np.dot(weight, global_dictionary["m"]))) 



    if boolean:
        boolean = False
        max_probability = answer*np.exp(__lambda__*np.dot(weight, global_dictionary["m"])) 
        max_lambda = __lambda__
        max_dictionary = global_dictionary.copy()
        print()

    if (answer*np.exp(__lambda__*np.dot(weight, global_dictionary["m"]))) > max_probability:
        max_lambda = __lambda__
        max_dictionary = global_dictionary.copy()
        max_probability = answer*np.exp(__lambda__*np.dot(weight, global_dictionary["m"])) 
    print("max prob in each iteeration", max_probability)
    
    # wm_array = np.append(wm_array,global_wm)
    # lambda_array = np.append(lambda_array,__lambda__) 
    global_wm = np.dot(global_dictionary["m"], weight)

    if bool(global_wm - W <= 0) == True:
        break

elapsed_time = time.time()-start_time
answer = 1  #  final func 
# calculating the answer
for i in range(N):
    answer = answer * prob(p[i],  max_dictionary["m"][i]) * np.exp(-max_lambda*max_dictionary["m"][i]*weight[i])

print("\n\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
max_lambda = 0.0008
print("wm", np.dot(weight, max_dictionary["m"]))
print("cm", np.dot(cost, max_dictionary["m"]))
print("the max probability of successful operation is", answer*np.exp(max_lambda*np.dot(weight, max_dictionary["m"])))
print("max m", max_dictionary["m"])
print("max_lambda=", max_lambda)
print("\n\ntime elapsed for the program in ms ", elapsed_time*1000)
print(lambda_array, wm_array)

print("lambda_current=", lambda_current, "lambda_last=", lambda_last)
print("lambda_min_wm=", lambda_min_wm, "lambda_max_wm", lambda_max_wm)
# plt.scatter(wm_array, lambda_array, s=1)
# plt.show()
print("lambda_min_dict=", lambda_min_dict)

print("lambda_max_dict=", lambda_max_dict)
print(compute_global_prob(lambda_min_dict))
print(compute_global_prob(lambda_max_dict))
