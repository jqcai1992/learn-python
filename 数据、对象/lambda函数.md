
# map，lambda，sort，filter函数
1.函数如果不是很复杂，用lambda匿名函数更加简便
2.复杂函数最好还是用def定义，用lambda和列表推导就太臃肿
3.map由于返回的是迭代器，因此速度更快，map优于列表推导优于循环
4.lambda越用越慢，因此map+函数定义可能更好
5.迭代器除了用for in调用，还可以用next(iterator)




```python
def fn(x,y):
    return x**2+y**2
z1=map(fn,[1,2,3],[1,2,3])
z2=map(lambda x,y:x**2+y**2,[1,2,3],[1,2,3] )

print([i for i in zip(z1,z2)])
```

    [(2, 2), (8, 8), (18, 18)]
    


```python
import time
 
x=[]
x1=[]
x2=[]
 
for i in range(1000000):
    x.append(i)
    x1.append(i)
    x2.append(i)
    
def fn(x):
    return x+1

start1=time.clock()
for i in range(len(x)):
    x[i] += 1
end1=time.clock()
print(end1-start1)

start3=time.clock()
y3 = [a + 1 for a in x2]
end3=time.clock()
print(end3-start3)

start2=time.clock()
y = map(lambda a: a + 1, x1)
end2=time.clock()
print(end2-start2) 

start2=time.clock()
y = map(fn, x1)
end2=time.clock()
print(end2-start2)
```

    0.3948590999999997
    0.3597075999999997
    0.024365999999999666
    0.00015350000000013964
    

## filter，对指定函数进行过滤


```python
f1=filter(lambda x:x%2==1,[1,2,3,4])
print([i for i in f1])
```

    [1, 3]
    

## sorted(iterable, key=None, reverse=False)  


```python
a={'a':3,'d':6,'b':4}
sorted(a)
print(sorted(a,key=lambda x:x*-1))
print(sorted(a,key=lambda x:a[x]))
```

    ['b', 'a', 'd']
    ['a', 'b', 'd']
    


```python
b=['az','by','cx']
print(sorted(b,key=lambda x:x[::-1]))
```

    ['cx', 'by', 'az']
    


```python

```
