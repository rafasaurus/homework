import numpy as np
from congruent import get_congruent_randoms, get_exponential, get_poisson
import copy

congruent_offset = 0
__Nmodelling__=2
exponent_dist_lambda=0.8

N = 100 # pordzarkumneri qan
T = 600 # in minutes

Number_of_Servers = 3 # varsavir
Queue_Length = 3 # person

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

# axis = np.arange(1, 101, 1)
# plt.scatter(axis,get_exponential(randoms))
# sns.distplot(get_exponential(randoms,exponent_dist_lambda = 0.8), bins=10)
# plt.show()

# print(get_poisson(poisson_lambda = 6))
# axis = np.arange(1, get_poisson(poisson_lambda = 6).shape[0]+1,1)
# plt.scatter(axis, get_poisson(poisson_lambda = 3))
# sns.distplot(get_poisson(), bins=40)
# plt.show()

T_Serve_Time_ = get_next_exponential(Number_of_Servers)
for i in range(__Nmodelling__):
    T_Serve_Time = T_Serve_Time_# get_next_exponential(Number_of_Servers)
    # T_Serve_Time /=2
    T_Serve_Time = np.around(T_Serve_Time)
    # Queue = np.array([], dtype="int")
    # Queue_Serve_Time = np.array([])
    Queue_dict = {
                     "queue_index": 0,
                     "server_index": 0
                 }
    arr_Queue_dict = np.array([])
    # arr_Queue_dict = np.append(arr_Queue_dict, Queue_dict)
    print("******T_Serve_Time******:\n", T_Serve_Time)
    print()
    T_Serve = get_T_input_with_poisson(Number_of_Servers)
    print("******T_Serve******:\n", T_Serve)
    index = 0
    Served_Objects = np.array([])
    Rejected_Objects = np.array([])
    Server_Times = np.zeros(Number_of_Servers)
    for T_Serve_j, T_Serve_Time_j in zip(T_Serve, T_Serve_Time):
        # print("\tindex:", index)
        # print("\tnext_Serve_time_j:", T_Serve_Time_j)
        # print("\tnext_T_Serve_j:", T_Serve_j)
        # print("\tserver_times:", Server_Times)
        # print("\t****Queue****\n:", arr_Queue_dict)
        # print("\tServed_Objects:", Served_Objects)
        # print("\tRejected_Objects:", Rejected_Objects)
        
        # if there is a queue
        if arr_Queue_dict.shape[0] > 0:
            # serve queue clients
            # cycle through all of queue clients
            boolean = True
            for arr_Queue_dict_i in arr_Queue_dict:
                if T_Serve_j >= Server_Times[arr_Queue_dict_i["server_index"]] and boolean:
                    Server_Times[arr_Queue_dict_i["server_index"]] += T_Serve_Time[arr_Queue_dict_i["queue_index"]]
                    Served_Objects = np.append(Served_Objects, arr_Queue_dict_i["queue_index"])
                    arr_Queue_dict = arr_Queue_dict[1:]
                else:
                    boolean = False

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
                                            "queue_index": index,
                                            "server_index": min_Server_Times_index
                                         }
                            arr_Queue_dict = np.append(arr_Queue_dict, Queue_dict)
                        else:
                            Rejected_Objects = np.append(Rejected_Objects, index)
            # if there's queue left
            else:
                min_Server_Times = min(Server_Times)
                min_Server_Times_index = np.argmin(Server_Times)
                if min_Server_Times + T_Serve_Time_j <=T and arr_Queue_dict.shape[0]<Queue_Length:
                    Queue_dict = {
                                    "queue_index": index,
                                    "server_index": min_Server_Times_index
                                 }
                    arr_Queue_dict = np.append(arr_Queue_dict, Queue_dict)
                else:
                    Rejected_Objects = np.append(Rejected_Objects, index)
           
        # if there is not a queue*******global else*******
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
    print("final_index:", index)
