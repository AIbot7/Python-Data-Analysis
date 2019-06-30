#!/usr/bin/env python
# coding: utf-8

# # Numpy Tutorial

# In[2]:


#Importing Numpy package
import numpy as np


# In[5]:


#Declaring simple array
a = np.array([2,3,4,6,2])
a


# In[6]:


#Initiating static two dimensional array
b = np.array([[2,3,4,6,2],[4,5,6,9,4]])
print(b)


# In[7]:


# ndim parameter to get dimension of array
b.ndim


# In[8]:


#array shape parameter to get shape of the array
a.shape


# In[11]:


print(a)


# In[15]:


#dtype parameter to get type of array
type(b)
b.dtype


# In[16]:


# auto type casting to higher data types as Array is homogenous
c = np.array([2,3,4.2,6,2])
c


# In[18]:


#Checking auto typecasting
c.dtype


# In[17]:


#string can be auto typecasted as well.
b = np.array([6, 7, 8.0,'a'])
print(b)


# In[ ]:


# array transforms sequences of sequences into two-dimensional arrays, sequences of sequences of sequences into three-dimensional arrays, and so on.
b = np.array([(1.5,2,3), (4,5,6)])
b


# In[7]:


#The type of the array can also be explicitly specified at creation time:
c = np.array( [ [1,2.2], [3,4] ], dtype=int )
c


# In[19]:


#The function zeros creates an array full of zeros
np.zeros( (3,4) )
np.ones( (3,4) )


# In[37]:


#arange function to create sequential array
data = np.arange(30)
data


# In[38]:


#reshape function to reshape array to the required dimension
data= data.reshape(6,5)

data
data1 = np.arange(10,100,5)


data1

# In[36]:


#more reshape examples
data1 = np.arange(10,100,5).reshape(6,3)
data2 = np.arange(110,200,5).reshape(6,3)
print(data1)
print(data2)


# In[21]:


data3= np.arange(18).reshape(6,3)
data3**15


# In[3]:


#creating array for spliting examples
a = np.arange(24).reshape(6,4)
a


# In[4]:


#horizontal splititing
a_hsplit = np.hsplit(a,2)
a_hsplit


# In[6]:


#Vertical split
a_vsplit=np.vsplit(a,2)
a_vsplit


# In[7]:


#creating arrays for stacking examples
a = np.arange(12).reshape(4,3)
b = np.arange(16,32).reshape(4,4)


# In[58]:


a


# In[59]:


b


# In[63]:


#combing arrays with vertical stacking
np.vstack((a,b))


# In[8]:


#combing arrays with hozontal stacking
np.hstack((a,b))


# In[32]:


#universal functions such as sqrt, sin, cos etc.,
print("Pi constant value : ",np.pi)  # pi constant
d = np.arange(0,120,30).reshape(2,2)  # array to apply sin cos
print("d array with angles in degrees")
print(d)
d_rad = d*np.pi/180 # converted angles to radians
print("d array with angles in radians")
print(d_rad)
print("Sin values of angles 0,30,60,90")
print(np.sin(d_rad))
print("Square root function on array")
e = np.array([4,9,16,25])
np.sqrt(e)


# In[40]:


#Numpy is capable of  huge Arrays manuplation very efficiently
a = np.arange(9000000).reshape(9000,1000)
a


# In[28]:


#shape manuplation
a = np.arange(4).reshape(2,2)
b = np.arange(11,15).reshape(2,2)
print(a)
print(b)


# In[42]:


#Generating random number with Numpy. random number are between 0 and 1
np.random.random()


# #### Random number functions in numpy.random
# rand(d0, d1, …, dn)	Random values in a given shape. <br\>
# randn(d0, d1, …, dn)	Return a sample (or samples) from the “standard normal” distribution.<br\>
# randint(low[, high, size, dtype])	Return random integers from low (inclusive) to high (exclusive).<br\>
# random_integers(low[, high, size])	Random integers of type np.int between low and high, inclusive.<br\>
# random_sample([size])	Return random floats in the half-open interval [0.0, 1.0).<br\>
# random([size])	Return random floats in the half-open interval [0.0, 1.0).<br\>
# ranf([size])	Return random floats in the half-open interval [0.0, 1.0).<br\>
# sample([size])	Return random floats in the half-open interval [0.0, 1.0).<br\>
# choice(a[, size, replace, p])	Generates a random sample from a given 1-D array<br\>
# bytes(length)	Return random bytes.
# 

# In[49]:


print("Random numbers with required shape")
print(np.random.rand(3,2))
print("random integers betweet two numbers with required size")
print(np.random.randint(10,50,10))


# In[52]:


#Numpy floor, ceil and round
print(np.floor(5.9))
print(np.ceil(3.3))
print(np.round(4.7))


# In[64]:


#Copies and Views

# No Copy at All¶

a = np.arange(12)
a


# In[65]:


b = a            # no new object is created
b


# In[66]:


a[5] = 160
a


# In[67]:


b


# In[ ]:


b.shape = 3,4    # changes the shape of a.shape(3, 4)


# In[ ]:


a.shape


# In[ ]:


c.base is a  
a.shape
a


# In[ ]:


c.shape = 2,6                      # a's shape doesn't change
print(a.shape)
c


# In[ ]:


c[0,4] = 999                    # a's data changes
c


# In[ ]:


a


# In[59]:


# Deep Copy

b = a.copy() 


# In[61]:


a[4] = 234
a


# In[62]:


b


# ## This completes basic tutorial on Numpy package

