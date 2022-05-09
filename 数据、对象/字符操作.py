
# coding: utf-8

# # 字符操作

# ## 1.strip和replace
# 只要位于序列中的字符全部删除

# In[29]:

a='000good morning000'
print(a.strip('0ing'))
print(a.lstrip('0ing'))
print(a.rstrip('0ing'))
print(a.replace('00','xx'))
print(a.replace('0',''))


# ## 2.大小写

# In[18]:

a='good morning'
print(a.upper())
print(a.upper().lower())
print(a.swapcase())


# ## 3.join函数

# In[19]:

a=[str(i) for i in range(5)]
'-'.join(a)


# ## 4. split函数

# In[22]:

a='a0b0c00'
print(a.split('0',2))
print(a.split('0'))


# ## 5. find,index,count
# find找不到返回-1，而index找不到会报错，所以一般不用index

# In[27]:

a='23jj22jjf'
print(a.find('j'))
print(a.index('j'))
print(a.count('j'))


# In[ ]:



