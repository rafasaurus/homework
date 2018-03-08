import numpy as np
C = 100
p = np.array([0.9,0.75,0.65,0.8,0.85],dtype=float)
#component_type = np.array([1,2,3,4,5],dtype=int)
cost = np.array([5,4,9,7,7],dtype=int)
weight = np.array([8,9,6,7,8],dtype=int)

l= 0.001

mj = np.array([2,3,4,2,2],dtype = int)
N=5
#def phi(p,mj):
#    q=1
#    for i in range(N):
#        q *= 1-pow(1-p[i], mj[i])
#    return q
#print(phi(p,mj))
def phi(p,m):
    return 1-pow(1-p, 1+m)
index = 5
m = np.array([],dtype=int)
arr_global = np.array([],dtype=int)
def func(index):
    arr = np.array([],dtype=float)
    global m
    global arr_global
    global C
    index-=1
    print("index",index,"################################################################################")
    #print("C=",C)
    #arr_global = np.append(arr_global) = np.array([],dtype=float)
    #print("type of m============",type(m))
    if index == 0:
        print("int(C/cost[index])+1)",int(C/cost[index])+1)
        for i in range(int(C/cost[index])+1):#C/ci
            arr = np.append(arr, phi(p[index],i)*np.exp(-l*i*weight[index]))
        arr_global = np.append(arr_global,np.max(arr))
        #print(arr)
        #print("reliable quantity of m1 = ",np.argmax(aarr_global = np.append(arr_global)rr,axis = 0))
        m = np.append(m, np.argmax(arr))
        C -= m[index]*cost[index]
        print("C=",C)
        dictionary = {"arr_max":np.max(arr),"m":m}
        print("th dictionary=",dictionary,"==========================================================") 
        print("m=============",m) 
        return dictionary
    else :
        #print(int(C/cost[index]))
        #return 0
        dictionary = func(index)
        print("int(C/cost[index])+1)",int(C/cost[index])+1)
        for i in range(int(C/cost[index])+1):#C/c
            arr = np.append(arr, phi(p[index],i)*np.exp(-l*i*weight[index])*dictionary["arr_max"])
        arr_global = np.append(arr_global,np.max(arr)) 
        #print(arr)
        #print("reliable quantity of m1 = ",np.argmax(arr,axis = 0))
        m = np.append(m, np.argmax(arr))
        C -= m[index]*cost[index]
        print("C=",C)
        print("th dictionary=",dictionary,"==========================================================")
        print("m=============",m)
        dictionary = {"arr_max":np.max(arr),"m":m}
        return dictionary
    
global_dictionary = func(index)
print("global_dict=",global_dictionary["m"])
print("arr_global = ",arr_global)
print("--------------")
print("wjmj",np.dot(weight,mj))
print("cjmj",np.dot(cost,mj))
answer = 1 # np.multiply(arr_global, np.exp(np.dot(*global_dictionary["m"],weight)))

for i in range(N):
    answer = answer * phi(p[i],global_dictionary["m"][i]) * np.exp(-l*global_dictionary["m"][i]*weight[i])
print("answer",answer)
print("total weight is ", np.dot(weight,global_dictionary["m"]))
print("total cost is",np.dot(cost,global_dictionary["m"]))
