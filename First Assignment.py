#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.Simple calculator for operators
a,b=8,3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print(a//b)


# In[4]:


#2.Simple interest
P=float(input('Enter the principle amount:'))
N=float(input('Enter the number of years:'))
R=float(input('Enter the rate of interest:'))
SI=(P*N*R)/100
print("Simple interest is",SI)


# In[6]:


#3.Area of a circle
r=float(input('Enter radius'))
Area=3.142*r**2
print('Area of circle is',Area)


# In[7]:


#4.Area of Triangle
a=float(input('enter 1st side of triangle'))
b=float(input('enter 2nd side of triangle'))
c=float(input('enter 3rd side of triangle'))
s=(a+b+c)/2
Area=(s-a)*(s-b)*(s-c)**0.5
print('Area of triangle',Area)


# In[8]:


#5.Area of Rectangle
I=float(input('Enter the length of rectangle'))
B=float(input('Enter the breath of rectangle'))
a=I*B
print('Area of rectangle:',a)


# In[9]:


#6.Celsius to Fahrenheit
C=float(input('enter value of celsius'))
F=(C*9/5)+32
print('temperature in fahernheit is',F)


# 

# In[11]:


#7.Perimeter of square
S=float(input("enter the side of a square"))
a=4*S
print('perimeter of square is:',a)


# In[14]:


#8.Circumference of a circle
r=float(input('enter the value radius'))
a=3.142*2*r
print('circumference of circle',a)


# In[15]:


#9.Snapping of two numbers
x=5
y=10
temp=x
x=y
y=temp
print(x,y)


# In[ ]:




