import numpy as np
from congruent import get_congruent_randoms, get_exponential, get_poisson
import copy
congruent_offset = 0
__Nmodelling__=1
exponent_dist_lambda=0.8
#def get_next_exponential(N, randoms):
#    return_next_exp = np.array([])
#    for i in range(int(randoms.shape[0]/N)):
#        return_next_exp = np.append(return_next_exp, get_exponential(randoms, exponent_dist_lambda = 0.8)[i*N:i*N+N])
#    return_next_exp = return_next_exp.reshape((int(randoms.shape[0]/N), N))
#    return return_next_exp 

def get_next_exponential(N):
    randoms = get_congruent_randoms(N0=congruent_offset*2*(1312412)+1)[:100]
    Exponent = 60 * get_exponential(randoms, exponent_dist_lambda)[:100]
    return Exponent
def get_T_input_with_poisson(N):
    global congruent_offset
    T_input = np.array([])
    T_input = np.append(T_input, 0)
    Poisson = get_poisson(poisson_lambda = 6, N0=2*(1022123)+1)[:100]
    # Poisson = get_poisson(poisson_lambda=6, N0=congruent_offset*(1022123)+1)[:100]
    for i in range(1,Poisson.shape[0]):
        T_input = np.append(T_input, T_input[i-1]+Poisson[i]) 
    congruent_offset += 1
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

for i in range(__Nmodelling__):
    T_Serve_Time  = get_next_exponential(Number_of_Servers) #
    # T_Serve_Time /=2
    T_Serve_Time = np.around(T_Serve_Time)
    Queue = np.array([],dtype = "int")
    Queue_Serve_Time = np.array([])
    Queue_dict = {
                            "queue_index":0,
                            "server_index":0
                          }
    arr_Queue_dict = np.array([])
    # arr_Queue_dict = np.append(arr_Queue_dict, Queue_dict)
    print("T_Serve_Time:", T_Serve_Time)
    print()
    T_Serve = get_T_input_with_poisson(Number_of_Servers)
    print("T_Serve:", T_Serve)
    
    Served_Objects = np.array([])
    Rejected_Objects = np.array([])
    index = 0
    
    for T_Serve_j, T_Serve_Time_j in zip(T_Serve, T_Serve_Time):
        # check server times if they exit T = 600 limit 
        print("\tindex:", index)
        print("\tnext_Serve_time_j:", T_Serve_Time_j)
        print("\tnext_T_Serve_j:", T_Serve_j)
        print("\tserver_times:", Server_Times)
        print("\tQueue:", arr_Queue_dict)
        print("\tServed_Objects:",Served_Objects)
        print("\tRejected_Objects:", Rejected_Objects)
        if arr_Queue_dict.shape[0] > 0:
            temp_arr_Queue_dict = arr_Queue_dict.copy()
            for arr_Queue_dict_i in temp_arr_Queue_dict:
                if T_Serve_j >= Server_Times[arr_Queue_dict_i["server_index"]]:
                    Server_Times[arr_Queue_dict_i["server_index"]] += T_Serve_Time[arr_Queue_dict_i["queue_index"]]
                    Served_Objects = np.append(Served_Objects, arr_Queue_dict_i["queue_index"])
                    arr_Queue_dict = arr_Queue_dict[1:]

            
            # serve next client T_SERVE_J
            # if there's no queue left
            if arr_Queue_dict.shape[0] == 0:
                for k in range(Number_of_Servers):
                    if T_Serve_j >= Server_Times[k] and T_Serve_j + T_Serve_Time_j <=T:
                        Server_Times[k] = T_Serve_j + T_Serve_Time_j
                        Served_Objects = np.append(Served_Objects, index)
                        break
                    elif k==Number_of_Servers-1:
                        min_Server_Times = min(Server_Times)
                        min_Server_Times_index = np.argmin(Server_Times)
                        if min_Server_Times + T_Serve_Time_j <=T and arr_Queue_dict.shape[0]<Queue_Length:
                            Queue_dict = {
                                    "queue_index":index,
                                    "server_index":min_Server_Times_index
                                  }
                            arr_Queue_dict = np.append(arr_Queue_dict, Queue_dict)
                        else:
                            Rejected_Objects = np.append(Rejected_Objects, index)
            # if there's queue left
            # else:
            #     print("**************************debug***********************************************")
            #     min_Server_Times = min(Server_Times)
            #     min_Server_Times_index = np.argmin(Server_Times)
            #     if min_Server_Times + T_Serve_Time_j <=T and arr_Queue_dict.shape[0]<Queue_Length:
            #         Queue_dict = {
            #                 "queue_index":index,
            #                 "server_index":min_Server_Times_index
            #               }
            #         arr_Queue_dict = np.append(arr_Queue_dict, Queue_dict)
            #     else:
            #         Rejected_Objects = np.append(Rejected_Objects, index)
            
        # *******global else*******
        else:
            for k in range(Number_of_Servers):
                if T_Serve_j >= Server_Times[k] and T_Serve_j + T_Serve_Time_j <=T:
                    Server_Times[k] = T_Serve_j + T_Serve_Time_j
                    Served_Objects = np.append(Served_Objects, index)
                    break
                elif k==Number_of_Servers-1:
                    min_Server_Times = min(Server_Times)
                    min_Server_Times_index = np.argmin(Server_Times)
                    if min_Server_Times + T_Serve_Time_j <=T:
                        Queue_dict = {
                                "queue_index":index,
                                "server_index":min_Server_Times_index
                              }
                        arr_Queue_dict = np.append(arr_Queue_dict, Queue_dict)
                    else:
                        Rejected_Objects = np.append(Rejected_Objects, index)
        index+=1
    print("\nServed_Objects:", Served_Objects) 
    print("Rejected_Objects:", Rejected_Objects)
    print("Nnum_Served:", Served_Objects.shape[0])
    print("Nnum_Rejected:", Rejected_Objects.shape[0])
    print("total:", Rejected_Objects.shape[0]+Served_Objects.shape[0])
