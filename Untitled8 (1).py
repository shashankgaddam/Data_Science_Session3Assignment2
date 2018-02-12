
# coding: utf-8

# In[1]:


s = "ACADGILD"
svar = [t for t in s]


# In[2]:


svar


# In[51]:


a = "xyz"
l = [x*j for x in a for j in range(1,5)]


# In[52]:


l


# In[60]:


b = "xyz"
l = [x*j for j in range(1,5) for x in a]


# In[61]:


l


# In[76]:


l = [1,2,3]
c = [[x+i]  for i in range(1,4) for x in l ] 


# In[77]:


c


# In[78]:


l1 = [1,2,3,4]
v = [[x+i for i in range(1,5)] for x in l1]


# In[79]:


v


# In[82]:


x = [(i,j) for j in range(1,4) for i in range(1,4)] 


# In[83]:


x

