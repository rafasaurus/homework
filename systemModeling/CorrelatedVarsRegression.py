import numpy as np

def correlation(arr1,arr2, n):
    sum = 0
    for i in range(n):
        sum += arr1[i] * arr2[i]
    return (sum / (n - 1))

def sigmaHat(arr, n):
    arr_mean = mean(arr, n)
    sum=0
    for i in range(n):
        sum+=((arr_mean-arr[i])*(arr_mean-arr[i]))

    return np.sqrt(sum/(n-1))
def xDotFunc(arr, n, sigmaHatVar):

    arr_mean = mean(arr, n)

    for i in range(n):
        arr[i] = (arr[i]-arr_mean)/sigmaHatVar
    return arr

def mean(arr,n):
    s=0
    for i in range(n):
        s+=arr[i]
    return s/n

def nullfinder(pop, n):
    val_ = True
    for o in range(n):
        for p in range(n):
            if pop[o][p] != 0:
                val_ = False
                break
    return val_

def sp(arr, n):
    s = 0
    for k in range(n):
        s += arr[k][k]
    return s


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

k=2#feature mount
featureSize=20
x = np.zeros(shape=(k, featureSize))
print("muffin=", x)

x[0] = np.array([2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 3, 1, 1, 2, 1, 2, 1, 2, 2, 2], np.float)
x[1] = np.array([2, 2, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1], np.float)
yp = np.array([3, 1, 1, 2, 1, 1, 1, 1, 2, 1 ,2, 1, 2, 2, 2, 2, 1, 1, 1, 1], np.float) # y_pordznakan

yp_mean = mean(yp, featureSize)
print(yp_mean)
x0_mean = mean(x[0],featureSize)
print(x0_mean)
x1_mean = mean(x[1],featureSize)
print(x1_mean)
sigma0= sigmaHat(yp, featureSize)
sigma1= sigmaHat(x[0], featureSize)
sigma2= sigmaHat(x[1], featureSize)
print("sigma0 = " , sigmaHat(yp, featureSize))
print("sigma1 = " , sigmaHat(x[0], featureSize))
print("sigma2 = " , sigmaHat(x[1], featureSize))
#calculation of dot variables
xDot = np.zeros(shape=(k,featureSize))
xDot[0] = xDotFunc(x[0],featureSize,sigma1)
print(xDot[0])
xDot[1] = xDotFunc(x[1],featureSize,sigma2)
print(xDot[1])
yDot = np.zeros(shape=(1,featureSize))
yDot = xDotFunc(yp, featureSize, sigma0)
print("yDot",yDot)


R0 = np.zeros(shape=(k,1))
##compute correlation
#sum = 0
#for i in range (featureSize):
#    sum+=(mean(yp,featureSize)-yp[i])*(mean(x[0],featureSize)-x[0][i])
#R0[0][0] = sum/((featureSize-1)*sigma0*sigma1)
#p#rint(R0[0][0])



#R0[0]= correlation(yDot,xDot[0],featureSize)
#R0[1]= correlation(yDot,xDot[1],featureSize)
for i in range(k):
    R0[i]=correlation(yDot,xDot[i],featureSize)

print("r01=",R0[0])
print("r02=",R0[1])

R = np.zeros(shape=(2,2)) #corellation matrix R
R[0][0]=R[1][1]=1
R[0][1]=R[1][0]=correlation(xDot[0],xDot[1],featureSize)




#----inverse matrix test------
R_inver=INVERSE_MATRIX(R,2)
print("R_inverse = \n",R_inver)
A=np.matmul(R_inver , R0)
print("A matrix \n",A)

B = np.zeros(shape=(k+1,1))
print(B)

B[0] = A[0]*sigma0/sigma1
B[1] = A[1]*sigma0/sigma2
B[2] = yp_mean-B[0]*x0_mean-B[1]*x1_mean

print("y-ի տեսքը կլինի  y=",B[0],"+",B[1],"*x1+",B[2],"*x2" )

print(B)



# հաշվարկային y_final
y_final = np.zeros(shape=(featureSize,1))
for i in range(featureSize):
    y_final[i]=B[0]+B[1]*x[0][i]+B[2]*x[1][i]
    #print(y_final[i])

#ռեգռեսիայով պայմանավորված միջին քառակուսային շեղումներ
y_final_mean = mean(y_final,featureSize)
SSR=0
for i in range(featureSize):
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