import numpy as np
import time

# input data

p = np.array([0.9, 0.75, 0.65, 0.8, 0.85], dtype=float)
cost = np.array([5, 4, 9, 7, 7], dtype=int)
weight = np.array([8, 9, 6, 7, 8], dtype=int)
N = 5
index = N
C = 100

#p = np.array([0.88, 0.88, 0.88, 0.88, 0.88, 0.88], dtype=float)
#cost = np.array([7, 7, 7, 7, 7, 7], dtype=int)
#weight = np.array([12, 12, 12, 12, 12, 12], dtype=int)
#
#__lambda__ = 0.001
#N = 6
#index = N
#C = 130

C_global = C
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
        for i in range(int(C/cost[index])+1):  # C/ci
            arr = np.append(arr, prob(p[index], i)*np.exp(-__lambda__*i*weight[index]))
        arr_global = np.append(arr_global, np.max(arr))
        m = np.append(m, np.argmax(arr))
        C -= m[index]*cost[index]
        # print("C=", C)
        dictionary = {"arr_max": np.max(arr), "m": m}
        # print("index", index, "th dictionary=", dictionary, "**********************")
        # print("m=============", m)
        return dictionary
    else:
        dictionary = func(index)
        for i in range(int(C/cost[index])+1):  # C/c
            arr = np.append(arr, prob(p[index], i)*np.exp(-__lambda__*i*weight[index])*dictionary["arr_max"])
        arr_global = np.append(arr_global, np.max(arr)) 
        m = np.append(m, np.argmax(arr))
        C -= m[index]*cost[index]
        # print("C=", C)
        # print("index", index, "th dictionary=", dictionary, "**********************") 
        # print("m=============", m)
        dictionary = {"arr_max": np.max(arr), "m": m}
        return dictionary

for i in np.arange(0.0001, 0.01, 0.0001):
    __lambda__ = i
    print("lambda=",__lambda__)
    m = np.array([], dtype=int)
    arr_global = np.array([], dtype=int)
    C = C_global

    start_time = time.time()
    global_dictionary = func(index)
    elapsed_time = time.time()-start_time

    #print("\n------------------------------------------------------------")
    #print("m = ", global_dictionary["m"])
    #print("arr_global = ", arr_global)
    #print("------------------------------------------------------------\n")

    answer = 1
    # calculating the answer
    for i in range(N):
        answer = answer * prob(p[i],  global_dictionary["m"][i]) * np.exp(-__lambda__*global_dictionary["m"][i]*weight[i])
    print("m", global_dictionary["m"])
    print("mw=", np.dot(global_dictionary["m"], weight)) 
    print("cw", np.dot(global_dictionary["m"], cost))
    print("theprobability of successful operation is", answer*np.exp(__lambda__*np.dot(weight, global_dictionary["m"]))) 
    if np.dot(global_dictionary["m"], weight) == 120:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("=-=-=-=-=-=-=-==--=-=-=--=--=--=-=--=-=-=-=-=-==-=-=--=-=-=-=-=-=--=-==-=--=--\n", __lambda__)
        break 

print("\n------------------------------------------------------------")
print("m = ", global_dictionary["m"])
print("arr_global = ", arr_global)
print("------------------------------------------------------------\n")

answer = 1
# calculating the answer
for i in range(N):
    answer = answer * prob(p[i],  global_dictionary["m"][i]) * np.exp(-__lambda__*global_dictionary["m"][i]*weight[i])

print("func(", N, ") with cost constraint", C_global, "is ", answer)
print("total weight is ", np.dot(weight, global_dictionary["m"]))
print("total cost is", np.dot(cost, global_dictionary["m"]), "\n")
print("time elapsed for the program in ms ", elapsed_time*1000)
print("the probability of successful operation is", answer*np.exp(__lambda__*np.dot(weight, global_dictionary["m"])))
