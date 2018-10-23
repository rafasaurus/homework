#!/usr/bin/env python
# -*- coding: utf-8 -*-
#All Subsets Regression - Generalized Linear Models
import numpy as np
import pandas as pd
import itertools
import scipy.optimize as optimizaion
from scipy.stats.stats import pearsonr,linregress
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

F_TABLE = 0.5

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
def exclude(N,df):
    X1 = df['X1']
    X2 = df['X2']
    X3 = df['X3']
    Y = df['Y']
    print(df.head())
    R_df = df[['Y']].copy()
    TO_ADD_FATURES=pd.DataFrame()
    for column in df:
        if column =='X1' or column =='X2' or column =='X3':

            #R_df = pd.concat([R_df, df[[]]], axis=1)
            R_df_copy = R_df
            dat = df[[column]]  # pd.DataFrame({column: range(0, df.size)})
            # R_df_copy = pd.concat([dat1, dat2], axis=1)
            # data = dat_1.append(dat_2)
            # R_df_copy.join(dat)
            R_df_copy = pd.concat([R_df_copy, dat], axis=1)
            # print(dat)
            R_df_corr = R_df_copy.corr()
            R_df_corr_numpy = R_df_corr.as_matrix()

            #print("R_df_corr_numpy=",R_df_copy.head())

            #print("R_df_copy=",R_df_copy)

            #computing regression
            to_line_reg_df = df['Y'].values[:, np.newaxis]
            # print("to_line_reg=",to_line_reg_df)
            featureSize = len(to_line_reg_df)
            featureCols = R_df.shape[1]#R_df.columns

            x_ = np.zeros(shape=(0, featureSize))
            x_ = np.append(x_, to_line_reg_df)
            x_ = np.append(x_, df[column])
            for to_add in TO_ADD_FATURES:
                x_ = np.append(x_,df[to_add])
            #x_ = np.append(x_, df[column])
            x_ = x_.reshape(featureCols+1, featureSize)
            # np.concatenate((x_, x1))
            # print("x++++",x_)
            # target data is array of shape (n,)
            y = df['Y'].values  # //////////////////////////////////////////////////////////
            x_ = x_.reshape(featureSize, -featureCols)  # reshaping for .fit method
            # print("x",x_)
            ## your code for regression
            regr = LinearRegression()
            regr.fit(x_, y)
            print("featureCols=",featureCols)
            # the correct coef is different from your findings
            print('regr.coef=',regr.coef_)
            print('intercept = ',regr.intercept_)
            y_hat = y
            for i in range(featureSize):
                y_hat[i] = regr.intercept_
                for j in range(featureCols):
                    y_hat[i] += regr.coef_[j] * x_[i][j]
            #print("y_hat=", y_hat)

            fisher_hat_q_m = ((RSquared(y_hat) ** 2) - RSquared(y) * (-3)) / (1 - RSquared(y_hat))
            print("fisher== ", fisher_hat_q_m)
            if (fisher_hat_q_m>=F_TABLE):
                print("-----------")
                print("ընդգրկվում է",column," փոփոխականը")
                print("-----------")
                R_df = pd.concat([R_df, dat], axis=1)
                TO_ADD_FATURES = pd.concat([TO_ADD_FATURES, dat], axis=1)
            else:
                print("-----------")
                print("բացառվում է", column, " փոփոխականը")
                print("-----------")
                del R_df_copy[column]
            print(R_df_copy.head())


#---------------------------------------program--------------------------------------------------------
df=pd.read_csv("Water Salinity and River Discharge.csv")

X1=df['X1']
X2=df['X2']
X3=df['X3']
Y=df['Y']
#plt.scatter(Y,X1)
#plt.show()
featureSize = df.__len__()
featureRows = 3

dof = featureRows # var that has been used for comuting SSR,SSE... for degrees of freedom

muffin = np.zeros(shape=(3, featureSize))
muffin[0]=X1
muffin[1]=X2
muffin[2]=X3

n=featureRows+1 #number of feature rows +1 for b0,b1,b2...

N=4#regression for N variables
Fisher_bool = 1
#computeN(N,df,Fisher_bool)
exclude(N,df)
