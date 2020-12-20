#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[4]:


#Creates Series1 and Series2 Indexing 
series1 = pd.Series([ 7.3 , -2.5 , 3.4 , 1.5 ], index= [ 'a' , 'c' , 'd' , 'e' ]) 
series2 = pd.Series ([ -2.1 , 3.6 , -1.5 , 4 , 3.1 ],index= [ 'a' , 'c' , 'e' , 'f' , 'g' ]) 


# In[5]:


#Adds the two series together
series1 + series2


# In[6]:


#Subtracts the two series 
series1 - series2


# In[ ]:




