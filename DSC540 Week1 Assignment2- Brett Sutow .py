#!/usr/bin/env python
# coding: utf-8

# In[6]:


import matplotlib.pyplot as plt
import pandas as pd


# In[27]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[30]:


wp= pd.read_excel('/Users/Brett/Desktop/world-population.xlsm')
x= wp.Year
y= wp.Population
plt.title('Population Changes')
plt.xlabel('Year')
plt.ylabel('Population')
plt.plot(x,y)


# In[ ]:




