import numpy as np
'''T4y 0akan syuneri qanakna ֆորմալ անջատված տարերի քանակ'''

np.set_printoptions(threshold=1000)

arr = np.zeros(shape=(19,19),dtype=int)
compareZeroMatrix = np.zeros(shape=(19,19),dtype=int)
zeros=arr
#x = np.array([1, 1, 2, 2, 3, 4, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 16, 17, 18, 19], np.float)
m=19 # ընդհանուր տարերի թիվը
x = np.array([1, 1,  2,  2,  3,  3, 4,  4, 5,  6, 7,  8, 9, 10,11,12, 12, 13, 14, 15, 16,16,17,18,19], np.int)
y = np.array([8, 11, 13, 12, 16, 5, 14, 6, 15, 7, 19, 9, 0, 9, 19, 7, 10, 16, 18, 14, 17, 0, 0, 0, 0], np.int)# 24 elements
x_temp=9
y_temp=0
r=0# գրաֆում միավոր կապերի թիվն է
for i in range(25):
    if (y[i]!=0):
        r+=1
print("գրաֆում միավոր կապերի թիվն` r=",  r)
for i in range(19):
    for j in range(19):
        for k in range(25):
            if y[k]-1 !=0 and y[k]!=0:
                #if ((int(y[k]-1)==19 and int(x[k])-1)==19):
                arr[int(x[k])-1][int(y[k]-1)]=1




compareZeroVector = np.zeros(shape=(19),dtype=int)

T1 = []
print("compareZeroVector=",compareZeroVector)
print(" eg  = ",arr[:,0])
T4=0
for j in range(19):
    if(arr[:,j].any()==compareZeroVector.any()):
        #print(j+1)
        T1.append(j+1)
        T4+=1
print("T1=",T1)

T3 = []
for i in range(25):
    thereIs=False
    if(y[i]==0):
        T3.append(x[i])

print("T3=",T3)


T2 = []
for i in range(25):
    thereIs = False
    for j in range(25):
        local_bool = False
        if (x[i]==y[j]):
            thereIs=True


    if (thereIs):
        thereIsNotInT3 = True
        for q in range(T3.__len__()):
            if (x[i]==T3[q]):
                for k in range(25):
                    if (x[k]==T3[q] and y[k]==0):
                        thereIsNotInT3 =False
                    else:
                        thereIsNotInT3 = True
        if (thereIsNotInT3):
            T2.append(x[i])

#deleting dublicates in T2
T2_1=[]
for i in T2:
    if i not in T2_1:
        T2_1.append(i)
T2=T2_1

print("T2=",T2)
print("ֆորմալ անջատված տարերի քանակ T4=",T4)

T5=0
for i in range(25):
    for j in range(i+1,25):
        if (x[i]==x[j] and y[j]!=0):
            local_bool=True
            for T1_i in T1:
                if(x[j]==T1_i):
                    local_bool=False
                    break
            if(local_bool):
                T5+=1
print("նեքին կապերի թիվը T5=",T5)

T6=0
for i in range(25):
    for j in range(i+1,25):
        if (x[i]==x[j] and y[j]==0):
            local_bool=True
            for T1_i in T1:
                if(x[j]==T1_i):
                    local_bool=False
                    break
            if(local_bool):
                T6+=1
print("ելքային կապերի միջև տարրերի կապերի թիվը T6=",T6)

k_m=T2.__len__()/m
print("միջանկյալ տարերի գործակիցը k_m=",k_m)# իչքան մոտ է ին այնքան համակարգը բարդ է
k_n_k =T5/r
print("նեռքին կապակցվածության գործակիցը k_n_k=",k_n_k)# որքան մոտ է 1 ին այնքան ներքին կապակցվածության աստիճանը բարձռ է
k_4=2*T6/(T3.__len__()*(T3.__len__()-1))
print("ինֆորմացիայի ավելցուկային աստիճանը k_4=",k_4)# որքան մոտ է 0ին նշանակում է համակարգում ելքային տարրերի միջև ինֆորմացիայի ավելցուկը քիչ է
#first matrix A^1
print("----- 0 տակտի մատրից-----")

print(arr)
print()

global_arr = np.zeros(shape=(19,19),dtype=int)
global_arr = arr.copy()
matrix_sum = np.zeros(shape=(19,19),dtype=int)
N = 0
while(np.array_equal(global_arr,compareZeroMatrix)==False):
    matrix_sum += global_arr
    global_arr=np.matmul(global_arr,arr)
    N += 1
    #print("n=", N)
    #print("boolean check = ", np.array_equal(global_arr,compareZeroMatrix))
    #print(global_arr )

print("մատրիցի աստիճանը՝ N=",N)
T7=T4-1
print("հաջորդ մատրիցնեռում ֆորմալ անջատվող տարրերի քանակը արաջին կարգի մատրիցի համար T7=",T7)# այն սյուննեռը վորոնք ամբողջովին 0 են
print("-----հասանելիության մատրից-----")