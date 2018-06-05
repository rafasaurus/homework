import numpy as np
from collections import OrderedDict
import copy

congruent_offset = 0
__Nmodelling__= 100
exponent_dist_lambda=0.8
Number_of_Servers = 4 # varsavir
Queue_Length = 3 # person
N_CLIENTS_DIST = 110# pordzarkumneri qan
T = 600 # in minutes


def get_congruent_randoms(N0=2923121):
   #congruent params
    t = 2
    __lambda__ = 8*t+3
    k = 14 
    m = pow(2, k)
    last_n_mixed = N0
    miu = 10  #  for mixed version
    randoms_mixed = np.array([]) #
    for i in range(pow(2, k-2)):
        n_mixed = (last_n_mixed * __lambda__ + miu) % m
        last_n_mixed = n_mixed
        randoms_mixed = np.append(randoms_mixed, n_mixed/m)
    return randoms_mixed

def get_exponential(randoms, exponent_dist_lambda = 0.8):
    exponent_dist = (-1/exponent_dist_lambda) * np.log(randoms)
    return exponent_dist

def get_poisson(poisson_lambda = 3, N0=2923121):
    t = 2
    __lambda__ = 8*t+3
    k = 14 
    m = pow(2, k)
    last_n_mixed = N0
    miu = 10  #  for mixed version
    poisson_randoms = np.array([])
    randoms_mixed = np.array([]) #
    S = 1
    J = 0
    for i in range(pow(2, k-2)):
        n_mixed = (last_n_mixed * __lambda__ + miu) % m
        last_n_mixed = n_mixed
        randoms_mixed = np.append(randoms_mixed, n_mixed/m)
        r = n_mixed/m
        S = S * r
        if S < np.exp(-poisson_lambda):
            poisson_randoms = np.append(poisson_randoms, J)    
            J = 0
            S = 1
        else:
            J = J+1
    return poisson_randoms

def get_next_exponential(N):
    randoms = get_congruent_randoms(N0=congruent_offset*2*(1312412)+1)[:N_CLIENTS_DIST]
    Exponent = 60 * get_exponential(randoms, exponent_dist_lambda)[:N_CLIENTS_DIST]
    return Exponent

def get_T_input_with_poisson(N):
    global congruent_offset
    T_input = np.array([])
    T_input = np.append(T_input, 0)
    Poisson = get_poisson(poisson_lambda = 6, N0=congruent_offset*2*(1022123)+1)[:N_CLIENTS_DIST]
    for i in range(1,Poisson.shape[0]):
        T_input = np.append(T_input, T_input[i-1]+Poisson[i]) 
    congruent_offset += 1
    return T_input

Model_Served_N = np.array([])
Model_Rejected_N = np.array([])
Model_First_Server_Time = np.array([])
First_Server_Time = np.array([]) 
Seccond_Server_Time = np.array([])
Queue_Wait_Time = np.array([])
for i in range(__Nmodelling__):
    T_Serve_Time = get_next_exponential(Number_of_Servers)
    T_Serve_Time = np.around(T_Serve_Time)
    arr_Queue_dict = np.array([])
    T_Serve = get_T_input_with_poisson(Number_of_Servers)
    # **** print distributions for debug ****
    # print("******T_Serve******:\n", T_Serve)
    # print("******T_Serve_Time******:\n", T_Serve_Time)
    # print()
    index = 0
    Served_Objects = np.array([])
    Served_Objects_Time = np.array([])
    Server_Time_Dict_arr = np.array([])
    Rejected_Objects = np.array([])
    Server_Times = np.zeros(Number_of_Servers)
    for T_Serve_j, T_Serve_Time_j in zip(T_Serve, T_Serve_Time):
        # **print to debug**
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
                    Queue_Wait_Time = np.append(Queue_Wait_Time, Server_Times[arr_Queue_dict_i["server_index"]]-T_Serve[arr_Queue_dict_i["queue_index"]])
                    Server_Times[arr_Queue_dict_i["server_index"]] += T_Serve_Time[arr_Queue_dict_i["queue_index"]]
                    Served_Objects = np.append(Served_Objects, arr_Queue_dict_i["queue_index"])
                    Served_Objects_Time = np.append(Served_Objects_Time, T_Serve_Time[arr_Queue_dict_i["queue_index"]])
                    arr_Queue_dict = arr_Queue_dict[1:]
                    if arr_Queue_dict_i["server_index"] == 0:
                        First_Server_Time = np.append(First_Server_Time,T_Serve_Time[arr_Queue_dict_i["queue_index"]])
                    if arr_Queue_dict_i["server_index"] == 1:
                        Seccond_Server_Time = np.append(Seccond_Server_Time, T_Serve_Time[arr_Queue_dict_i["queue_index"]])
                else:
                    boolean = False

            # serve next client T_SERVE_J
            # if there's no queue left
            if arr_Queue_dict.shape[0] == 0:
                for k in range(Number_of_Servers):
                    if T_Serve_j >= Server_Times[k] and T_Serve_j + T_Serve_Time_j <=T:
                        Server_Times[k] = T_Serve_j + T_Serve_Time_j
                        Served_Objects = np.append(Served_Objects, index)
                        Served_Objects_Time = np.append(Served_Objects_Time, T_Serve_Time_j)
                        if k==0:
                            First_Server_Time = np.append(First_Server_Time, T_Serve_Time_j)
                        if k==1:
                            Seccond_Server_Time = np.append(Seccond_Server_Time, T_Serve_Time_j)
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
                    Served_Objects_Time = np.append(Served_Objects_Time, T_Serve_Time_j)
                    if k==0:
                        First_Server_Time = np.append(First_Server_Time, T_Serve_Time_j)
                    if k==1:
                        Seccond_Server_Time = np.append(Seccond_Server_Time, T_Serve_Time_j)
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
        if T_Serve_Time_j >= T:
            break

    Model_Rejected_N = np.append(Model_Rejected_N, Rejected_Objects.shape[0])
    Model_Served_N = np.append(Model_Served_N, Served_Objects.shape[0])
P_SERVE_MEAN = np.mean(Model_Served_N)# model serve mean
P_SERVE_STD = np.std(Model_Served_N)
T_TABLE = 1.98
# ***** STUDENT PRECISION *****
T_COMPUTED = (P_SERVE_MEAN-30)/P_SERVE_STD*pow(__Nmodelling__, 1/2)
print(" ***** MODELLING PARAMS\tT=", T," MODELLING TIMES_N=", __Nmodelling__, " NUMBER OF SERVERS=", Number_of_Servers, " *****")
if abs(T_COMPUTED) < T_TABLE:
    print("\t\t\tSTUDENT MODEL EVALUATON --- MODEL is evaled\n")
MODEL_SERVE_PROBABILITY = np.sum(Model_Served_N)/(np.sum(Model_Served_N)+np.sum(Model_Rejected_N))
MODEL_SERVE_MEAN_TIME = np.mean(Served_Objects_Time)
SYSTEM_BANDWITH = P_SERVE_MEAN/MODEL_SERVE_MEAN_TIME# hamakargi toxunakutyun
# **for debug**
# print("Model_Served_N:", Model_Served_N)
# print("Model_Rejected_N:", Model_Rejected_N)
# print("P_SERVE_MEAN:", P_SERVE_MEAN)
# print("T_COMPUTED:", T_COMPUTED)
print("MODEL_SERVE_PROBABILITY:", MODEL_SERVE_PROBABILITY)
print("MODEL_SERVE_MEAN_TIME:", MODEL_SERVE_MEAN_TIME)
print("SYSTEM_BANDWITH:", SYSTEM_BANDWITH)
print("First Server busy time:", np.sum(First_Server_Time)/(T*__Nmodelling__))
print("Seccond Server IDLE time:", 1-np.sum(Seccond_Server_Time/(T*__Nmodelling__)))
print("MODEL_SERVE_MEAN_TIME:", MODEL_SERVE_MEAN_TIME)# spasarkman mijin jamanak
print("Queue_Wait_Time_MEAN:", np.mean(Queue_Wait_Time))
'''
spasrkam hav
merjman
hamakargi toxunakutyun  = ichqan hayta spasarkvel / spasparkvacneri jamanaki vra
mek kapuxu zbaxvacutyan havanakanutyun = kapucu zbaxvacutyun /T
mek kapuxu parapurdi havanakanutyun 

spasarkman mijin jamanak
hertum hayeri spasman mijin janmanak
student
'''
