#!/usr/bin/env python
# coding: utf-8

# In[1]:


"def"


# In[4]:


def test1():
    a = list(range(1,25,2))
    return a
test1()


# In[5]:


"it make a Python function flexible so it can accept a variable number of arguments and keyword arguments, "


# In[6]:


def add(*args):
    print(args, type(args))

add(2, 3)


# In[7]:


def total_fruits(**kwargs):
    print(kwargs, type(kwargs))


total_fruits(banana=5, mango=7, apple=8)


# In[12]:


l = [2, 4, 6, 8, 10, 12, 14,
16, 18, 20]
l[0:6]


# In[13]:


"A type of function that is memory efficient and can be used like an iterator object"


# In[14]:


"the yield keyword in Python controls the flow of a generator function."


# In[18]:


def mygenerator():
    print('First item')
    yield 10

    print('Second item')
    yield 20

    print('Last item')
    yield 30


# In[19]:


num = int(input("Enter the Fibonacci Number Range: "))

n1 = 0
n2 = 1
Sum = 0
i = 0

while(i <  num):
    print(n1, end = '  ')
    Sum = Sum + n1
    Next = n1 + n2
    n1 = n2
    n2 = Next
    i = i + 1
    
print("\nSum of Fibonacci Series Numbers: %d" %Sum)


# In[31]:


l = ["pwskills"]
l1 = []
for i in l:
    l1.append(i)
print(i)


# In[2]:


def check_palindrome(num):
  """
  This function checks whether a given number is a palindrome.
  """
  original_num = num
  reversed_num = 0
  while num > 0:
    remainder = num % 10
    reversed_num = reversed_num * 10 + remainder
    num //= 10
  return original_num == reversed_num

# Ask the user to enter a number
num = int(input("Enter a number: "))

# Check if the number is a palindrome
if check_palindrome(num):
  print(f"{num} is a palindrome")
else:
  print(f"{num} is not a palindrome")


# In[3]:


# List comprehension to print odd numbers from 1 to 100
odd_numbers = [x for x in range(1, 101) if x % 2 != 0]

# Print the list of odd numbers
print(odd_numbers)


# In[ ]:




