#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Create list#
list1= [15, 28, 42, -7]
print(list1)


# In[15]:


#Iterate over a list#
i = 0
while i < len(list1) :
    print(list1[i]) 
    i += 1


# In[17]:


#Sorts list highest to lowest#
list1.sort(reverse=True)
print(list1)


# In[18]:


#Sorts list by lowest to highest#
list1.sort(reverse=False)
print(list1)


# In[28]:


import random
list2=[random.randint(0,50)
for x in range (0,4)]
print(list2)


# In[29]:


list3 = list1+list2
print(list3)


# In[ ]:




