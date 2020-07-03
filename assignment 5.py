#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1. Length of a string
str=input("enter the string")
print('length of the input string is:',len(str))


# In[5]:


#2.Character frequency.
def char_frequency(str1):
    dict={}
    for n in str1:
        keys=dict.keys()
        if n in keys:
            dict[n]+=1
        else:
                dict[n]=1
    return dict
print(char_frequency("google.com"))


# In[6]:


# to find length without using len()
a="refrigerator"
count=0
for i in a:
    count=count+1
    print(count)


# In[7]:


#to print char of a string using loop
x=input('enter the string')
for i in x:
    print(i)


# In[8]:


# count a string in a list
str="apple, mango,banana"
print('list of iteam[str1.split('.')]')


# In[1]:


# string display in uppercase and lower case
user_input('what is your fav language')
print('my fav language is',user_input.upper())
print('my fav language is',user_input.lower())

