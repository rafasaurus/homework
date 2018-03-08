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
def func(index):
    global m
    index-=1
    print("index",index,"################################################################################")
    arr = np.array([],dtype=float)
    #print("type of m============",type(m))
    if index == 0:
        for i in range(int(C/cost[index])+1):#C/ci
            arr = np.append(arr, phi(p[index],i)*np.exp(-l*i*weight[index]))
        #print(arr)
        #print("reliable quantity of m1 = ",np.argmax(arr,axis = 0))
        m = np.append(m, np.argmax(arr))
        dictionary = {"arr_max":np.max(arr),"m":m}
        print("th dictionary=",dictionary,"==========================================================") 
        print("m=============",m) 
        return dictionary
    else :
        #print(int(C/cost[index]))
        #return 0
        dictionary = func(index)
        for i in range(int(C/cost[index])+1):#C/c
            arr = np.append(arr, phi(p[index],i)*np.exp(-l*i*weight[index])*dictionary["arr_max"])
        #print(arr)
        #print("reliable quantity of m1 = ",np.argmax(arr,axis = 0))
        m = np.append(m, np.argmax(arr))
        print("th dictionary=",dictionary,"==========================================================")
        print("m=============",m)
        dictionary = {"arr_max":np.max(arr),"m":m}
        return dictionary
    
global_dictionary = func(index)
print("global_dict=",global_dictionary["m"])
print("--------------")
print("wjmj",np.dot(weight,mj))
print("cjmj",np.dot(cost,mj))
