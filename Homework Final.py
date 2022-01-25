#!/usr/bin/env python
# coding: utf-8

# In[1]:


nums = list(range(30,65,5))
print(nums)


# In[2]:


print(nums[::-1])


# In[3]:


nums2 = nums[::-1]


# In[4]:


nums2.insert(0,65)
print(nums2)


# In[5]:


mt = list()
print(mt)


# In[6]:


for i in range (21):
    mt.append(i)
print(mt)


# In[7]:


mt.remove(0)
print(mt)


# In[8]:


print(len(mt))


# In[9]:


print(max(mt))


# In[10]:


print(min(mt))


# In[11]:


sum = sum(mt)
print(sum)


# In[12]:


weather = {"Sunny": "play", "Rainy": "watch TV", "Cloudy": "walk"}
print(weather)


# In[13]:


for x in weather:
  print("When " + str(x) + " let us " + str(weather[x]))


# In[14]:


weather.update({"snowy": "ski"})
print(weather)


# In[ ]:




