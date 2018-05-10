import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from congruent import get_congruent_randoms, get_exponential, get_poisson

#def get_next_exponential(N, randoms):
#    return_next_exp = np.array([])
#    for i in range(int(randoms.shape[0]/N)):
#        return_next_exp = np.append(return_next_exp, get_exponential(randoms, exponent_dist_lambda = 0.8)[i*N:i*N+N])
#    return_next_exp = return_next_exp.reshape((int(randoms.shape[0]/N), N))
#    return return_next_exp 

def get_next_exponential(N):
    randoms = get_congruent_randoms(N0=2*(1312412)+1)[:100]
    Exponent = 60 * get_exponential(randoms, exponent_dist_lambda=0.8)[:100]
    return Exponent

def get_T_input_with_poisson(N):
        T_input = np.array([])
        T_input = np.append(T_input, 0)
        Poisson = get_poisson(poisson_lambda = 6, N0=2*(1122123)+1)[:100]
        for i in range(1,Poisson.shape[0]):
            T_input = np.append(T_input, T_input[i-1]+Poisson[i]) 
        return T_input

axis = np.arange(1, 101, 1)
# plt.scatter(axis,get_exponential(randoms))

# sns.distplot(get_exponential(randoms,exponent_dist_lambda = 0.8), bins=10)
# plt.show()


N = 100 # pordzarkumneri qan
T = 600 # in minutes

Number_of_Servers = 4 # varsavir
T_wait = np.array([])
Server_State = np.array([True, True, True, True],dtype = bool)
Server_Times = np.array([0, 0, 0, 0], dtype = int)

T_Current = np.array([])
T_Free = np.array([0, 0, 0, 0])
T_input = np.array([])
N_served = np.array([])
N_rejected = np.array([])
Serve_Time = np.array([])
Queue_Length = 3 # person


# print(get_poisson(poisson_lambda = 6))
# axis = np.arange(1, get_poisson(poisson_lambda = 6).shape[0]+1,1)
# plt.scatter(axis, get_poisson(poisson_lambda = 3))
# sns.distplot(get_poisson(), bins=40)

# plt.show()

#f or i in range(100):
    # for j in range(Server_State):


T_Queue  = get_next_exponential(Number_of_Servers) # սպասարկման ժամանակ
T_Queue = np.around(T_Queue)
print("T_queue:", T_Queue)
print()
T_Serve = get_T_input_with_poisson(Number_of_Servers)
print("T_Serve:", T_Serve)

for T_Serve_i, T_Queue_i in zip(T_Serve, T_Queue):
    # check server times if they exit T = 600 limit 
    for i in range(Server_State.shape[0]):
        if Server_Times[i] >= T:
            Server_State[i] = False
            print("out of time for", i, "-th Server")
            
        if T_Queue_i > Server_Times[i]:
            Server_Times[i]+=T_Serve_i
            continue
    print("T_Serve_Timeline:", Server_Times)
    #for i in range(Server_State.shape[0]): # 4 varsavirneri state
        #if Server_State[i] == True:
            #if T_Queue_i+T_Serve_i > 
        
