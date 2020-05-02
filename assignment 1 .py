#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Task 1:
# Q. 1. Install Jupyter notebook and run the first program and share the screenshot of the output

print("ineuron")


# In[6]:


'''Q. 2. Write a program which will find all such numbers which are divisible by 7 but are not a multiple
of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a
comma-separated sequence on a single line.'''

for i in range(2000,3201):
    if i % 7 == 0 and i % 5 != 0:
        print(i,end=',')


# In[9]:


"""" Q. 3. Write a Python program to accept the user's first and last name and then getting them printed in
the the reverse order with a space between first name and last name."""

Name = input("Enter your first and second name: ").split()
for i in Name[::-1]:
    print(i,end=' ')


# In[13]:


""""Q. 4. Write a Python program to find the volume of a sphere with diameter 12 cm"""

Diameter = 12
Volume_Sphere = (4/3)* 3.14 * Diameter**3
print(Volume_Sphere)


# In[ ]:





# In[ ]:





# In[16]:


# Task 2:

'''''Q. 1. Write a program which accepts a sequence of comma-separated numbers from console and
generate a list'''''

Number = (input('Enter a number with comma-separated: ').split(','))
print(Number)


# In[25]:


'''Q. 2. Create the below pattern using nested for loop in Python.
                            *
                            * *
                            * * *
                            * * * *
                            * * * * *
                            * * * *
                            * * *
                            * *
                            *
'''

for i in range(9):
    for j in range(5):
        if (i in {0,8}) and (j in {0}):
            print('*',end=' ')
        elif (i in {1,7}) and (j in {0,1}):
            print('*', end =' ')
        elif (i in {2,6})and (j in {0,1,2}):
            print('*', end=' ')
        elif (i in {3, 5})and (j in {0,1,2,3}):
            print('*', end=' ')
        elif i ==4 and (j in {0,1,2,3,4}):
            print('*', end =' ')
        else: 
            print(' ', end= ' ')
    print()
            


# In[26]:


'''Q. 3.Write a Python program to reverse a word after accepting the input from the user.
        Sample Output:
        Input word: AcadGild
        Output: dilGdacA'''
a = input()
print(a[::-1])


# In[ ]:





# In[ ]:




