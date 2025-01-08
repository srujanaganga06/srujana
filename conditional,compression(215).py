#!/usr/bin/env python
# coding: utf-8

# In[1]:


num = 6
if num %2 == 0:
    print('even')
else:
    print('odd')


# In[4]:


print('even') if num % 2 == 0 else print('odd')


# In[5]:


print('odd') if num % 2 == 0 else print('even')


# In[10]:


num = 0
result = 'Positive' if num > 0 else('Negative' if num > 0 else 'Zero')
print(result)


# In[11]:


L = [1,9,2,10,56,89]
[2*x for x in L]


# In[12]:


L = [1,9,2,10,56,89]
[x for x in L if x%2 == 0]


# In[13]:


L = [1,9,2,10,56,89]
[x for x in L if x%2 == 1]


# In[20]:


L = [1,9,2,10,56,89]
sum([x for x in L])/len(L)


# In[21]:


d1 = {'Sri':[78,89,90,100], 'Nani':[56,98,78,67]}
d1


# In[22]:


{k:sum(v)/len(v) for k,v in d1.items()}


# In[ ]:




