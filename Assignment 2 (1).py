#!/usr/bin/env python
# coding: utf-8

# In[2]:


#1.Program to check whether the person is eligible to vote or not
age = int(input("Enter Age : "))
if (age>=18):
        print('eligible to vote')
else:
    print('not eligible to vote')
    


# In[8]:


#2. To check whether the number is even or odd.
number=int(input('Enter the number:'))
if (number%2==0):
        print('number is even')
else: 
        print('number is odd')


# In[8]:


#3.Print the string in reverse order.
str="Python"  
slicedString=str[::-1] 
print (slicedString) 


# In[10]:


#4.num is +ve or not.
num=int(input('Enter the number'))
if num>=0:
    print('number is +ve')
else:
    print('number is not +ve')


# In[2]:


#5.find roots of quadratic eq using elif.
a = int(input("Enter a Value of a Quad Eq : "))
b = int(input("Enter b Value of a Quad Eq : "))
c = int(input("Enter c Value of a Quad Eq : "))

d = (b * b) - (4 * a * c)

r1=(-b+d)/2*a
r2=(-b-d)/2*a
if(d>0):
    print('roots are unequal')
elif(d<0):
    print('roots are imaginary')
elif(d==0):
    print('roots are same')


# In[4]:


#6.check num is +ve or -ve or zero using nested if.
x=int(input('Enter a number'))
if x>0:
    print('+ve')
if x<0:
    print('-ve')
elif x==0: 
    print('zero')


# In[4]:


#7.program to accept a number(1-5) and print the given number in words.
number=(" ","one","two","three","four","five")
n=int(input("Enter a number"))
print(number[n])


# In[3]:


#8.program to read a character and print the given character is vowel or consonant.

ch = input("Enter a character: ")

if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I'
 or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
    print(ch, "is a Vowel")
else:
    print(ch, "is a Consonant")

