#!/usr/bin/env python
# -*- coding: utf-8 -*-
#All Subsets Regression - Generalized Linear Models
import numpy as np
import pandas as pd
import itertools

def findsubsets(S,m):
    return set(itertools.combinations(S, m))
#import matplotlib.pyplot as plt

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
#faddev inverse matrix
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
        Bn = arr - (P * E)
        arr = np.matmul(static_arr, Bn)
        if nullfinder(arr, n):
            print("the end")
            break
    return print_val

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

def COMPUTE_Y(yp,muffin, n, featureSize):
    y = np.zeros(n, dtype=float)
    for i in range(n):
        if i==0:
            y[i] = sumX(yp,featureSize)
        else:
            y[i] = sumXY(yp,muffin[i-1],featureSize)
    return y

def mean(arr,n):
    s=0
    for i in range(n):
        s+=arr[i]
    return s/n

#ռեգրեսիայով պայմանավորված միջին քառակուսային շեղումներ
def SSR(arr,featureSize):
    arr_mean = mean(arr, featureSize)
    SSR_ = 0
    for i in range(n):
        SSR_ += (arr[i] - arr_mean) * (arr[i] - arr_mean)
    return SSR_

#միջին քառակուսային շեղումներ
def SS0(arr,featureSize):
    SS0_ = 0
    arr_mean = mean(arr, featureSize)
    for i in range(featureSize):
        SS0_ += (arr[i] - arr_mean) * (arr[i] - arr_mean)
    return SS0_

#դետերմինացման գործակից
def RSquared(arr,featureSize):
    return SSR(arr,featureSize)/SS0(arr,featureSize)

#ռեգռեսիայով պայմանավորված դիսպերսիան
def MSR(arr,featureSize,dof):
    MSR_ = SSR(arr,featureSize)/(dof)# featureRows+1 is "degrees of freedom"
    return MSR_

#անհամաձայնեցումներով պայմանավորված միջին քառակուսային շեղումներ
def SSE(yp,y_final,featureSize):
    SSE_ = 0
    for i in range(featureSize):
        SSE_+=(y_final[i] - yp[i])*(y_final[i] - yp[i])
    return SSE_

#մնացորդային դիսպերսիայի վիճակագրական գնահատական, ազատության աստիճանը n-k-1
def sigmaSquared(yp,y_final,feautreSize,dof):
    sigmaSquared_ = SSE(yp,y_final,featureSize)/(featureSize-dof-1)
    return sigmaSquared_

#ֆիշերի չափանիշ
def FISHER(yp,y_final,featureSize,dof):
    F = MSR(y_final,featureSize,dof)/(sigmaSquared(yp,y_final,featureSize,dof))
    return F
def fact(n):
    fact_=1
    for i in range(1,n+1):
        fact_=fact_*i
    return fact_

def combinatorial(n,k):
    return fact(n) / (fact(n - k) * fact(k))




def getB_index(featureRows,df,global_iter):

    S = [1, 2, 3]
    S=findsubsets(S, global_iter)
    return S


def computeN(N,df):#computes regression for N variables
    featureSize = df.__len__()
    featureRows = 3
    X1 = df['X1']
    X2 = df['X2']
    X3 = df['X3']
    Y = df['Y']
    X_ = np.zeros(shape=(3, featureSize))
    X_[0] = X1
    X_[1] = X2
    X_[2] = X3
    
    global_iter = featureRows
    dof = featureRows  # var that has been used for comuting SSR,SSE... for degrees of freedom

    # print("featureSize = ",featureSize)



    while global_iter != 0:
        c=combinatorial(featureRows,global_iter)
        #print("c=",c)

        B_indexes=getB_index(featureRows, df, global_iter)
        print(B_indexes)


        list_=[]

        for index in B_indexes:
            for index_of_index in index:

                    #print(index_of_index)
                    list_.append(index_of_index)

            print("  ")
        #print(list_)
        print("--------end----------")



        '''
        matrix=np.zeros(shape=(global_iter,c))
        print("matrixLen=",matrix.__len__())

        if c==1:
         1   for i in range(global_iter):
                print(i)
                #matrix[i]=1#list_[i]

        print("matrix=",matrix)
        '''
        middle_muffin = np.zeros(shape=(global_iter, featureSize))
        
        n = featureRows + 1  # number of feature rows +1 for b0,b1,b2...
        #X = COMPUTE_REGRESSION_X(middle_muffin, global_iter, featureSize, n)
        vector = COMPUTE_Y(Y, middle_muffin, global_iter + 1, featureSize)

        # print(X)
        # print(vector)

        #inverse_arr = INVERSE_MATRIX(X, n)
        # print(inverse_arr)

        #B = np.matmul(inverse_arr, vector)
        # print()
        # print(B)

        y_final = np.zeros(shape=(featureSize))






        global_iter = global_iter - 1


#---------------------------------------program--------------------------------------------------------
df=pd.read_csv("Water Salinity and River Discharge.csv")
#plt.scatter(df)
#plt.show()
#print(df.head())
#arr = np.zeros(shape=df['X1'].)
#print(df["X1"].head())
X1=df['X1']
X2=df['X2']
X3=df['X3']
Y=df['Y']

featureSize = df.__len__()
featureRows = 3

dof = featureRows # var that has been used for comuting SSR,SSE... for degrees of freedom

#print("featureSize = ",featureSize)

muffin = np.zeros(shape=(3, featureSize))
muffin[0]=X1
muffin[1]=X2
muffin[2]=X3

n=featureRows+1 #number of feature rows +1 for b0,b1,b2...
X=COMPUTE_REGRESSION_X(muffin,featureRows,featureSize,n)
#vector = COMPUTE_Y(Y, muffin,featureRows+1, featureSize)

#print(X)
#print(vector)

#inverse_arr = INVERSE_MATRIX(X, n)
#print(inverse_arr)

#B = np.matmul(inverse_arr, vector)
#print()
#print(B)

#y_final = np.zeros(shape=(featureSize))


#for i in range(featureSize):
#    y_final[i]=B[0]+B[1]*muffin[0][i]+B[2]*muffin[1][i]+B[3]*muffin[2][i]

#print("y_final=",y_final)
#print("rsquared=",RSquared(y_final,featureSize))
N=4#regression for N variables
computeN(N,df)



print("-----------------------")
global_iter=featureRows
getB_index(featureRows,df,global_iter)
