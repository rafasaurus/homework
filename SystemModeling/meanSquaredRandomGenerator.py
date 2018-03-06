import numpy as np
r0 = int('0b101010101010', 2)
r1 = int('0b11001000001', 2)
r2 = int('0b10001010001', 2)
r3 = int('0b11011000110', 2)
r4 = int('0b100000101111', 2)
r5 = int('0b1110100001011', 2)
r6 = int('0b101110100101', 2)
r7 = int('0b11001000001110001', 2)
r8 = int('0b1110101000001', 2)
r9 = int('0b11101000001010101', 2)
'''
r0 = int(bin(int(np.random.uniform(10,200))), 2)
r1 = int(bin(int(np.random.uniform(10,200))), 2)
r2 = int(bin(int(np.random.uniform(10,200))), 2)
r3 = int(bin(int(np.random.uniform(10,200))), 2)
r4 = int(bin(int(np.random.uniform(10,200))), 2)
r5 = int(bin(int(np.random.uniform(10,200))), 2)
r6 = int(bin(int(np.random.uniform(10,200))), 2)
r7 = int(bin(int(np.random.uniform(10,200))), 2)
r8 = int(bin(int(np.random.uniform(10,200))), 2)
r9 = int(bin(int(np.random.uniform(10,200))), 2)
'''




#print( binary+bin(0b101010101 << 1))
#print(bin(0b1111 << 4))
def meanSquaredGenerator(r0,r1):
    r0_str = bin(r0)
    r1_str = bin(r1)

    r0_middle = r0_str[2:10]  # string
    r1_middle = r1_str[2:10l]  # string
    #print("r0=", r0_middle)
    #print("r1=", r1_middle)
    # bin(int('0b1010', 2))
    r0_middle_int = int(r0_middle, 2)
    r1_middle_int = int(r1_middle, 2)
    #print(type(int(r0_middle, 2)))
    str_ = "0."
    for i in range(100):
        # r1_middle_int = int(bin(r0_middle_int*r1_middle_int),2)
        #pop =r0_middle_int * r1_middle_int >>4
        if i//2 ==1:
            r1_str = bin(r0_middle_int * r1_middle_int<<4)
        else:
            r1_str = bin(r0_middle_int * r1_middle_int>>4)

        # print("r1_mi=",r1_str)
        #print(r1_middle)
        r1_middle = r1_str[2:10]
        # str(r1_middle_int)
        r1_middle_int = int(r1_middle, 2)
        str_ += str(r1_middle_int)
        #print(bin(r1_middle_int))
    return str_
#print(float(meanSquaredGenerator(r0,r1)))
arr = np.array([],dtype=float)
dict = {"r0":r0,"r1":r1,"r2":r2,"r3":r3,"r4":r4,"r5":r5,"r6":r6,"r7":r7,"r8":r8,"r9":r9}

for i in range(10):
    arr = np.append(arr,float(meanSquaredGenerator(dict["r"+str(i)],dict["r1"])))
print(arr)
print("mean",np.mean(arr))
print("variance",np.var(arr))