'''դասակառգման մեթոդը'''
import numpy as np
import copy
N=9
K=8
x = np.array([2,7,5,2,1,3,2,5,5,
              6,3,4,5,3,2,3,2,1,
              4,6,6,7,7,6,7,6,6,
              3,5,3,4,4,5,1,4,3,
              1,1,1,1,2,1,5,1,4,
              8,8,8,8,8,8,8,8,8,
              7,2,2,3,5,4,4,3,2,
              5,4,7,6,6,7,6,7,7])

x = x.reshape(8,9)
r_i_j = np.zeros(shape=(8))
print(r_i_j)
print(x)
print(" ")
for i in range(8):
    for j in range(9):
        r_i_j[i] = r_i_j[i]+x[i][j]
sorted = np.sort(r_i_j,axis = -1,kind='quicksort',order=None)
print("r_i_j=",r_i_j)
print("sorted=",sorted)
r_i_j_index=np.zeros(shape=(9))
counter = 1
r_i_j_= copy.copy(r_i_j)

for i in range(8):
    for j in range(8):
        if(sorted[i] == r_i_j[j]):
            r_i_j_index[j] = counter
            counter = counter+1
            r_i_j[j] = -1
            break




print("r_i_j_index=",r_i_j_index)

t_j = np.zeros(9)

for j in range(9):
    for i in range(8):
        if (x[i][j] == r_i_j_index[i]):
            t_j[j] +=1


print("t_j=",t_j)
T_j = np.zeros(9)
for i in range(9):
    T_j[i] = pow(t_j[i],3) - t_j[i]
print("T_j=",T_j)

T_j_sum = 0
for i in range(9):
    T_j_sum += T_j[i]

S = 0


for j in range(8):
    S+=pow((r_i_j_[j]-0.5*N*(K+1)),2)
    #print(pow((r_i_j_[j]-0.5*N*(K+1)),2))


print("S=",S)
W = (12*S)/(pow(N,2)*(pow(K,3)-K)-N*T_j_sum)

print("կոնկորդացյիայի գործակից W=",W)
