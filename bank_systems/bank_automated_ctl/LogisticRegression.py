#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# ## Data
# 
# The data is related with direct marketing campaigns (phone calls) of a Portuguese banking institution. The classification goal is to predict if the client will subscribe (1/0) a term deposit (variable y).

# This dataset provides the customer information. It includes 41188 records and 21 fields.

# In[2]:
class logic:
    def inference(self, X):
        return self.logreg.predict(X)
    def train(self):
        data = pd.read_csv('bank.csv', header=0)
        data = data.dropna()
        print(data.shape)
        print(list(data.columns))
        
        
        # In[3]:
        
        
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
        # # 14 - previous: number of contacts performed before this campaign and for this client (numeric)
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
        
        # In[5]:
        
        
        data['education']=np.where(data['education'] =='basic.9y', 'Basic', data['education'])
        data['education']=np.where(data['education'] =='basic.6y', 'Basic', data['education'])
        data['education']=np.where(data['education'] =='basic.4y', 'Basic', data['education'])
        
        
        # After grouping, this is the columns
        
        # In[6]:
        
        
        data['education'].unique()
        
        
        # ### Data exploration
        
        # In[7]:
        
        
        data['y'].value_counts()
        
        
        # In[8]:
        
        
        sns.countplot(x='y',data=data, palette='hls')
        # plt.show()
        plt.savefig('count_plot')
        
        
        # There are 36548 no's and 4640 yes's in the outcome variables.
        
        # Let's get a sense of the numbers across the two classes
        
        # In[9]:
        
        
        data.groupby('y').mean()
        
        
        # Observations:
        # 
        # The average age of customers who bought the term deposit is higher than that of the customers who didn't.
        # The pdays (days since the customer was last contacted) is understandably lower for the customers who bought it. The lower the pdays, the better the memory of the last call and hence the better chances of a sale.
        # Surprisingly, campaigns (number of contacts or calls made during the current campaign) are lower for customers who bought the term deposit.
        
        # We can calculate categorical means for other categorical variables such as education and marital status to get a more detailed sense of our data.
        
        # In[10]:
        
        
        data.groupby('job').mean()
        
        
        # In[11]:
        
        
        data.groupby('marital').mean()
        
        
        # In[12]:
        
        
        data.groupby('education').mean()
        
        
        # Visualizations
        
        # In[13]:
        
        
        # get_ipython().run_line_magic('matplotlib', 'inline')
        pd.crosstab(data.job,data.y).plot(kind='bar')
        plt.title('Purchase Frequency for Job Title')
        plt.xlabel('Job')
        plt.ylabel('Frequency of Purchase')
        plt.savefig('purchase_fre_job')
        
        
        # The frequency of purchase of the deposit depends a great deal on the job title. Thus, the job title can be a good predictor of the outcome variable.
        
        # In[14]:
        
        
        table=pd.crosstab(data.marital,data.y)
        table.div(table.sum(1).astype(float), axis=0).plot(kind='bar', stacked=True)
        plt.title('Stacked Bar Chart of Marital Status vs Purchase')
        plt.xlabel('Marital Status')
        plt.ylabel('Proportion of Customers')
        plt.savefig('mariral_vs_pur_stack')
        
        
        # Hard to see, but the marital status does not seem a strong predictor for the outcome variable.
        
        # In[15]:
        
        
        table=pd.crosstab(data.education,data.y)
        table.div(table.sum(1).astype(float), axis=0).plot(kind='bar', stacked=True)
        plt.title('Stacked Bar Chart of Education vs Purchase')
        plt.xlabel('Education')
        plt.ylabel('Proportion of Customers')
        plt.savefig('edu_vs_pur_stack')
        
        
        # Education seems a good predictor of the outcome variable.
        
        # In[16]:
        
        
        pd.crosstab(data.day_of_week,data.y).plot(kind='bar')
        plt.title('Purchase Frequency for Day of Week')
        plt.xlabel('Day of Week')
        plt.ylabel('Frequency of Purchase')
        plt.savefig('pur_dayofweek_bar')
        
        
        # Day of week may not be a good predictor of the outcome
        
        # In[17]:
        
        
        pd.crosstab(data.month,data.y).plot(kind='bar')
        plt.title('Purchase Frequency for Month')
        plt.xlabel('Month')
        plt.ylabel('Frequency of Purchase')
        plt.savefig('pur_fre_month_bar')
        
        
        # Month might be a good predictor of the outcome variable
        
        # In[18]:
        
        
        data.age.hist()
        plt.title('Histogram of Age')
        plt.xlabel('Age')
        plt.ylabel('Frequency')
        plt.savefig('hist_age')
        
        
        # The most of the customers of the bank in this dataset are in the age range of 30-40.
        
        # In[19]:
        
        
        pd.crosstab(data.poutcome,data.y).plot(kind='bar')
        plt.title('Purchase Frequency for Poutcome')
        plt.xlabel('Poutcome')
        plt.ylabel('Frequency of Purchase')
        plt.savefig('pur_fre_pout_bar')
        
        
        # Poutcome seems to be a good predictor of the outcome variable.
        
        # ### Create dummy variables
        
        # In[20]:
        
        
        cat_vars=['job','marital','education','default','housing','loan','contact','month','day_of_week','poutcome']
        for var in cat_vars:
            cat_list='var'+'_'+var
            cat_list = pd.get_dummies(data[var], prefix=var)
            data1=data.join(cat_list)
            data=data1
        
        
        # In[21]:
        
        
        cat_vars=['job','marital','education','default','housing','loan','contact','month','day_of_week','poutcome']
        data_vars=data.columns.values.tolist()
        to_keep=[i for i in data_vars if i not in cat_vars]
        
        
        # In[22]:
        
        
        data_final=data[to_keep]
        data_final.columns.values
        
        
        # In[23]:
        
        
        data_final_vars=data_final.columns.values.tolist()
        y=['y']
        X=[i for i in data_final_vars if i not in y]
        
        
        # ### Feature Selection
        
        # In[24]:
        
        
        from sklearn import datasets
        from sklearn.feature_selection import RFE
        from sklearn.linear_model import LogisticRegression

        self.logreg = LogisticRegression()

        rfe = RFE(logreg, 18)
        rfe = rfe.fit(data_final[X], data_final[y] )
        print(rfe.support_)
        print(rfe.ranking_)
        
        
        # The Recursive Feature Elimination (RFE) has helped us select the following features: "previous", "euribor3m", "job_blue-collar", "job_retired", "job_services", "job_student", "default_no", "month_aug", "month_dec", "month_jul", "month_nov", "month_oct", "month_sep", "day_of_week_fri", "day_of_week_wed", "poutcome_failure", "poutcome_nonexistent", "poutcome_success".
        
        # In[25]:
        
        
        cols=["previous", "euribor3m", "job_blue-collar", "job_retired", "job_services", "job_student", "default_no", 
              "month_aug", "month_dec", "month_jul", "month_nov", "month_oct", "month_sep", "day_of_week_fri", "day_of_week_wed", 
              "poutcome_failure", "poutcome_nonexistent", "poutcome_success"] 
        X=data_final[cols]
        y=data_final['y']
        
        
        # ### Implementing the model
        
        # In[26]:
        
        
        import statsmodels.api as sm
        logit_model=sm.Logit(y,X)
        result=logit_model.fit()
        print(result.summary())
        
        
        # The p-values for most of the variables are very small, therefore, most of them are significant to the model.
        
        # ### Logistic Regression Model Fitting
        
        # In[27]:
        
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
        from sklearn.linear_model import LogisticRegression
        from sklearn import metrics
        logreg = LogisticRegression()
        logreg.fit(X_train, y_train)
        
        
        # #### Predicting the test set results and caculating the accuracy
        
        # In[50]:
        
        
        y_pred = logreg.predict(X_test)
        print("debug::::X_test:", X_train.head)
        print("debug::::y_pred:", y_pred.shape)
        
        
        # In[45]:
        
        
        print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(logreg.score(X_test, y_test)))
        
        
        # ### Cross Validation
        
        # In[30]:
        
        
        from sklearn import model_selection
        from sklearn.model_selection import cross_val_score
        kfold = model_selection.KFold(n_splits=10, random_state=7)
        modelCV = LogisticRegression()
        scoring = 'accuracy'
        results = model_selection.cross_val_score(modelCV, X_train, y_train, cv=kfold, scoring=scoring)
        print("10-fold cross validation average accuracy: %.3f" % (results.mean()))
        
        
        # ### Confusion Matrix
        
        # In[31]:
        
        
        from sklearn.metrics import confusion_matrix
        confusion_matrix = confusion_matrix(y_test, y_pred)
        print(confusion_matrix)
        
        
        # The result is telling us that we have 10872+254 correct predictions and 1122+109 incorrect predictions.
        
        # #### Accuracy
        
        # In[35]:
        
        
        print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(logreg.score(X_test, y_test)))
        
        
        # #### Compute precision, recall, F-measure and support
        # 
        # The precision is the ratio tp / (tp + fp) where tp is the number of true positives and fp the number of false positives. The precision is intuitively the ability of the classifier not to label as positive a sample that is negative.
        # 
        # The recall is the ratio tp / (tp + fn) where tp is the number of true positives and fn the number of false negatives. The recall is intuitively the ability of the classifier to find all the positive samples.
        # 
        # The F-beta score can be interpreted as a weighted harmonic mean of the precision and recall, where an F-beta score reaches its best value at 1 and worst score at 0.
        # 
        # The F-beta score weights recall more than precision by a factor of beta. beta == 1.0 means recall and precision are equally important.
        # 
        # The support is the number of occurrences of each class in y_test.
        
        # In[36]:
        
        
        from sklearn.metrics import classification_report
        print(classification_report(y_test, y_pred))
        
        
        # #### Interpretation: 
        # 
        # Of the entire test set, 88% of the promoted term deposit were the term deposit that the customers liked. Of the entire test set, 90% of the customer's preferred term deposit were promoted.
        
        # ### ROC Curvefrom sklearn import metrics
        # from ggplot import *
        # 
        # prob = clf1.predict_proba(X_test)[:,1]
        # fpr, sensitivity, _ = metrics.roc_curve(Y_test, prob)
        # 
        # df = pd.DataFrame(dict(fpr=fpr, sensitivity=sensitivity))
        # ggplot(df, aes(x='fpr', y='sensitivity')) +\
        #     geom_line() +\
        #     geom_abline(linetype='dashed')
        
        # In[37]:
        
        
        from sklearn.metrics import roc_auc_score
        from sklearn.metrics import roc_curve
        logit_roc_auc = roc_auc_score(y_test, logreg.predict(X_test))
        fpr, tpr, thresholds = roc_curve(y_test, logreg.predict_proba(X_test)[:,1])
        plt.figure()
        plt.plot(fpr, tpr, label='Logistic Regression (area = %0.2f)' % logit_roc_auc)
        plt.plot([0, 1], [0, 1],'r--')
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('Receiver operating characteristic')
        plt.legend(loc="lower right")
        plt.savefig('Log_ROC')
        # plt.show()
