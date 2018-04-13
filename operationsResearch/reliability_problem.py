#/usr/bin/python
import numpy as np
import time
import copy
import matplotlib.pyplot as plt
l = [0.001, 0.0008, 0., 0.0001, 0.00001, 0.00000001, 0.1, 0.01]

# ****************** input data *******************

# p = np.array([0.9, 0.75, 0.65, 0.8, 0.85], dtype=float)
# weight = np.array([5, 4, 9, 7, 7], dtype=int)
# cost = np.array([8, 9, 6, 7, 8], dtype=int)
# N = 5
# index = N
# C = 104
# W = 100
'''
p = np.array([0.9, 0.85, 0.88, 0.75, 0.9, 0.8], dtype=float)
weight = np.array([4, 8, 7, 3, 5, 3], dtype=int)
cost = np.array([4, 6, 12, 10, 5, 8], dtype=int)
N = 6
index = N
C = 130
W = 120
'''
p = np.array([0.9, 0.85, 0.88, 0.75, 0.9, 0.8, 0.75], dtype=float)
weight = np.array([4, 8, 7, 3, 5, 3, 6], dtype=int)
cost = np.array([4, 6, 12, 10, 5, 8, 10], dtype=int)
N = 7
index = N
C = 120
W = 100
# *************************************************
def fixed_left_edge_chord(leftLambda, __lambda__, iterations):  #fixed with left edge chord method "quasi-Newton method" 167 Simonyan
    """
    finds the best lambda, and the best dictionary for dynamic programming problem,
    using fixed left edge chord method 
    :return: returns the best lambda dictionary
    """
    global boolean
    global plot_prob_arr
    global plot_index_arr
    global plot_lambda_arr
    global plot_cm
    local_boolean = False
    max_probability = 0
    for __iter__ in range(iterations):
        start_time = time.time()
        print("\n******** iteration number:", __iter__,"***********")
        lambdaf_dict = compute_global_prob(func(index-1, W, m, __lambda__))
        print("\tlambda:", __lambda__ , "\n\tdict", lambdaf_dict) 
        lambdaf = lambdaf_dict["cm"]-C
        boolean = True

        # gathering plot information
        plot_cm = np.append(plot_cm, lambdaf)
        plot_index_arr = np.append(plot_index_arr, __iter__)
        plot_prob_arr = np.append(plot_prob_arr, lambdaf_dict["prob"])
        plot_lambda_arr = np.append(plot_lambda_arr, __lambda__)

        lambdaf_left_dict = compute_global_prob(func(index-1, W, m, leftLambda))
        lambdaf_left = lambdaf_left_dict["cm"]-C
        boolean = True
        
        last_labmda = copy.copy(__lambda__)
        # calulating next lambda
        __lambda__ = __lambda__ - ((leftLambda - __lambda__) * lambdaf) / (lambdaf_left - lambdaf) #####
        print("\tnext labmda:", __lambda__)
        elapsed_time = time.time()-start_time
        print("\t\ttime elapsed for the program in ms ", elapsed_time*1000)

        # checks if the probability is maximum at C-sum(cm) condition, not that important
        if abs(lambdaf) <= (min(cost)):
            local_boolean = True
        else :
            local_boolean = False
        if __lambda__ > last_labmda and local_boolean:
            
            __iter__ += 1
            lambdaf_dict = compute_global_prob(func(index-1, W, m, __lambda__))
            lambdaf = lambdaf_dict["cm"]-C
            plot_cm = np.append(plot_cm, lambdaf)
            boolean = True

            # gathering ploting data 
            plot_index_arr = np.append(plot_index_arr, __iter__)
            plot_prob_arr = np.append(plot_prob_arr, lambdaf_dict["prob"])
            plot_lambda_arr = np.append(plot_lambda_arr, __lambda__)
            
            return lambdaf_dict


def prob(p, m):
    return 1-pow(1-p, 1+m)


def compute_global_prob(dictionary):
    answer = 1
    # print(dictionary)
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
    global debug_index
    if index == 0:
        for i in range(int((W)/weight[index])+1):  # W/wi
            arr = np.append(arr, prob(p[index], i)*np.exp(-__lambda__*i*cost[index]))

        m = np.append(m, np.argmax(arr))  # arr comes with none so you should continue in line 72
        dictionary = {
                        "arr_max": np.max(arr),  # F(index)(C) 
                        "m": m, 
                        "lambda": __lambda__
                     }
        return dictionary
    else:
        for i in range(int((W)/weight[index]+1)):  # mj = C/cj # +1 ================================================================
            m = np.append(m, i)
            dictionary = func(index-1, W-i*weight[index], m, __lambda__)
            arr = np.append(arr, prob(p[index], i) * np.exp(-__lambda__*i*cost[index])*dictionary["arr_max"])
            m = m[:-1]
            m_arr = np.append(m_arr, dictionary)

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
'''
for __lambda__ in np.arange(0.00015, 0.00027 , 0.00001):  # for my problem
    start_time = time.time()
    print("-----------------------------------------------------------------------")
    global_dictionary = func(index-1, W, m, __lambda__)  ######
    print("global:", compute_global_prob(global_dictionary))        
    plot_lambda_dict = np.append(plot_lambda_dict, __lambda__)
    plot_prob_dict = np.append(plot_prob_dict, compute_global_prob(global_dictionary))
    boolean = True
    elapsed_time = time.time()-start_time
    print("time elapsed for the program in ms ", elapsed_time*1000)
'''
######### best_dict["lambda"] = round(best_dict["lambda"], 5)
best_dict = fixed_left_edge_chord(leftLambda = 0.0001, __lambda__ = 0.00007, iterations = 15)
print("\n\n\n\n***************** found the best labmda dict ******************\n\n")
print("the best dict: ", best_dict)

print("\n\n\nW:", W)
print("C:", C, " +/- " + str(min(cost)))
print("cost:", cost)
print("weight:", weight)

plt.subplot(122)
plt.title("probability dependence with iterations of lambda")
plt.xlabel('iterations')
plt.xticks(plot_index_arr, np.round(plot_lambda_arr,6))
plt.ylabel('probability')
plt.plot(plot_index_arr, plot_prob_arr)

plt.subplot(121)
plt.title("C-cm dependence with iterations of lambda")
plt.xticks(plot_index_arr, np.round(plot_lambda_arr,6))
plt.xlabel('iterations')
plt.ylabel('C-cm')
plt.plot(plot_index_arr, plot_cm)
plt.show()
