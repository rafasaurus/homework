import numpy as np
C = 100
p = np.array([0.9,0.75,0.65,0.8,0.85],dtype=float)
#component_type = np.array([1,2,3,4,5],dtype=int)
cost = np.array([5,4,9,7,7],dtype=int)
weight = np.array([8,9,6,7,8],dtype=int)

l= 0.001

mj = np.array([2,3,4,2,2],dtype = int)
print(np.dot(mj,weight))
N=5
def phi(p,mj):
    q=1
    for i in range(N):
        q *= 1-pow(1-p[i], mj[i])
    return q
#print(phi(p,mj))
def phi(p,m):

    return 1-pow(1-p, 1+m)

def func():
    arr = np.array([],dtype=float)
    for i in range(20+1):#C/ci
        middle = phi(p[0],i)
        arr = np.append(arr, middle*np.exp(-l*mj[0]*weight[0]))
    print(arr)
    print("reliable quantity of m1 = ",np.argmax(arr,axis = 0))
func()
print("wjmj",np.dot(weight,mj))
print("cjmj",np.dot(cost,mj))
