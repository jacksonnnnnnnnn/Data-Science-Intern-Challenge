#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import library
import pandas as pd
import numpy as np


# In[3]:


#read the 2019 Winter Data Science Intern Challenge Data Set - Sheet1.csv File
#establish DataFrame to CSV

df = pd.read_csv("/Users/jacksonyoung/Downloads/2019 Winter Data Science Intern Challenge Data Set - Sheet1.csv")


# In[6]:


df


# In[8]:


# before cleaning data, I want to figure out the data information from the csv file
# get info from the data
df.info()


# In[ ]:


#1. Think about what could be going wrong with our calculation. Think about a better way to evaluate this data.

#   The calculation of AOV might get wrong because the total amount of orders 
#   might be calculated with the COUNT() function, so the total amount of orders will 
#   be the number of rows. I think when I  need to get total amount of orders
#   I would use SUM() function on total_items, then I’ll get the correct answer for AOV



#2. What metric would you report for this dataset?
# a. I need to figure out the SUM of total order amount
# b. I need to figure out the SUM of total order items


# In[10]:


# a. I need to figure out the SUM of total order amount
sum_oa = df['order_amount'].sum()
# b. I need to figure out the SUM of total order items
sum_ti = df['total_items'].sum()
print(sum_oa)
print(sum_ti)


# In[14]:


# now we know the sum of total order amount is 15725640
# and the total order items is 43936
# then we can calculate the AVO by dividing sum_oa by sum_ti
AOV = sum_oa / sum_ti
AOV = "%.2f" % AOV
print(AOV)


# In[ ]:




