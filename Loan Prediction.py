#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import os
os.chdir('C:\DSBD project\Streamlit_Bank_Loan_Prediction-master\Streamlit_Bank_Loan_Prediction-master')


# In[5]:


train=pd.read_csv('./Loan_Data/train.csv')
train.Loan_Status=train.Loan_Status.map({'Y':1,'N':0})


# # Checking missing data

# In[6]:


train.isnull().sum()


# # Preprocessing

# In[7]:


Loan_status=train.Loan_Status
train.drop('Loan_Status',axis=1,inplace=True)
test=pd.read_csv('./Loan_Data/test.csv')
Loan_ID=test.Loan_ID
data=train.append(test)
data.head()


# In[8]:


data.shape


# In[9]:


data.describe()


# In[10]:


data.isnull().sum()


# In[11]:


data.Dependents.dtypes


# In[ ]:




