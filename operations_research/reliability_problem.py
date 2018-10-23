#/usr/bin/python3
import numpy as np
#****************** input data *******************

__lambda__ = 0.00022
p = np.array([0.9, 0.85, 0.88, 0.75, 0.9, 0.8], dtype=float)
weight = np.array([4, 8, 7, 3, 5, 3], dtype=int)
cost = np.array([4, 6, 12, 10, 5, 8], dtype=int)
N = 6
index = 0
C = 130
W = 120

def compute_global_prob(dictionary):
    answer = 1
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

def prob(p, m):
    return 1-pow(1-p, 1+m)

def func(index, W, m, __lambda__, arr_max):
    """
    Bellman recurrent function
    """
    max_arr = np.array([])
    arr = np.array([], dtype=float)
    global debug_index
    if index == 0:
        for i in range(int((W)/weight[index])+1):  # W/wi
            arr = np.append( arr, prob(p[index], i)*np.exp(-__lambda__*i*cost[index]) )
            max_arr = np.append(max_arr, np.max(arr))
        print("\n\t\tTABLE:", index)
        print(max_arr.T)
        print("max_table:", np.max(max_arr))
        print("max_m:", np.argmax(max_arr))
        m = np.append(m, np.argmax(max_arr))
        arr_max = np.max(max_arr)
        dictionary = func(index+1, W-weight[index]*np.argmax(max_arr), m, __lambda__, arr_max)
        return dictionary
    else:
        for i in range(int((W)/weight[index]+1)):  # mj = C/cj #=
            arr = np.append( arr, prob(p[index], i) * np.exp(-__lambda__*i*cost[index])*arr_max )
            max_arr = np.append(max_arr, np.max(arr))
        print("\n\t\tTABLE:", index)
        print(max_arr.T)
        print("max_table:", np.max(max_arr))
        print("max_m:", np.argmax(max_arr))
        m = np.append(m, np.argmax(max_arr))
        arr_max = np.max(max_arr)
        dictionary = {
                        "arr_max": np.max(max_arr),
                        "m": m,  
                        "lambda": __lambda__
                     }
        if index+1 >= N:
            return dictionary
        else:
            return func(index+1, W-weight[index]*np.argmax(max_arr), m, __lambda__, arr_max)

m = np.array([], dtype=int)
arr_max=0 
best_dict = compute_global_prob(func(index, W, m, __lambda__, arr_max))
print("\n\nanswer: ", best_dict)
print("\nW:", W)
print("C:", C, " +/- " + str(min(cost)))
print("cost:", cost)
print("weight:", weight)
print("p:", p)
