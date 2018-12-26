#!/usr/bin/env python
# coding: utf-8

# In[53]:


x = [5,6,7,8,9]
x.sort(reverse=True)
print(x)

y = ['a','b','e','d']
y.sort()
print(y)


# In[8]:


y = ['a','b','e','d']
y.sort()
print(y)


# In[10]:


z = [1,9,6,'a','m']
#z.sort()

#String and integer cannot be compred
#cannot sort different datatypes


# In[15]:


x2 = [5,6,7,8,9]
sorted_x2 = sorted(x2, reverse=True) # reverse and store in variable.
print(sorted_x2)
print(x2)


# In[16]:


max(x2)


# In[19]:


min(x2)
sum(x2)


# In[21]:


min(y)


# In[23]:


#check whether an element is in the list or not
print(x2)
print(7 in x2)


# In[32]:


for n in x2:
    print(n, end = '\t')


# In[40]:


for index, n in enumerate(x2):
    print(index,n)


# In[37]:


for ind,n in enumerate(y):
    print(ind,n)


# In[41]:


for index, n in enumerate(x2, start=100):
    print(index,n)


# In[47]:


comp = ['OOP','CSA','NM','CS','MGMT','OS']

j_comp = "+".join(comp)
print(j_comp)


# In[48]:


j_comp.split('+')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




