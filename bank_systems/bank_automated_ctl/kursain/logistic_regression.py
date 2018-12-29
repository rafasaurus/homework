#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt 
plt.rc("font", size=14)
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import seaborn as sns
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)

class logic:
    def __init__(self):
        self.x_test_ = []
        self.logreg = LogisticRegression()
        pass
    def setTestData(self, x_test):
        self.x_test_ = x_test
        print("self.x_test: ", self.x_test_)
    def inference(self):
        print("self.x_test: ", self.x_test_)
        self.x_test_ = self.x_test_.reshape(1, -1)
        return self.logreg.predict_proba(self.x_test_)
    def getDataSampleValue(self):
        data = pd.read_csv('bank.csv', header=0)
        data = data.dropna()
        data['education'].unique()
        data['education']=np.where(data['education'] =='basic.9y', 'Basic', data['education'])
        data['education']=np.where(data['education'] =='basic.6y', 'Basic', data['education'])
        data['education']=np.where(data['education'] =='basic.4y', 'Basic', data['education'])
        data['education'].unique()
        data['y'].value_counts()
        data.groupby('y').mean()
        data.groupby('job').mean()
        data.groupby('marital').mean()
        data.groupby('education').mean()
        cat_vars=['job','marital','education','default','housing','loan','contact','month','day_of_week','poutcome']
        for var in cat_vars:
            cat_list='var'+'_'+var
            cat_list = pd.get_dummies(data[var], prefix=var)
            data1=data.join(cat_list)
            data=data1
        cat_vars=['job','marital','education','default','housing','loan','contact','month','day_of_week','poutcome']
        data_vars=data.columns.values.tolist()
        to_keep=[i for i in data_vars if i not in cat_vars]
        data_final=data[to_keep]
        data_final.columns.values
        data_final_vars=data_final.columns.values.tolist()
        y=['y']
        X=[i for i in data_final_vars if i not in y]
        cols=["previous", "euribor3m", "job_blue-collar", "job_retired", "job_services", "job_student", "default_no", 
              "month_aug", "month_dec", "month_jul", "month_nov", "month_oct", "month_sep", "day_of_week_fri", "day_of_week_wed", 
              "poutcome_failure", "poutcome_nonexistent", "poutcome_success"] 
        X=data_final[cols]
        y=data_final['y']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
        return X_test.head(1)

        # return data.iloc[:].head(1).copy()
    def train(self):
        data = pd.read_csv('bank.csv', header=0)
        data = data.dropna()
        print(data.shape)
        print(list(data.columns))
        data.head()
        
        # #### Input variables
        
        # 1 - age (numeric)
        # 
        # 2 - job : type of job (categorical: 'admin.','blue-collar','entrepreneur','housemaid','management','retired','self-employed','services','student','technician','unemployed','unknown')
        # 
        # 3 - marital : marital status (categorical: 'divorced','married','single','unknown'; note: 'divorced' means divorced or widowed)
        # 
        # 4 - education (categorical: 'basic.4y','basic.6y','basic.9y','high.school','illiterate','professional.course','university.degree','unknown')
        # 
        # 5 - default: has credit in default? (categorical: 'no','yes','unknown')
        # 
        # 6 - housing: has housing loan? (categorical: 'no','yes','unknown')
        # 
        # 7 - loan: has personal loan? (categorical: 'no','yes','unknown')
        # 
        # 8 - contact: contact communication type (categorical: 'cellular','telephone')
        # 
        # 9 - month: last contact month of year (categorical: 'jan', 'feb', 'mar', ..., 'nov', 'dec')
        # 
        # 10 - day_of_week: last contact day of the week (categorical: 'mon','tue','wed','thu','fri')
        # 
        # 11 - duration: last contact duration, in seconds (numeric). Important note: this attribute highly affects the output target (e.g., if duration=0 then y='no'). Yet, the duration is not known before a call is performed. Also, after the end of the call y is obviously known. Thus, this input should only be included for benchmark purposes and should be discarded if the intention is to have a realistic predictive model.
        # 
        # 12 - campaign: number of contacts performed during this campaign and for this client (numeric, includes last contact)
        # 
        # 13 - pdays: number of days that passed by after the client was last contacted from a previous campaign (numeric; 999 means client was not previously contacted)
        # 14 - previous: number of contacts performed before this campaign and for this client (numeric)
        # 
        # 15 - poutcome: outcome of the previous marketing campaign (categorical: 'failure','nonexistent','success')
        # 
        # 16 - emp.var.rate: employment variation rate - (numeric)
        # 
        # 17 - cons.price.idx: consumer price index - (numeric)
        # 
        # 18 - cons.conf.idx: consumer confidence index - (numeric) 
        # 
        # 19 - euribor3m: euribor 3 month rate - (numeric)
        # 
        # 20 - nr.employed: number of employees - (numeric)
        
        # #### Predict variable (desired target):
        # 
        # y - has the client subscribed a term deposit? (binary: '1','0')
        
        # The education column of the dataset has many categories and we need to reduce the categories for a better modelling. The education column has the following categories:
        
        # In[4]:
        
        
        data['education'].unique()
        # Let us group "basic.4y", "basic.9y" and "basic.6y" together and call them "basic".
        data['education']=np.where(data['education'] =='basic.9y', 'Basic', data['education'])
        data['education']=np.where(data['education'] =='basic.6y', 'Basic', data['education'])
        data['education']=np.where(data['education'] =='basic.4y', 'Basic', data['education'])
        # After grouping, this is the columns
        data['education'].unique()
        # ### Data exploration
        data['y'].value_counts()
        sns.countplot(x='y',data=data, palette='hls')
        plt.savefig('count_plot')
        # There are 36548 no's and 4640 yes's in the outcome variables.
        # Let's get a sense of the numbers across the two classes
        data.groupby('y').mean()
        # Observations:
        # The average age of customers who bought the term deposit is higher than that of the customers who didn't.
        # The pdays (days since the customer was last contacted) is understandably lower for the customers who bought it. The lower the pdays, the better the memory of the last call and hence the better chances of a sale.
        # Surprisingly, campaigns (number of contacts or calls made during the current campaign) are lower for customers who bought the term deposit.
        # We can calculate categorical means for other categorical variables such as education and marital status to get a more detailed sense of our data.
        data.groupby('job').mean()
        data.groupby('marital').mean()
        data.groupby('education').mean()
        # Visualizations
        # get_ipython().run_line_magic('matplotlib', 'inline')
        pd.crosstab(data.job,data.y).plot(kind='bar')
        plt.title('Purchase Frequency for Job Title')
        plt.xlabel('Job')
        plt.ylabel('Frequency of Purchase')
        plt.savefig('purchase_fre_job')
        # The frequency of purchase of the deposit depends a great deal on the job title. Thus, the job title can be a good predictor of the outcome variable.
        table=pd.crosstab(data.marital,data.y)
        table.div(table.sum(1).astype(float), axis=0).plot(kind='bar', stacked=True)
        plt.title('Stacked Bar Chart of Marital Status vs Purchase')
        plt.xlabel('Marital Status')
        plt.ylabel('Proportion of Customers')
        plt.savefig('mariral_vs_pur_stack')
        # Hard to see, but the marital status does not seem a strong predictor for the outcome variable.
        table=pd.crosstab(data.education,data.y)
        table.div(table.sum(1).astype(float), axis=0).plot(kind='bar', stacked=True)
        plt.title('Stacked Bar Chart of Education vs Purchase')
        plt.xlabel('Education')
        plt.ylabel('Proportion of Customers')
        plt.savefig('edu_vs_pur_stack')
        # Education seems a good predictor of the outcome variable.
        pd.crosstab(data.day_of_week,data.y).plot(kind='bar')
        plt.title('Purchase Frequency for Day of Week')
        plt.xlabel('Day of Week')
        plt.ylabel('Frequency of Purchase')
        plt.savefig('pur_dayofweek_bar')
        # Day of week may not be a good predictor of the outcome
        pd.crosstab(data.month,data.y).plot(kind='bar')
        plt.title('Purchase Frequency for Month')
        plt.xlabel('Month')
        plt.ylabel('Frequency of Purchase')
        plt.savefig('pur_fre_month_bar')
        # Month might be a good predictor of the outcome variable
        data.age.hist()
        plt.title('Histogram of Age')
        plt.xlabel('Age')
        plt.ylabel('Frequency')
        plt.savefig('hist_age')
        # The most of the customers of the bank in this dataset are in the age range of 30-40.
        pd.crosstab(data.poutcome,data.y).plot(kind='bar')
        plt.title('Purchase Frequency for Poutcome')
        plt.xlabel('Poutcome')
        plt.ylabel('Frequency of Purchase')
        plt.savefig('pur_fre_pout_bar')
        # Poutcome seems to be a good predictor of the outcome variable.
        # ### Create dummy variables
        cat_vars=['job','marital','education','default','housing','loan','contact','month','day_of_week','poutcome']
        for var in cat_vars:
            cat_list='var'+'_'+var
            cat_list = pd.get_dummies(data[var], prefix=var)
            data1=data.join(cat_list)
            data=data1

        cat_vars=['job','marital','education','default','housing','loan','contact','month','day_of_week','poutcome']
        data_vars=data.columns.values.tolist()
        to_keep=[i for i in data_vars if i not in cat_vars]
        data_final=data[to_keep]
        data_final.columns.values
        data_final_vars=data_final.columns.values.tolist()
        y=['y']
        X=[i for i in data_final_vars if i not in y]

        # ### Feature Selection
        from sklearn import datasets
        from sklearn.feature_selection import RFE
        from sklearn.linear_model import LogisticRegression
        rfe = RFE(self.logreg, 18)# The Recursive Feature Elimination (RFE)
        rfe = rfe.fit(data_final[X], data_final[y] )
        print(rfe.support_)
        print(rfe.ranking_)
        # The Recursive Feature Elimination (RFE) has helped us select the following features: "previous", "euribor3m", "job_blue-collar", "job_retired", "job_services", "job_student", "default_no", "month_aug", "month_dec", "month_jul", "month_nov", "month_oct", "month_sep", "day_of_week_fri", "day_of_week_wed", "poutcome_failure", "poutcome_nonexistent", "poutcome_success".
        cols=["previous", "euribor3m", "job_blue-collar", "job_retired", "job_services", "job_student", "default_no", 
              "month_aug", "month_dec", "month_jul", "month_nov", "month_oct", "month_sep", "day_of_week_fri", "day_of_week_wed", 
              "poutcome_failure", "poutcome_nonexistent", "poutcome_success"] 
        X=data_final[cols]
        y=data_final['y']

        # ### Implementing the model
        import statsmodels.api as sm
        logit_model=sm.Logit(y,X)
        result=logit_model.fit()
        print(result.summary())
        # The p-values for most of the variables are very small, therefore, most of them are significant to the model.

        # ### Logistic Regression Model Fitting
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
        from sklearn.linear_model import LogisticRegression
        from sklearn import metrics
        self.logreg = LogisticRegression()
        self.logreg.fit(X_train, y_train)

        # #### Predicting the test set results and caculating the accuracy
        test_ = [[0.  ,  1.405 ,1.,    0.,    0.    ,0.   , 1.   , 0.  ,  0. ,   0. ,   0.,    0.,  0.  ,  0.  ,  0.  ,  0.   , 1.  ,  0.   ]]
        y_pred = self.logreg.predict(test_)
        print("deself.bug::::X_test:", X_train.shape)
        print("shape: " , X_test.shape)
        print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(self.logreg.score(X_test, y_test)))

        # ### Cross Validation
        from sklearn import model_selection
        from sklearn.model_selection import cross_val_score
        kfold = model_selection.KFold(n_splits=10, random_state=7)
        modelCV = LogisticRegression()
        scoring = 'accuracy'
        results = model_selection.cross_val_score(modelCV, X_train, y_train, cv=kfold, scoring=scoring)
        print("10-fold cross validation average accuracy: %.3f" % (results.mean()))
