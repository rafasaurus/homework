import numpy as np
from collections import OrderedDict
from congruent import get_congruent_randoms, get_exponential, get_poisson
import copy

congruent_offset = 0
__Nmodelling__=4
exponent_dist_lambda=0.8
Number_of_Servers = 4 # varsavir
Queue_Length = 3 # person
N_CLIENTS_DIST = 110# pordzarkumneri qan
T = 600 # in minutes
class SlicableDict(OrderedDict):
    def __getitem__(self, key):
        if isinstance(key, slice):
            # Unmangle `__root` to access the doubly linked list
            root = getattr(self, "_OrderedDict__root")
            # By default, make `start` as the first element, `end` as the last
            start, end = root[1][2], root[0][2]
            start = key.start or start
            end = key.stop or end
            step = key.step or 1
            curr, result, begun, counter = root[1], [], False, 0

            # Begin iterating
            curr, result, begun = root[1], [], False
            while curr is not root:
                # If the end value is reached, `break` and `return`
                if curr[2] == end:
                    break
                # If starting value is matched, start appending to `result`
                if curr[2] == start:
                    begun = True
                if begun:
                    if counter % step == 0:
                        result.append((curr[2], self[curr[2]]))
                    counter += 1

                # Make the `curr` point to the next element
                curr = curr[1]

            return result

        return super(SlicableDict, self).__getitem__(key)

def get_next_exponential(N):
    randoms = get_congruent_randoms(N0=congruent_offset*2*(1312412)+1)[:N_CLIENTS_DIST]
    Exponent = 60 * get_exponential(randoms, exponent_dist_lambda)[:N_CLIENTS_DIST]
    return Exponent
def get_T_input_with_poisson(N):
    global congruent_offset
    T_input = np.array([])
    T_input = np.append(T_input, 0)
    Poisson = get_poisson(poisson_lambda = 6, N0=congruent_offset*2*(1022123)+1)[:N_CLIENTS_DIST]
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
Model_Served_N = np.array([])
Model_Rejected_N = np.array([])
Model_First_Server_Time = np.array([])

for i in range(__Nmodelling__):
    T_Serve_Time = get_next_exponential(Number_of_Servers)
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
    T_Serve = get_T_input_with_poisson(Number_of_Servers)
    # **** print distributions ****
    print("******T_Serve******:\n", T_Serve)
    print("******T_Serve_Time******:\n", T_Serve_Time)
    print()
    index = 0
    Served_Objects = np.array([])
    Served_Objects_Time = np.array([])
    Server_Time_Dict = {
            "server_index":0,
            "time":0
            }
    Server_Time_Dict_arr = np.array([])
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
        First_Server_Time = np.array([]) 
        # if there is a queue
        if arr_Queue_dict.shape[0] > 0:
            # serve queue clients
            # cycle through all of queue clients
            boolean = True
            for arr_Queue_dict_i in arr_Queue_dict:
                if T_Serve_j >= Server_Times[arr_Queue_dict_i["server_index"]] and boolean:
                    Server_Times[arr_Queue_dict_i["server_index"]] += T_Serve_Time[arr_Queue_dict_i["queue_index"]]
                    Served_Objects = np.append(Served_Objects, arr_Queue_dict_i["queue_index"])
                    Served_Objects_Time = np.append(Served_Objects_Time, T_Serve_Time[arr_Queue_dict_i["queue_index"]])

                    arr_Queue_dict = arr_Queue_dict[1:]
                    if arr_Queue_dict_i["server_index"] == 0:
                        First_Server_Time = np.append(First_Server_Time,T_Serve_Time[arr_Queue_dict_i["queue_index"]])
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
        # Server_Time_Dict_arr = SlicableDict(Server_Time_Dict_arr[:])
        Model_First_Server_Time = np.append(Model_First_Server_Time, First_Server_Time)
        if T_Serve_Time_j >= T:
            break

    # print("\nServed_Objects:", Served_Objects)
    # print("Rejected_Objects:", Rejected_Objects)
    # print("Nnum_Served:", Served_Objects.shape[0])
    # print("Nnum_Rejected:", Rejected_Objects.shape[0])
    # print("total:", Rejected_Objects.shape[0]+Served_Objects.shape[0])
    # print("final_index:", index)
    Model_Rejected_N = np.append(Model_Rejected_N, Rejected_Objects.shape[0])
    Model_Served_N = np.append(Model_Served_N, Served_Objects.shape[0])

print("debug:", Model_First_Server_Time) 
P_SERVE_MEAN = np.mean(Model_Served_N) # model serve mean
P_SERVE_STD = np.std(Model_Served_N)
T_TABLE = 1.98
T_COMPUTED = (P_SERVE_MEAN-6)/P_SERVE_STD*pow(__Nmodelling__, 1/2)
if abs(T_COMPUTED) < T_TABLE:
    print("MODEL@ HAMARJEQ E")
MODEL_SERVE_PROBABILITY = np.sum(Model_Served_N)/(np.sum(Model_Served_N)+np.sum(Model_Rejected_N))
MODEL_SERVE_MEAN_TIME = np.mean(Served_Objects_Time)
SYSTEM_BANDWITH = P_SERVE_MEAN/MODEL_SERVE_MEAN_TIME# hamakargi toxunakutyun
print("Model_Served_N:", Model_Served_N)
print("Model_Rejected_N:", Model_Rejected_N)
print("P_SERVE_MEAN:", P_SERVE_MEAN)
print("T_COMPUTED:", T_COMPUTED)
print("MODEL_SERVE_PROBABILITY:", MODEL_SERVE_PROBABILITY)
print("MODEL_SERVE_MEAN_TIME:", MODEL_SERVE_MEAN_TIME)
print("SYSTEM_BANDWITH:", SYSTEM_BANDWITH)

'''
spasrkam hav
merjman
hamakargi toxunakutyun  = ichqan hayta spasarkvel / spasparkvacneri jamanaki vra
mek kapuxu zbaxvacutyan= havanakanutyun kapucu zbaxvacutyun /T
mek kapuxu parapurdi havanakanutyun 
spasarkman mijin jamanak
hertum hayeri spasman mijin janmanak
student
'''
