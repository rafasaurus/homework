import re
import numpy as np

arr = np.array([8,1,9,12,15,14],dtype='int')
arr_ = np.array([58,403,157,206,318,89],dtype='int')
#mean of random nummber distribution
def mean(random_numbers):
    return np.sum(random_numbers/arr.size)
#dispersion of random number distribution
def dispersion(random_numbers):
    return mean(random_numbers**2)-mean(random_numbers)*mean(random_numbers)
#daking an array of numbers, converting it to binary,
# and spliting [0,1] range , and taking the next range according to binary

def generator(arr):
    random_numbers = np.array([], dtype="double")
    for arr_i in arr:
        s = '{0:04b}'.format(arr_i)
        print((s))
        coin = np.array([0, 1], dtype='double')
        for str_ in s:
            if k == 1:
                coin[0] = coin[0] + (coin[1] - coin[0]) / 2
            else:
                coin[1] = coin[1] - (coin[1] - coin[0]) / 2
            print(coin)
        random_numbers = np.append(random_numbers, coin[0])
    return random_numbers
#########################################################
#seccond method
# spllting an array , anc converting number from octal to decimal
def oct2int(x,counter):
    return pow(8,-1*counter)*x
def __generator__(arr):
    random_numbers = np.array([], dtype="double")
    for arr_i in arr:
        s = '{0:09b}'.format(arr_i)
        print((s))
        split =re.findall('.{1,3}', s)
        print(split)
        __number__ = "0."
        coin = np.array([0, 1], dtype='double')
        counter = 1
        integer_number = 0
        for split_i in split:
            integer_index = int(split_i, 2)
            __number__= __number__ + str(integer_index)
            #print(integer_index)
            integer_number = integer_number + oct2int(integer_index,counter)
            counter = counter + 1
        print(integer_number)
        print()
        random_numbers = np.append(random_numbers, integer_number)
    return random_numbers

random_numbers = __generator__(arr_)
print()
print(random_numbers)
print(mean(random_numbers))
print(dispersion(random_numbers))
