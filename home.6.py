#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1.Dictionary is a mutable data tyte in python. apython dictionary ia a collection of key and  value pairs separated by a color
mydict={'student': 'man', 'stuage':  '19', 'stucity': 'heaven'}
print("student age is :",mydict['stuage'])
print("student city is:",mydict['stucity'])


# In[ ]:


#2. to sum all the items in a list
def sum_list(item):
    sum_numbers=0
    for x in item:
        sum_numbers+=x
    return sum_numbers
print(sum_list([4,-20,3]))


# In[ ]:


# 3. create a list of empty dictionaries
n =4
l = [{} for _ in range(n)]
print(l)


# In[ ]:


# 4. Access dictionary keys element by index
num = {'physics': 80, 'math': 90, 'chemistry': 86}
print(list(num)[2])


# In[ ]:


# 5. python program to iterate over dictionaries using for loops
d = {'blue': 4, 'Green': 2, 'Blue': 3} 
for color_key, value in d.items():
     print(color_key, 'corresponds to ', d[color_key]) 


# In[ ]:


# 6. python program to sum all the items in a dictionary
my_dict = {'num1':10,'num2':-54,'num3':50}
print(sum(my_dict.values()))


# In[ ]:


# 7. concatenate dictionaries to create a new one 
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)


# In[ ]:


# 8. Expected result:{1:10,2:20,3:30,4:40,5:50,6:60}
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)


# In[ ]:


# 9. Create a tuple 
x = ()
print(x)


# In[ ]:


# 10. Create a tuple with different data types
tuplex = ("tuple", True, 4.2, 1)
print(tuplex)


# In[ ]:


# 11.covert a tuple to string 
tup = ('M','O','H','A','N')
str =  ''.join(tup)
print(str)


# In[ ]:


# 12. to slice a tuple
tuplex = ('M','O','h','a','n')
_slice = tuplex[2:]
print(_slice)


# In[ ]:


# 13. length of a tuple
tuplex = tuple("python")
print(tuplex)
print(len(tuplex))


# In[ ]:


# 14. convert a tuple to dictionary
tuplex = ((1, "v"),(4, "i"))
print(dict((y, x) for x, y in tuplex))


# In[ ]:


# 15. to reverse a tuple
x = (5, 10, 15, 20)
y = reversed(x)
print(tuple(y))


# In[ ]:


# 16. convert a list of tuples in to a dictionary
l = [("M", 1), ("o", 2), ("h", 3), ("a", 4), ("n", 5)]
d = {}
for a, b in l:
    d.setdefault(a, []).append(b)
print (d)


# In[ ]:


# 17.Convert list to tuple
listx = [5, 10, 7, 4, 15, 3]
tuplex = tuple(listx)
print(tuplex)


# In[ ]:




