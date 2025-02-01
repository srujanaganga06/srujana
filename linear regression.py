#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Load the libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf


# In[2]:


#Reading the file
data1 = pd.read_csv("NewspaperData.csv")
data1


# In[3]:


data1.info()


# In[4]:


data1.isnull().sum()


# In[5]:


data1.describe()


# In[11]:


#Boxplot for daily column
plt.figure(figsize=(6,3))
plt.title("Box plot for Daily Sales")
plt.boxplot(data1["daily"], vert = False)
plt.show()


# In[12]:


sns.histplot(data1['daily'], kde = True,stat='density',)
plt.show()


# In[13]:


#Boxplot for daily column
plt.figure(figsize=(6,3))
plt.title("Box plot for Sunday Sales")
plt.boxplot(data1["sunday"], vert = False)
plt.show()


# In[ ]:


#Observations
    -There are no missing values
    -The daily column values appears to be right-skewed
    -The sunday column values also appear to be right-skewed
    -The are two outliers in both daily column and also in sunday column as observed from the boxplots 


# In[14]:


#Scatter plot and Correlation Strength
x=data1["daily"]
y=data1["sunday"]
plt.scatter(data1["daily"], data1["sunday"])
plt.xlim(0, max(x) + 100)
plt.ylim(0, max(y) + 100)
plt.show()


# In[15]:


data1["daily"].corr(data1["sunday"])


# In[16]:


data1[["daily","sunday"]].corr()


# In[ ]:


#Observations
    -The relationship between x (daily) and y (sunday) is seen to be linear as seen from scatter plot
    -The correlation is strong positive with Pearson's correlation coefficent as 0.958154


# In[21]:


#Build regression Model
import statsmodels.formula.api as smf
model1 = smf.ols("sunday~daily",data = data1).fit()


# In[22]:


model1.summary()


# In[ ]:





# In[ ]:




