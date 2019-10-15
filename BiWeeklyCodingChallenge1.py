
# coding: utf-8

# In[4]:


a=0
for i in range(5, 1001):
    if i%3==0 or i%5==0:
        a=a+i
print(a)

