import numpy as np
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


T_Serve_Time  = get_next_exponential(Number_of_Servers) #
T_Serve_Time = np.around(T_Serve_Time)
Queue = np.array([],dtype = "int")
Queue_Serve_Time = np.array([])

print("T_Serve_Time:", T_Serve_Time)
print()
T_Serve = get_T_input_with_poisson(Number_of_Servers)
T_Serve *=2
print("T_Serve:", T_Serve)

Served_Objects = np.array([])
Rejected_Objects = np.array([])
index = 0

for T_Serve_j, T_Serve_Time_j in zip(T_Serve, T_Serve_Time):
    # check server times if they exit T = 600 limit 
    Reject_boolean_checker = True
    Queue_boolean_checker = True
    print("server_times:", Server_Times)
    print("Queue:", Queue) 
    print("Served_Objects:",Served_Objects)
    if Queue.shape[0] > 0:
        print("***********************")
        min_Server_Times = min(Server_Times)
        min_Server_Times_index = np.argmin(Server_Times)
        if (min_Server_Times + T_Serve_Time[Queue[0]]) <=T:
            Server_Times[min_Server_Times_index] += T_Serve_Time[Queue[0]]
            Served_Objects = np.append(Served_Objects, Queue[0])
            Queue = Queue[1:]
            Queue = np.append(Queue, index)
        if T_Serve_Time[Queue[0]]+min_Server_Times > T:
            break
    else:
        min_Server_Times = min(Server_Times)
        min_Server_Times_index = np.argmin(Server_Times)
        if (T_Serve_j+T_Serve_Time_j) <=T:
            if T_Serve_j > min_Server_Times and Queue.shape == 0:
                # Queue_boolean_checker = False
                Server_Times[min_Server_Times_index] += T_Serve_Time[index]
                Served_Objects = np.append(Served_Objects, index)
            elif Queue.shape[0]<3:
                Queue = np.append(Queue, index)
        else:
            Rejected_Objects = np.append(Rejected_Objects, index)
    index+=1
        #for i in range(Number_of_Servers):
        #    #if Server_Times[i] >= T:
        #    #    Server_State[i] = False
        #    #    print("out of time for", i, "-th Server")
        #    if T_Serve_j > Server_Times[i] and T_Serve_Time_j+Server_Times[i] <= T:
        #        Queue_boolean_checker = False
        #        Served_Objects = np.append(Served_Objects, index)
        #        Server_Times[i]+=T_Serve_Time_j
        #        break
        #    #print("T_Serve_Timeline:", Server_Times)
        #if Reject_boolean_checker:
        #               **********************************************************************************************
        #if Queue_boolean_checker == False and Queue.shape[0]<3:
        #    Queue = np.append(Queue, index)
        #for i in range(Server_State.shape[0]): # 4 varsavirneri state
            #if Server_State[i] == True:
                #if T_Serve_Time_i+T_Serve_i > 
print("\nServed_Objects:", Served_Objects) 
print("Rejected_Objects:", Rejected_Objects)
