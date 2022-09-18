#!/usr/bin/env python
# coding: utf-8

# # The Sparks Foundation- Data Science & Business Analytics Internship

# # task 3- perform "Exploratory Data Analysis" on dataset 'Sample superstore'

# # Author- Shubhangi Baruah

# # dataset
# https://drive.google.com/file/d/1lV7is1B566UQPYzzY8R2ZmOritTW299S/view

# # importing libraries

# In[18]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[26]:


df =pd.read_csv("SampleSuperstore.csv")
df.head()


# In[27]:


df.info()


# In[28]:


df.describe()


# In[29]:


df.isnull().sum()


# In[32]:


plt.figure(figsize=(10,16))
df.groupby('Category')['Profit','Sales'].agg(['sum']).plot.bar()
plt.ylabel('Profit')
plt.show()


# In[33]:


plt.figure(figsize=(10,16))
df.groupby('Sub-Category')['Profit','Sales'].agg(['sum']).plot.bar()
plt.ylabel('Profit')
plt.show()


# In[35]:


plt.figure(figsize=(5,4))
sns.heatmap(df.corr(),annot=True)


# In[36]:


plt.figure(figsize=(8,7))
sns.countplot(df['Sub-Category'])
plt.xticks(rotation=45)


# In[37]:


plt.figure(figsize=(8,7))
sns.lineplot(df['Discount'],df['Profit'],data=df)


# In[38]:


plt.figure(figsize=(8,7))
sns.lineplot(df['Discount'],df['Quantity'],data=df)


# In[39]:


plt.figure(figsize=(8,7))
sns.lineplot(df['Discount'],df['Profit'],data=df)


# In[40]:


plt.figure(figsize=(8,7))
sns.lineplot(df['Ship Mode'],df['Quantity'],data=df)


# In[42]:


df.groupby('State')['Profit','Sales'].agg(['sum']).plot.bar()
plt.ylabel('Profit')
plt.show()


# In[43]:


plt.figure(figsize=(10,16))
df.groupby('Ship Mode')['Profit','Sales'].agg(['sum']).plot.bar()
plt.ylabel('Sale')
plt.show()


# # Thank you
# 

# In[ ]:




