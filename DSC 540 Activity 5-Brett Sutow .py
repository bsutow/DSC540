#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from sklearn.datasets import load_boston
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


#Uploads data#
boston= pd.read_csv('/Users/Brett/Documents/GitHub/Packt-Data_Wrangling/Lesson 4/Boston_housing.csv')
boston


# In[4]:


#Prints first 10#
boston.head(10)


# In[6]:


#Provides shape of df#
boston.shape


# In[8]:


#New df#
boston1= boston[['CRIM','ZN','INDUS', 'RM', 'AGE','DIS','RAD','TAX','PTRATIO','PRICE']]
boston1


# In[9]:


#Last 7#
boston1.tail(7)


# In[16]:


#All histograms without FOR loop#
print(plt.hist(boston1['CRIM'], bins=20))


# In[17]:


print(plt.hist(boston1['ZN'], bins=20))


# In[18]:


print(plt.hist(boston1['INDUS'], bins=20))


# In[19]:


print(plt.hist(boston1['RM'], bins=20))


# In[20]:


print(plt.hist(boston1['AGE'], bins=20))


# In[21]:


print(plt.hist(boston1['DIS'], bins=20))


# In[22]:


print(plt.hist(boston1['RAD'], bins=20))


# In[23]:


print(plt.hist(boston1['TAX'], bins=20))


# In[24]:


print(plt.hist(boston1['PTRATIO'], bins=20))


# In[25]:


print(plt.hist(boston1['PRICE'], bins=20))


# In[27]:


#For loop to plot all histograms#
for a in boston1.columns:
    plt.title('Plot:' +a)
    plt.hist(boston1[a], bins=20)
    plt.show()


# In[32]:


#Scatter plot comparing crime and price#
plt.scatter(x=boston1['CRIM'], y=boston1['PRICE'],color='purple')
plt.xlabel('Crime')
plt.ylabel('Price')
plt.title('Crime Rate vs Price')


# In[33]:


#Log scatterplot#
plt.scatter(x=np.log10(boston1['CRIM']), y=boston1['PRICE'],color='purple')
plt.xlabel('Crime')
plt.ylabel('Price')
plt.title('Crime Rate vs Price')


# In[45]:


#Prints all descriptive statistics#

crim=boston1['CRIM']
zn=boston1['ZN']
indus = boston1['INDUS']
rm = boston1['RM']
age= boston1['AGE']
dis=boston1['DIS']
rad=boston1['RAD']
tax=boston1['TAX']
ptratio=boston1['PTRATIO']
price=boston1['PRICE']

print(crim.describe())
print(zn.describe())
print(indus.describe())
print(rm.describe())
print(age.describe())
print(dis.describe())
print(rad.describe())
print(tax.describe())
print(ptratio.describe())
print(price.describe())


# In[48]:


#Calculates prices under 20k and then averages them out to find percentage of houses#
hp=price<20
hp


# In[50]:


avecost=hp.sum()/506
avecost


# In[51]:


avecost*100


# In[ ]:




