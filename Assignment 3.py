#!/usr/bin/env python
# coding: utf-8

# In[3]:


#1.program to find area of circle in Python using math.
import math
r = float(input("Enter the radius of the circle: "))
area = math.pi* r **2
print("area of circle",area)


# In[2]:


#2.Area of rectangular polygon.
from math import tan, pi
n_sides = int(input("Input number of sides: "))
s_length = float(input("Input the length of a side: "))
p_area = n_sides * (s_length ** 2) / (4 * tan(pi / n_sides))
print("The area of the polygon is: ",p_area)


# In[4]:


#3.Area of a segment of a circle using math.
import math
t=float(input('enter the angle measured'))
r=float(input('enter the radius of circle'))
if t>=360:
    print('the angle is not possible')
else:
    a=(math.pi*(r**2)*(t/360))-((1/2)*(r**2)*math.sin((t*math.pi)/180))
    print('the area of segment=',a)


# In[11]:


#4.Generating a random number from the list.
import random
print('the random number from the list is')
print(random.choice([100,1,2,3,30,40]))


# In[12]:


#5.Generating random number b/w 1 to 10000 with difference 50.
import random
print('the random number b/w 1 to 10000',random.randrange(1,10000,50))


# In[14]:


#6.calcuate using math module.
import math
print('value of sin(60)is',math.sin(60))
print('value of cos(pi) is',math.cos(math.pi))
print('value of tan(90) is',math.tan(90))
print('value of sin(0.866024037844386) is',math.degrees(math.asin(0.866025037844)))
print('value of 5^8 is',5**8)
print('value of Square root of 400 is',math.sqrt(400))
print('value of 5^e is',5**math.e)
print('value of of log(1024) base 2 is',math.log(1024,(2)))
print('value of log(1024) base 10 is',math.log(1024,(10)))
print('the floor value of 23.56 is',math.floor(23,56))
print('the ceiling value of 23.56 is',math.ceil(23,56))


# In[ ]:




