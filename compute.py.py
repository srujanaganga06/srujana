#!/usr/bin/env python
# coding: utf-8

# In[ ]:


greet = lambda name : print(f"Good Night {name}!")


# In[2]:


greet("Srujana")


# In[3]:


average = lambda a, b, c: (a + b + c) / 3
result = average(10, 20, 30)
print(result)


# In[9]:


product = lambda a,b,c: a*b*c
product(20,30,40)


# In[11]:


even = lambda L : [x for x in L if x%2 ==0]
my_list = [100,8,5,79,567,78]
even(my_list)


# In[12]:


odd = lambda L : [x for x in L if x%2 ==1]
my_list = [100,8,5,79,567,78]
odd(my_list)


# In[14]:


def mean_value(*n):
    sum = 0
    counter = 0
    for x in n:
       counter = counter +1
       sum += x
    mean = sum /counter
    return mean


# In[32]:


#Find the product of given numbers
def product(*n):
    result = 1
    for number in n:
        result *= number
    return result
print(product(1,2,3,4))


# In[ ]:





# In[ ]:




