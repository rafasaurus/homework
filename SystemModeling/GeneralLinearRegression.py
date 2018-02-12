import numpy as np

def mean(arr,n):
    s=0
    for i in range(n):
        s+=arr[i]
    return s/n

def sp(arr, n):
    s = 0
    for k in range(n):
        s += arr[k][k]
    return s

def nullfinder(pop, n):
    val_ = True
    for o in range(n):
        for p in range(n):
            if pop[o][p] != 0:
                val_ = False
                break
    return val_

def COMPUTE_REGRESSION_X(muffin, featureRows, featurSize, n): # featureRows =2 featureSize=5
    x = np.zeros(shape=(n, n))
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                x[i][i] = featureSize
            elif j == 0 and i >= 1:#
                x[i][j] = sumX(muffin[i - 1], featureSize)
            elif i == 0 and j >= 1:
                x[i][j] = sumX(muffin[j-1], featureSize)
            #elif i > 0 and j > 0:
            else:
                x[i][j] = sumXY(muffin[i-1], muffin[j-1], featureSize)
    return x

def sumXY(arr1,arr2,n):
    sum_ = 0
    for i in range(n):
        sum_ += arr1[i]*arr2[i]
    return sum_

def sumX(arr, n):
    sum_ = 0
    for i in range(n):
        sum_ += arr[i]
    return sum_

def COMPUTE_REGRESSION_Y_EX(yp, x1, x2, n):  # stands for experimental
    y = np.zeros(3, dtype=float)
    for i in range(n):
        y[0] += yp[i]
        y[1] += yp[i] * x1[i]
        y[2] += yp[i] * x2[i]
    return y

def INVERSE_MATRIX(arr, n):
    E = np.matrix(np.identity(n))
    E = np.array(E)
    print_val = -10
    temp_arr = np.matrix(n, dtype=float)
    temp_arr = np.array(temp_arr)
    static_arr = arr
    Bn = arr
    for i in range(n):
        P = sp(arr, n) / (i + 1)
        if i == n - 1:
            print_val = Bn / P
            print("debug")
        Bn = arr - (P * E)
        arr = np.matmul(static_arr, Bn)
        if nullfinder(arr, n):
            print("the end")
            break
    return print_val

#
#-------program-------
n = 4
k = 2 #the number of regression features --- ազատության աստիճան
k += 1

featureSize = 5
featureRows = 2

muffin = np.zeros(shape=(k, featureSize))
print("muffin=", muffin)
arr = np.zeros(shape=(4, 4))
muffin[0] = np.array([2, 1, 1, 2, 1], np.float)
muffin[1] = np.array([3, 1, 2, 1, 2], np.float)
yp = np.array([1, 1, 3, 2, 1], np.float)


arr = COMPUTE_REGRESSION_X(muffin, featureRows, featureSize, k)
print(arr)
vector = COMPUTE_REGRESSION_Y_EX(yp, muffin[0], muffin[1], featureSize)
print("arr=", arr)
inverse_arr = INVERSE_MATRIX(arr, 3)
print("vector=\n", vector)
print(B)
# հաշվարկային y_final
y_final = np.zeros(shape=(5,1))
for i in range(featureSize):
    y_final[i]=B[0]+B[1]*muffin[0][i]+B[2]*muffin[1][i]
    #print(y_final[i])

#ռեգրեսիայով պայմանավորված միջին քառակուսային շեղումներ
y_final_mean = mean(y_final,featureSize)
SSR=0
for i in range(n):
    SSR+=(y_final[i]-y_final_mean)*(y_final[i]-y_final_mean)
print("ռեգռեսիայով պայմանավորված միջին քառակուսային շեղումներ = ",SSR)

#միջին քառակուսային շեղումներ
SSO = 0
yp_mean = mean(yp, featureSize)
for i in range(featureSize):
    SSO += (yp[i]-yp_mean)*(yp[i]-yp_mean)
print("SS0  միջին քառակուսային շեղումներ = ", SSO)

#անհամաձայնեցումներով պայմանավորված միջին քառակուսային շեղումներ
SSE = 0
#
for i in range(featureSize):
    SSE+=(y_final[i] - yp[i])*(y_final[i] - yp[i])
print("SSE  անհամաձայնեցումներով պայմանավորված միջին քառակուսային շեղումներ = ",SSE)

#ռեգռեսիայով պայմանավորված դիսպերսիան
MSR = SSR/k
print("MSR  ռեգռեսիայով պայմանավորված դիսպերսիան = ",MSR)

#մնացորդային դիսպերսիայի վիճակագրական գնահատական, ազատության աստիճանը n-k-1
sigmaSquared = SSE/(featureSize-k-1)
print("SIGMASQUARED  մնացորդային դիսպերսիայի վիճակագրական գնահատականը = ",sigmaSquared)

#դետերմինացված գործակից
RSquared = SSR/SSO
print("RSQUARED  դետերմինացված գործակից = ", RSquared)

#ֆիշերի չափանիշ
F = MSR/sigmaSquared
print("ֆիշերի = ",F)
