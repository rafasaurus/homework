import binascii
import numpy as np
arr = np.array([425712,232512,112312,100012,55,5,2,212,2312,1231,123,75145,241,74324],dtype='int')
random_numbers = np.array([],dtype="double")
def mean(random_numbers):
    return np.sum(random_numbers/arr.size)
def dispersion(random_numbers):
    return mean(random_numbers**2)-mean(random_numbers)*mean(random_numbers)
for arr_i in arr:
    s = '{0:012b}'.format(arr_i)
    print((s))
    pop = 1
    coin = np.array([0,1],dtype='double')
    for str_ in s:
        #if  == 1
        k=int(str_)

        if k == 1:
            coin[0] = coin[0]+(coin[1]-coin[0]) / 2
        else:
            coin[1] = coin[1] - (coin[1]-coin[0]) / 2
        print(coin)
    random_numbers = np.append(random_numbers,coin[0])

print(random_numbers)
print(mean(random_numbers))
print(dispersion(random_numbers))