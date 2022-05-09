
# coding: utf-8

# # 赋值和拷贝
# 1.赋值是所有对象都是引用的，地址都一样
# 2.浅拷贝是拷贝对象地址有变化，但是子对象如果是可变对象如列表，地址不会改变。
# 3.深拷贝是对象和子对象全部拷贝，
# 4.-5到257的数字每次都是同一个内存地址，id(300)每次地址就不相同
# 5.可变对象，变量所指定的值可以改变,但是内存地址不可改变
# 6.如果对象或者子对象全部是不可变对象，则不需要拷贝

# In[19]:

import copy
a=[1,2000,3000,[4,5],6]
b=a
c=a.copy()
d=copy.deepcopy(a)
print(id(a),id(b),id(c),id(d))
print([id(i) for i in a])
print([id(i) for i in b])
print([id(i) for i in c])
print([id(i) for i in d])


# In[20]:

a.append(7)
a[1]=2
a[3].append(8)
print(id(a),id(b),id(c),id(d))
print(a)
print(b)
print(c)
print(d)


# In[ ]:




# In[ ]:



