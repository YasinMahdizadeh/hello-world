#!/usr/bin/env python
# coding: utf-8

# In[15]:


def sum_list(i, mylist = []):
    n = len(mylist)
    if(i == n-1 ):
        return mylist[i]
    return mylist[i]+sum_list(i+1,mylist)


# In[17]:


sum_list(0,[4,5,6])


# In[ ]:




