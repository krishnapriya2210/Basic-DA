#!/usr/bin/env python
# coding: utf-8

# In[156]:


#importing libraries required for analysis on the customer dB
import pandas as pd
import numpy as np


# In[114]:


#loading the dataset
df = pd.read_csv("project_data.csv")


# # Understanding the dataset

# In[115]:


df.head(5)


# In[116]:


df.tail()


# In[117]:


df.count()


# In[123]:


#Since the row values "Widowed" and "Widow" mean the same, we can consider rename them as one for further analysis
df1 = df.replace(['Widowed'],'Widow')


# In[125]:


#Check if the changes have been applied
df1.head(10)


# In[127]:


#checking for null values in dataset
df1.isnull().sum()


# In[129]:


#viewing the null value data
df1[df1['annual_income'].isna()]


# In[130]:


#dropping rows with null values
df1=df1.dropna()


# In[131]:


#checking if there are anymore null data left
df1.isnull().sum()


# In[132]:


#Only 3% of data is dropped,so we still have good number of data to continue the analysis
df1.count()


# In[133]:


#number of customer profiles based on education_level
df1.groupby(by=["educational_level"]).count()


# In[134]:


#viewing number of profiles based on education_values and marital_status
df1.groupby(by=["educational_level","marital_status"]).count()


# In[143]:


#dataframe to understand purchase pattern based on education_level and marital_status
purchase_pattern = df1.groupby(by=["educational_level","marital_status"])[['online_purchases','store_purchases','complaints','recency']].sum()


# In[144]:


purchase_pattern


# In[145]:


#dataframe to understand income level of group based on education_level and marital_status
income = df1.groupby(by=["educational_level","marital_status"])[['annual_income']].mean()


# In[146]:


income


# In[147]:


purchase_pattern


# In[148]:


#joining both purchase_pattern and income dataset
new_df =pd.merge(purchase_pattern,income,on=['educational_level','marital_status'],how='inner')


# In[149]:


new_df


# # Analysing the dataset for insights

# In[150]:


new_df.online_purchases.sum()


# In[151]:


new_df.store_purchases.sum()


# In[160]:


new_df['total_purchase']=new_df.online_purchases+new_df.store_purchases #understading total purchase of various customer groups


# In[163]:


new_df.sort_values('recency',ascending=False)  #sorting the dataset based on recent purchases


# In[171]:


new_df.sort_values('total_purchase',ascending=False) #sorting based on total purchase pattern


# In[153]:


new_df.sort_values('annual_income',ascending=False) #sorting based on annual income of various customer groups


# In[174]:


new_df.sort_values('complaints',ascending=False) #sorting based on compliants by various customer groups


# # Insights Derived

# In[194]:


insights1 = new_df[['online_purchases','store_purchases']]
insights.plot.bar(figsize=(20,5))


# In[204]:


insights2 = new_df[['total_purchase','recency','complaints']]
insights2.plot.bar(figsize=(25,5))


# In[200]:


insights3 = new_df[['annual_income']]
insights3.plot.bar(figsize=(20,5))


# 1. In-store shopping has ~47% higher purchase rate by customers compared to online shopping
# 2. Graduates who are married hold the highest number of purchases,recency,complaints with their shopping
# 3. Customer groups with PhD have high annual income followed by those with Masters, Graduates, HighSchool, Basic

# In[ ]:




