#!/usr/bin/env python
# coding: utf-8

# # Introduction

# Since I've been working on a lot of Kaggle competitions, I use Pandas quite a bit. As you may know, Pandas (in addition to Numpy) is the go-to Python library for all your data science needs. It helps with dealing with input data in CSV formats and with transforming your data into a form where it can be inputted into ML models. However, getting comfortable with the ideas of dataframes, slicing, etc was very tough for me in the beginning. Hopefully, this short tutorial can show you a lot of different commands that will help you gain the most insights into your dataset. 

# In[1]:


import pandas as pd



# # Loading in Data

# The first step in any ML problem is identifying what format your data is in, and then loading it into whatever framework you're using. For Kaggle compeitions, a lot of data can be found in CSV files, so that's the example we're going to use. 

# Since I'm a huge sports fan, we're going to be looking at a sports dataset that shows the results from NCAA basketball games from 1985 to 2016. This dataset is in a CSV file, and the function we're going to use to read in the file is called **pd.read_csv()**. This function returns a **dataframe** variable. The dataframe is the golden jewel data structure for Pandas. It is defined as "a two-dimensional size-mutable, potentially heterogeneous tabular data structure with labeled axes (rows and columns)".

# Just think of it as a table for now. 

# In[2]:


df = pd.read_csv('RegularSeasonCompactResults.csv')


# # The Basics

# Now that we have our dataframe in our variable df, let's look at what it contains. We can use the function **head()** to see the first couple rows of the dataframe (or the function **tail()** to see the last few rows).

# In[3]:


df.head()


# In[4]:


df.tail()


# We can see the dimensions of the dataframe using the the **shape** attribute

# In[5]:


df.shape

#%%

df.columns
# We can also extract all the column names as a list, by using the **columns** attribute and can extract the rows with the **index** attribute

# In[6]:


df.columns.tolist()


# In order to get a better idea of the type of data that we are dealing with, we can call the **describe()** function to see statistics like mean, min, etc about each column of the dataset. 

# In[7]:


df.describe()
#%%

df.info()

# Okay, so now let's looking at information that we want to extract from the dataframe. Let's say I wanted to know the max value of a certain column. The function **max()** will show you the maximum values of all columns

# In[8]:


df.max()
#%%

df.min()
#%%

df.mean()

#%%

df.mode()
#%%

df.median()


# Then, if you'd like to specifically get the max value for a particular column, you pass in the name of the column using the bracket indexing operator

# In[9]:

df['Daynum']

#%%

df['Wscore'].max()
#%%
df['Wscore'].min()


# If you'd like to find the mean of the Losing teams' score. 

# In[10]:


df['Lscore'].mean()



# In[11]:
# But what if that's not enough? Let's say we want to actually see the game(row) where this max score happened. We can call the **argmax()** function to identify the row index


df['Wscore'].argmax()
#%%
df['Wscore'].idxmax()


df['Season'].idxmax()



# In[12]:
# One of the most useful functions that you can call on certain columns in a dataframe is the **value_counts()** function. It shows how many times each item appears in the column. This particular command shows the number of games in each season


df['Season'].value_counts()



# In[13]:
# # Acessing Values

# Then, in order to get attributes about the game, we need to use the **iloc[]** function. Iloc is definitely one of the more important functions. The main idea is that you want to use it whenever you have the integer index of a certain row that you want to access. As per Pandas documentation, iloc is an "integer-location based indexing for selection by position."


df.iloc[[df['Wscore'].argmax()]]



# In[14]:
# Let's take this a step further. Let's say you want to know the game with the highest scoring winning team (this is what we just calculated), but you then want to know how many points the losing team scored. 

#%%
df.iloc[[df['Wscore'].idxmax()]]['Lscore']

df.iloc[[df['Wscore'].idxmax()]][['Lscore','Wteam']]

df.iloc[[df['Wscore'].idxmax()]][['Wscore','Lscore','Wteam']]

# In[15]:
# When you see data displayed in the above format, you're dealing with a Pandas **Series** object, not a dataframe object.


type(df.iloc[[df['Wscore'].argmax()]]['Lscore'])


# In[16]:


type(df.iloc[[df['Wscore'].argmax()]])



# In[17]:
# The following is a summary of the 3 data structures in Pandas (Haven't ever really used Panels yet)
# 
# ![](DataStructures.png)

# When you want to access values in a Series, you'll want to just treat the Series like a Python dictionary, so you'd access the value according to its key (which is normally an integer index)


df.iloc[[df['Wscore'].argmax()]]['Lscore'][24970]


#
# In[18]:
 #The other really important function in Pandas is the **loc** function. Contrary to iloc, which is an integer based indexing, loc is a "Purely label-location based indexer for selection by label". Since all the games are ordered from 0 to 145288, iloc and loc are going to be pretty interchangable in this type of dataset


df.iloc[:3]


# In[19]:


df.loc[:3]



# In[20]:
# Notice the slight difference in that iloc is exclusive of the second number, while loc is inclusive. 

# Below is an example of how you can use loc to acheive the same task as we did previously with iloc


df.loc[df['Wscore'].argmax(), 'Lscore']



# In[21]:
# A faster version uses the **at()** function. At() is really useful wheneever you know the row label and the column label of the particular value that you want to get. 


df.at[df['Wscore'].argmax(), 'Lscore']


# If you'd like to see more discussion on how loc and iloc are different, check out this great Stack Overflow post: http://stackoverflow.com/questions/31593201/pandas-iloc-vs-ix-vs-loc-explanation. Just remember that **iloc looks at position** and **loc looks at labels**. Loc becomes very important when your row labels aren't integers. 

# # Sorting

# Let's say that we want to sort the dataframe in increasing order for the scores of the losing team

# In[22]:


df.sort_values('Lscore').head()


# In[23]:


df.groupby('Lscore')



# In[24]:
# # Filtering Rows Conditionally

# Now, let's say we want to find all of the rows that satisy a particular condition. For example, I want to find all of the games where the winning team scored more than 150 points. The idea behind this command is you want to access the column 'Wscore' of the dataframe df (df['Wscore']), find which entries are above 150 (df['Wscore'] > 150), and then returns only those specific rows in a dataframe format (df[df['Wscore'] > 150]).

df[df['Wscore'] > 150]



# In[25]:
# This also works if you have multiple conditions. Let's say we want to find out when the winning team scores more than 150 points and when the losing team scores below 100. 


df[(df['Wscore'] > 150) & (df['Lscore'] < 100)]

#%%

df[(df['Lscore']==84)]
#%%
df[(df['Wscore']>150) & (df['Lscore']==99)]
#%%

df[(df['Wscore']==159) & (df['Lscore']==86)]

#%%
s = pd.Series(range(5))
print(s)


# In[26]:
s = pd.Series(range(5))
print(s)
s.where(s > 1)
#%%
s1 = pd.Series(range(5))
s1.where(s > 1, 4)

print(df)
#%%

df1 = pd.DataFrame(np.arange(10).reshape(-1, 2), columns=['A', 'B'])
print(df1)
m = df1 % 3 == 0
df1.where(m, -df1)
#%%
s.mask(s > 1)
#%%
df2 = pd.DataFrame([[4, 9],] * 6, columns=['A', 'B'])

df0 = pd.DataFrame([[4, 9],], columns=['A', 'B'])
print(df0)

print("----------")
print(df2)

#df1.apply(np.sqrt)
#%%
print(df1)
df1.apply(np.sum, axis=0)
#%%

df1.apply(np.sum, axis=1)
#%%
#Retuning a list-like will result in a Series
df2.apply(lambda x: [1, 2], axis=1)
#print(df2)
#%%

df2.apply(lambda x: pd.Series([1, 2], index=['foo', 'bar']), axis=1)

#%%

#Apply a function to a Dataframe elementwise.

df3 = pd.DataFrame([[1, 2.12], [3.356, 4.567]])
print(df3)
df3.applymap(lambda x: len(str(x)))
#%%
df3.applymap(lambda x: x**2)

#%%

df4 = pd.DataFrame([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
                   [np.nan, np.nan, np.nan]],
                   columns=['A', 'B', 'C'])
print(df4)

df4.agg(['sum', 'min'])

#%%
df4.agg("mean", axis="columns")
#%%
df4.agg("mean", axis=1)


#%%
# # Grouping

# Another important function in Pandas is **groupby()**. This is a function that allows you to group entries by certain attributes (e.g Grouping entries by Wteam number) and then perform operations on them. The following function groups all the entries (games) with the same Wteam number and finds the mean for each group. 

df.groupby('Wteam')['Wscore'].mean()
#%%
df.groupby('Wteam')['Wscore'].mean().head()



# In[27]:

# This next command groups all the games with the same Wteam number and finds where how many times that specific team won at home, on the road, or at a neutral site

df.groupby('Wteam')['Wloc'].value_counts().head(9)



# In[28]:
# Each dataframe has a **values** attribute which is useful because it basically displays your dataframe in a numpy array style format


df.values



# In[29]:
# Now, you can simply just access elements like you would in an array. 


df.values[0][0]
#%%
df.values[0][1]

#%%
df.values[0][2]
#%%

df.values[2][0]


# In[30]:

# # Dataframe Iteration

# In order to iterate through dataframes, we can use the **iterrows()** function. Below is an example of what the first two rows look like. Each row in iterrows is a Series object

for index, row in df.iterrows():
    print (row)
    if index == 1:
        break



# In[31]:
# # Extracting Rows and Columns

# The bracket indexing operator is one way to extract certain columns from a dataframe.


df[['Wscore', 'Lscore']].head()



# In[32]:
# Notice that you can acheive the same result by using the loc function. Loc is a veryyyy versatile function that can help you in a lot of accessing and extracting tasks. 


df.loc[:, ['Wscore', 'Lscore']].head()



# In[33]:
# Note the difference is the return types when you use brackets and when you use double brackets. 


type(df['Wscore'])


# In[34]:


type(df[['Wscore']])



# In[35]:
# You've seen before that you can access columns through df['col name']. You can access rows by using slicing operations. 


df[0:3]



# In[36]:
# Here's an equivalent using iloc


df.iloc[0:3,:]



# In[37]:
# # Data Cleaning

# One of the big jobs of doing well in Kaggle competitions is that of data cleaning. A lot of times, the CSV file you're given (especially like in the Titanic dataset), you'll have a lot of missing values in the dataset, which you have to identify. The following **isnull** function will figure out if there are any missing values in the dataframe, and will then sum up the total for each column. In this case, we have a pretty clean dataset.


df.isnull().sum()


# If you do end up having missing values in your datasets, be sure to get familiar with these two functions. 
# * **dropna()** - This function allows you to drop all(or some) of the rows that have missing values. 
# * **fillna()** - This function allows you replace the rows that have missing values with the value that you pass in.
#%%
# * **drop_duplicates()** - Lets you remove identical rows
df.drop_duplicates()
# In[38]:
# * **drop()** - This function removes the column or row that you pass in (You also have the specify the axis). 
df.drop(0)
#%%
#** pop( ) method return popped item data

df.pop('Wscore')

#%%
# * **agg()** - The aggregate function lets you compute summary statistics about each group

df.agg(0)
#%%
# * **apply()** - Lets you apply a specific function to any/all elements in a Dataframe or Series
# * **get_dummies()** - Helpful for turning categorical data into one hot vectors.
# * **drop_duplicates()** - Lets you remove identical rows
# # Visualizing Data

# An interesting way of displaying Dataframes is through matplotlib. 

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[39]:


ax = df['Wscore'].plot.hist(bins=20)
ax.set_xlabel('Points for Winning Team')



# In[40]:
# # Creating Kaggle Submission CSVs

# This isn't directly Pandas related, but I assume that most people who use Pandas probably do a lot of Kaggle competitions as well. As you probably know, Kaggle competitions require you to create a CSV of your predictions. Here's some starter code that can help you create that csv file


import numpy as np
import csv

results = [[0,10],[1,15],[2,20]]
results = pd.np.array(results)
print( results)


# In[41]:


firstRow = [['id', 'pred']]
with open("result.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(firstRow)
    writer.writerows(results)


# The approach I described above deals more with python lists and numpy. If you want a purely Pandas based approach, take a look at this video: https://www.youtube.com/watch?v=ylRlGCtAtiE&list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y&index=22

# # Other Useful Functions

# * **drop()** - This function removes the column or row that you pass in (You also have the specify the axis). 
# * **agg()** - The aggregate function lets you compute summary statistics about each group
# * **apply()** - Lets you apply a specific function to any/all elements in a Dataframe or Series
# * **get_dummies()** - Helpful for turning categorical data into one hot vectors.
# * **drop_duplicates()** - Lets you remove identical rows

# # Lots of Other Great Resources

# Pandas has been around for a while and there are a lot of other good resources if you're still interested on getting the most out of this library. 
# * http://pandas.pydata.org/pandas-docs/stable/10min.html
# * https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python
# * http://www.gregreda.com/2013/10/26/intro-to-pandas-data-structures/
# * https://www.dataquest.io/blog/pandas-python-tutorial/
# * https://drive.google.com/file/d/0ByIrJAE4KMTtTUtiVExiUGVkRkE/view
# * https://www.youtube.com/playlist?list=PL5-da3qGB5ICCsgW1MxlZ0Hq8LL5U3u9y

