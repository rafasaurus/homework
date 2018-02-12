#!/usr/bin/env python
# -*- coding: utf-8 -*-
#All Subsets Regression - Generalized Linear Models
import numpy as np
import pandas as pd
import itertools
import scipy.optimize as optimizaion
from scipy.stats.stats import pearsonr,linregress
from sklearn.linear_model import LinearRegression

F_TABLE = 0.0001
def findsubsets(S,m):
    return set(itertools.combinations(S, m))

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

#Faddeev inverse matrix
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
def RSquared(arr):
    featureSize=arr.__len__()
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
#def FISHER_HAT():
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

def include(N,df):
    X1 = df['X1']
    X2 = df['X2']
    X3 = df['X3']
    Y = df['Y']

    #print(np.corrcoef(Y,X1)[0,1])
    data_cols =0
    max_corr_string = "X1"
    max_corr = (np.corrcoef(df['X1'], df['Y'])[0, 1]) ** 2
    max_corr_place_counter = 0
    for column in df:
        data_cols += 1
        if (data_cols < N):
            if ((np.corrcoef(df[column],df['Y'])[0,1])**2>max_corr):
                max_corr = np.corrcoef(df[column],df['Y'])[0,1]
                max_corr_string = column
                max_corr_place_counter=data_cols

            #print(np.corrcoef(df[column],df['Y'])[0,1])

    #This computes a least-squares regression for two sets of measurements.
    slope, intercept, r_value, p_value, std_err = linregress(df[max_corr_string], df['Y'])

    #r_value ** 2 is r_squared
    fisher = (r_value**2)*(data_cols-2)/(1-r_value**2)
    print("ֆիշերի չափանիշը", max_corr_string, "փոփոխականի ընդգրկման դեպքում = ",fisher)
    if (fisher < F_TABLE):
        return 0
    else :
        print("-----------")
        print("ընդգրկվում է", max_corr_string, " փոփոխականը")
        print("-----------")
    R_df = df[['Y']].copy()
    R_df = pd.concat([R_df, df[[max_corr_string]]], axis=1)
    R_df_copy=R_df
    iter_q_iter=0

    #print("_______")
    #print(np.corrcoef(df['X1'],df['X2']))
    #print("pierce-----")
    #print(pearsonr(df['X1'],df['Y']))
    #print("endo")
    R_df = df[['Y']].copy()
    TO_ADD_FATURES = pd.DataFrame()
    for column in df:

        if column != max_corr_string and column!='Y' and iter_q_iter!=0:
            dat = df[[column]]#pd.DataFrame({column: range(0, df.size)})
            #R_df_copy = pd.concat([dat1, dat2], axis=1)
            #data = dat_1.append(dat_2)
            #R_df_copy.join(dat)
            R_df_copy = pd.concat([R_df_copy, dat], axis=1)
            #print(dat)
            R_df_corr = R_df_copy.corr()
            R_df_corr_numpy = R_df_corr.as_matrix()
            #R_df_corr_inverse=INVERSE_MATRIX(R_df_corr_numpy,_df_corr_numpy.size)
            R_df_corr_inverse = INVERSE_MATRIX(R_df_corr_numpy,len(R_df_copy.columns))#np.linalg.inv (R_df_corr_numpy)
            #print()
            #print((R_df_corr_inverse))
            Q_ = R_df_corr_inverse

            R_SQUARED_CYCLE = True

            max_j = 0
            max = .0
            for j in range(1,3):#(len(R_df_copy.columns)):
                if j !=max_corr_place_counter:
                    middle_var = ((Q_[0][j]) ** 2) / (Q_[0][0] * Q_[j][j])
                    if R_SQUARED_CYCLE == True:
                        R_SQUARED_CYCLE = False
                        max = middle_var
                        max_j=j
                    else:
                        if (middle_var > max):
                            max = ((Q_[0][j])**2) / (Q_[0][0]*Q_[j][j])
                            max_j = j

            to_line_reg_df = df[max_corr_string].values[:, np.newaxis]
            #print("to_line_reg=",to_line_reg_df)
            featureSize = len(to_line_reg_df)
            featureCols = 1
            x_ = np.zeros(shape=(0, featureSize))
            x_ = np.append(x_, to_line_reg_df)
            x_ = np.append(x_, df[column])
            x_ = x_.reshape(2,featureSize)
            # np.concatenate((x_, x1))
            #print("x++++",x_)
            # target data is array of shape (n,)
            y = df['Y'].values #//////////////////////////////////////////////////////////
            x_ = x_.reshape(featureSize, -featureCols)  # reshaping for .fit method
            #print("x",x_)
            ## your code for regression
            regr = LinearRegression()
            regr.fit(x_, y)


            # the correct coef is different from your findings
            print("regr.coef_=",regr.coef_)
            print("regr.intercept_=",regr.intercept_)
            #computes y_hat
            y_hat = y
            for i in range(featureSize):
                y_hat[i] = regr.intercept_
                for j in range(featureCols):
                    y_hat[i] += regr.coef_[j] * x_[i][j]
            #print("y_hat=",y_hat)
            #y_hat_ = y# y hat with only b0+b1
            #for i in range(featureSize):
            #    y_hat[i] = regr.intercept_
            #    for j in range(featureCols):
            #        y_hat_[i] += regr.coef_[j] * x_[i][j]
            #print("y_hat_=",y_hat)

            fisher_hat_q_m = ((RSquared(y_hat)**2) - RSquared(y)*(-3))/(1-RSquared(y_hat))
            #print("fisher== ",fisher_hat_q_m)
            print("ֆիշերի չափանիշը", column, "փոփոխականի ընդգրկման դեպքում = ", fisher_hat_q_m)


            if (fisher_hat_q_m >= F_TABLE):
                print("-----------")
                print("ընդգրկվում է", column, " փոփոխականը")
                print("-----------")
                R_df = pd.concat([R_df, dat], axis=1)
                TO_ADD_FATURES = pd.concat([TO_ADD_FATURES, dat], axis=1)
            else:
                print("-----------")
                print("բացառվում է", column, " փոփոխականը")
                print("-----------")
                del R_df_copy[column]
            print(R_df.head())
        iter_q_iter+=1

    #del R_df_copy['Unnamed']r
    #print(R_df_copy)


#---------------------------------------program--------------------------------------------------------
df=pd.read_csv("Water Salinity and River Discharge.csv")

X1=df['X1']
X2=df['X2']
X3=df['X3']
Y=df['Y']

featureSize = df.__len__()
featureRows = 3

dof = featureRows # var that has been used for comuting SSR,SSE... for degrees of freedom

muffin = np.zeros(shape=(3, featureSize))
muffin[0]=X1
muffin[1]=X2
muffin[2]=X3

n=featureRows+1 #number of feature rows +1 for b0,b1,b2...
X=COMPUTE_REGRESSION_X(muffin,featureRows,featureSize,n)

N=4#regression for N variables
Fisher_bool = 1
#computeN(N,df,Fisher_bool)
include(N,df)
print("-----------------------")
global_iter=featureRows
getB_index(featureRows,df,global_iter)

