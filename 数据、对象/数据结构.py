
# coding: utf-8

# 
# # 数据结构
# ## 0.四种数据结构

# In[15]:

print([1,2,3,[1,2],'a'])
print((1,2,3,(1,2)))
print({1:2,3:4})
print(dict(x=2,y=1))
print(set([1,2,3,1,2,4]))


# ## 1.列表
#     1.列表中元素可以不同，数字、字符或者列表，元组都行
#     2.索引、切片和嵌套本质差不多，都是a[1:2][1]调用，修改也可以用利用索引切片a[1:2]=[2,2]
#     3.in和for用法，既可以用于if a in b的判断，用可以for i in range（10）的循环
#     4.append是一个元素，extend是一群元素，注意append([1,2,3])是[1,2,3]加入这个列表，
#     而extend([1,2,3])是1,2,3加入列表.
#     5.count是统计出现次数，index是查看索引值，可用for i,num in enumerate(b)来查看所有索引和元素
#     6.列表解析，列表里嵌套循环和判断
#     7. 函数len(a),max(a),min(a),释放空间，不改变对象
#     8 方法是类里面的方法，会永久改变对象，比如a.pop(),a.extend(),a.insert(),a.pop(),a.remove(),a.sort()
#     9.dir()函数查看所有方法
#     
#     
# ### 1.索引、切片、嵌套、连接和修改

# In[2]:

a=[1,2,4,8,10,12,[1,2,3]]
print(a[0])
print(a[::-1])
print(a[:-1])
print(a[-1][-1])
print(a+a[::-1])
a[1:5]=[1,1,1,1,1]
print(a)


# ### 2. in、for循环

# In[22]:

b=[1,2,3,4,5]
print(6 in b)
print([i for i in b])


# ### 3.列表增加、删除

# In[13]:

c=[2,4,6]
c.append([2,3])
print(c)
c.extend([2,3])
print(c)
c.pop()
print(c)
c.pop(2)
print(c)
c.remove(2)
print(c)


# ### 4.排序、查看

# In[14]:

a=[1,4,2,3,6,2,3]
a.sort()
print(a)
print(a.count(2),a.count(3))


# # 2.元组
#     1.元组元素不可修改，不可进行增添，除非元组中有列表元素
#     2.单元素要用逗号，否则与小括号混淆，几个元素用逗号间隔不用小括号也是元组
#     3.函数的函数赋值和return本质也是元组 
#     4.for i,v in enumerate(a),本质也是元组
#     5.for i in range(20),遍历尽量用元组不用列表
#     6.几个元素间逗号默认为元组
# ## 1.任意变量交换数值

# In[10]:

a=1;b=2;c=3
b,c,a=c,a,b
print(a,b,c)


# ## 2. 函数赋值和return

# In[19]:

def max_min(t):
    return min(t),max(t)
max_min([1,4,8])


# ## 3.变量打印

# In[32]:

print('name:%s,age:%d' %('tom',30))


# ## 4.和zip一起构建字典，或者遍历enumerate

# In[31]:

a=['a','b','c']; b=[1,2,3]
c={}
for i,j in zip(a,b):
    c[i]=j
print(c)
d=dict(zip(a,b))
print(d)


# # 3.字典
# ## 1.字典定义
#     1.字典的key必须是字符串‘a’，数字3，或者元组（1,2）这三种
#     2.列表list不能，因为列表不是hashable

# In[64]:

print(dict(zip([1,2,3],[4,5,6])))
print(dict(a=2,b=4))
print({(1,2):2,3:4})
a={'a':1,'b':2}
for i in a:
    print(i)



# ## 2.keys，values，items

# In[11]:

a={1:2,3:4,5:6}
print([i for i in a.keys()])
print([i for i in a.values()])
print([(i,j) for i,j in a.items()])


# ## 3.get,setdefault,update

# In[20]:

b={'a':'b','c':'d'}
print(b.get('a'),b['a'])
print(b.get('b')) #b['b']会报错
a.update(b)
print(a)
b[2]=3
print(b)
b.setdefault(2,3)
print(b)


# # 4.集合
# 1.交集，并集，差集

# In[21]:

a={1,2,3}
b={3,4,5}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))


# In[ ]:



