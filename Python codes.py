#!/usr/bin/env python
# coding: utf-8

# # Data Types

# ## There are eight kinds of types supported by PyTables:
# 
# - bool: Boolean (true/false) types. Supported precisions: 8 (default) bits.
# - int: Signed integer types. Supported precisions: 8, 16, 32 (default) and 64 bits.
# - uint: Unsigned integer types. Supported precisions: 8, 16, 32 (default) and 64 bits.
# - float: Floating point types. Supported precisions: 16, 32, 64 (default) bits and extended precision floating point (see note on floating point types).
# - complex: Complex number types. Supported precisions: 64 (32+32), 128 (64+64, default) bits and extended precision complex (see note on floating point types).
# - string: Raw string types. Supported precisions: 8-bit positive multiples.
# - time: Data/time types. Supported precisions: 32 and 64 (default) bits.
# - enum: Enumerated types. Precision depends on base type.

# In[6]:






            a = "I am a Data Scientist"
            print(type(a))
            print(a)
            
            b=234
            print(type(b))
            print(b)




# In[10]:


        b = 5.9
        int(b)


# In[11]:


        a = 10
        b = 5.9
        print(a+b)
        print(a*b)
        print(a/b)
        print(a//b)
        print(a-b)


# In[13]:


           b = 3.9
           c = True
           print(b+c)
           d=False
           print(b+d)


# In[23]:


        d = '3'
        d
        a= 6
        
        
        a+int(d)


# In[4]:


                    a=3.5
                    b=5
                    print(type(a))
                    print(type(b))


# In[ ]:





# In[9]:


int(a) +b


# In[ ]:


bool(-10) * 3


# In[8]:


z = False
a*z


# In[10]:


a='I am a Data Scientist'
type(a)


# In[12]:


a=3
b=5.2
c = 20/6
c = 5 * False
c= 5* True


# In[11]:

                #%%
            c = 20/6
            c


# In[28]:


            stringvar = 'This is interesting. I am Reading python'
            e ="hi i"
            ee="hi   i"
            print(len(stringvar))
            print(len(e))
            print(len(ee))
            


# In[ ]:


            print(type(3))
            print(type(4.0))


# In[ ]:


        print(type(2))  # returns 'int’ 
        print(type(2.0)) # returns 'float’ 
        print(type('two')) # returns 'str’ 
        print(type(True)) # returns 'bool’ 
        print(type(None)) # returns 'NoneType'


# In[29]:


a=3.0
type(a)


# In[30]:


a


# In[36]:


            import datetime as d
            from datetime import date


# In[39]:


            td= date.today()

            print(td)
# In[40]:


            type(td)


# In[42]:


            someday = dt.date(2018,7,15)
            type(someday)


# In[43]:
/

            someday-td


# In[24]:


today = dt.date.today()
today


# In[22]:


from datetime import date
today = date.today()


# In[25]:


            from datetime import date
            from datetime import datetime
            
            today = date.today()
            print(today)
            print(datetime.now())
            datetime.


# In[28]:


            from datetime import date
            day1 = date(2010, 6, 20)

            data.today
# In[30]:


            day100 = today + dt.timedelta(days=100)


# In[32]:


day100.isoweekday()


# In[53]:


import datetime as dt
day1 = date(2010, 6, 20)
print(day1)

newdate = day1 + dt.timedelta(hours=10,minutes=40)


# In[40]:



import datetime

otherday = day1 + datetime.timedelta(days=400)
print(otherday)

my_bday = date(1978, 6, 10)

print(date.today()-my_bday)


# In[ ]:


my_birthday = date(today.year, 6, 24)
my_birthday = my_birthday.replace(year=today.year + 1)
print(my_birthday)

time_to_birthday = abs(my_birthday - today)
print(time_to_birthday.days)


# In[ ]:


print(date.today())
print(date.weekday(date.today()))
print(date.isoweekday(date.today()))
print(date.today())


# In[ ]:


date.today()


# # Math Operators

# In[44]:


            print(10 + 4) # add (returns 14) 
            print(10 - 4) # subtract (returns 6) 
            print(10 * 4) # multiply (returns 40) 
            print(10**4) # exponent (returns 10000) 
            print(10 / 4) # divide (returns 2.5) 
            print(5 % 4) # modulo (returns 1) - also known as the remainder


# # Logical / Comparision Operators

# In[45]:


# comparisons (these return True) 
            print(5 > 3 )
            print(5 >= 3)
            print(5 != 5)
            print(5 == 5) # boolean operations (these return True) 

# evaluation order: not, and, or


# In[50]:


False and -2.0

True and False
False and True


False or True

True or False

False or False


# In[46]:


print(5 > 3 and 6 < 3 )
True and False
print(5 > 3 or 5 < 3 )

True or False


# In[45]:


5 >= 3 or 6 > 100


# In[ ]:


val= input("enter a number")
print(val)

# # Conditional Statements

# In[62]:
i=val
if i>3:
     print(f"{i} is greater than 3")
else:
    print(f"{i} is lesser")
         
#%% 
            angle1 = 300
            angle2 = 20
            angle3 = 40
            
            
            if(angle1 + angle2 + angle3 == 180):
                print("Valid Triangle")
            
            elif(angle1 + angle2 + angle3==360):
                print("360 degree angle")
            else:
                print("invalid traingle")
                
                    
#%%
                
#x=int(input("enter a number"))                
x=-1

if ((x>0) or (x==-100)):
    print("X is positive Value or -100")
    print("I am if loop")
elif (x<0):
    print("I am in else if block")
    print("X is negative")
else:
    print("X is Zero")
    
print("I am out of IF looP")
    


# In[56]:


x = 6

if x%2 == 0 :
    print(x, " is even number")
    print("hello..")
else :
    print(x, " is ODD number")

print("this is out of IF else block")


# In[54]:
            
            
            x = -20
            # if/elif/else statement
            if x > 0:
                print('positive') 
                
            elif x == 0: 
                print('zero') 
            else: 
                print('negative') 
            #print("I am out of IF block")


# In[55]:


# single-line if statement (sometimes discouraged) 
            x=5
            if x > 0:
                print('positive') 


# # Lists
#  Python lists are very flexible and can hold completely heterogeneous, arbitrary data, and they can be appended to very efficiently.
#  

# In[67]:
                t1=(2,4,5,6,7)
                t2=(3,5,6,7,8)
                print(t1+t2)
                
                print(len(t1))
                
             
                
                
                t1=[2,3,4,5]
                t2=[5,6,7,8]
                print(t1+t2)
                t1.extend([3])
                
                
                tt1={"name":"Rohan","Marks":400}
                print(tt1)
                
                t1=np.array(t1)
                t2=np.array(t2)
                t1+t2
                t1*t2
                

            
            

# In[71]:
            my_list = [3,4.0,True,[8,9,90],"data science"]
            print(my_list)
            type(my_list)

my_list[4][2]
        


        


# In[85]:

months = ('January','February','March','April','May','June',\
'July','August','September','October','November','  December')
months.c


# In[86]:
myfamily = ['mom','dad','me']

myfamily.extend(['bro','sis','wife'])


# In[87]:


myfamily.append('cousin')


# In[89]:


myfamily.insert(8,"MP")
myfamily

# In[92]:


myfamily.pop(2)


# In[65]:


family.extend(['bro','uncle','aunt'])
family


# In[93]:


myfamily


# In[70]:


family.append('wife')
family


# In[75]:


family.insert(4,"sis")
family


# In[ ]:





# In[ ]:





# In[76]:


family.pop(3)


# In[77]:


family


# In[ ]:


## properties: ordered, iterable, mutable, can contain multiple data types       
# create an empty list (two ways) 
empty_list = [] 
empty_list = list() 
# create a list 
simpsons = ['homer', 'marge', 'bart']
# examine a list 
print(simpsons[0])        # print element 0 ('homer’) 
print(len(simpsons))    # returns the length (3)
 # modify a list (does not return the list) 
simpsons.append('lisa') # append element to end 
simpsons.extend(['itchy', 'scratchy'])  # append multiple elements to end 
print(simpsons)


# In[ ]:


family.remove('me')


# In[76]:


family.remove('me')


# In[80]:


family.pop(2)


# In[95]:


myfamily.sort()


# In[96]:


myfamily


# In[ ]:


simpsons.insert(0, 'maggie')  # insert element at index 0 (shifts ˓→everything right) 
print(simpsons)
simpsons.remove('bart')  # searches for first instance and removes it 
print(simpsons)
simpsons.pop(0) # removes element 0 and returns it del
print(simpsons)
simpsons[0] = 'krusty' # replace element 0
print(simpsons)


# # Tuples
# A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists. The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets. Creating a tuple is as simple as putting different comma-separated values.

# In[97]:


# create a tuple 
digits = (0, 1, 'two',0,1,1,1)  # create a tuple directly 
digits = tuple([0, 1, 'two'])  # create a tuple from a list 
# examine a tuple 
print(digits[2])  # returns ‘two’ 
print(len(digits)) # returns 3 
print(digits.count(0))  # counts the number of instances of that value (0) digits.index(1)  # returns the index of the first instance of that value (1) 

digits.


# In[84]:


# create a tuple 
digits1 = (0, 1, 'two',0,1,1,1)  # create a tuple directly 
# examine a tuple 
print(digits1.count(1))  # counts the number of instances of that value (0) digits.index(1)  # returns the index of the first instance of that value (1) 
len(digits1)


# In[ ]:


digits[1]= 'one' #returns an assignment error


# In[ ]:


my_tuple = (1,3.0,'works')
my_tuple
my_tuple2 = tuple(["this works too",8,10,True])
type(my_tuple2)


# # Strings

# In[ ]:


# create a string 
s = 'I like you' # examine a string 
s[0] # returns 'I’ 
len(s) # returns 10 
# string slicing like lists
s[:6] # returns 'I like’
s[7:] # returns 'you’
s[-1] # returns 'u' 


# In[105]:


        s = 'I am a Data Scientist'
        #s[:-9]
        s[-9:]


# In[88]:


        snew = 'Hello Data Science World'
        snew[-5:-2]


# In[94]:

        snew = 'Hello Data Science World'
        snew[2:5]


# # Dictionaries
# Python dictionary is an unordered collection of items. While other compound data types have only value as an element, a dictionary has a key: value pair.
# 
# Dictionaries are optimized to retrieve values when the key is known.

# In[114]:


# create an empty dictionary (two ways) 
            empty_dict = {} 
            empty_dict = dict() 
# create a dictionary (two ways) 


            my_pro = {'name':'Ashok', 'job':'Data Scientist', 'location':"bangalore", "years_exp":17} 
            my_dict = dict(name='Anand', age=30, job=['programmer','CEO','Data Scientist'], location="bangalore", years_Exp=17) 
    
    
            my_dict['name']


# # Sets
# A set contains an unordered collection of unique and immutable objects. The set data type is, as the name implies, a Python implementation of the sets as they are known from mathematics. This explains, why sets unlike lists or tuples can't have multiple occurrences of the same element.

# In[115]:


# create an empty set
empty_set = set()
# create a set
lang = {'python', 'r', 'java'} # create a set directly 
snakes = set(['cobra', 'viper', 'python','viper']) # create a set from a list 


# In[116]:


snakes.union(lang)


# In[117]:


snakes.intersection(lang)


# In[ ]:


# examine a set 

lang.intersection(snakes)


# In[ ]:


languages.union(snakes)


# In[ ]:


lang.


# # Functions

# In[ ]:





# In[128]:




# In[133]:


iseven(7,6)


# In[ ]:


# In[134]:


# alternative for loop (recommended style)
fruits = ['apple', 'banana', 'cherry','mango'] 

for x in fruits: 
	 print(x) 
    


# In[135]:


for x in range(10):
    print(x," hello")



# In[ ]:
    
import os
os.system('clear')

print(range(20))
#%%

for i in range(20):
    print(i)
#%%
for i in range(2,20,2):
    print(i)
#%%    
for i in range(3,20,3):
    print(i)    

#%%
# =============================================================================
# 
# =============================================================================

for i in range(1,11):
   print(f"5 * {i} = {5 * i}")

#%%
for i in range(1,10):
  print(i)
  print(2*i)

#%%
  
  import sklearn
  sklearn.cross_validation



#print(range(10))
#%%
#!/usr/bin/python

count = 0
while (count < 9):
   print( 'The count is:', count)
   count = count + 1

print ("Good bye!")
#%%

count = 0
while count < 5:
   print count, " is  less than 5"
   count = count + 1
else:
   print count, " is not less than 5"
#%%
#def forexample()
for i in range (1,11,2):
   print(i)
   
#forexample()   
 #%%  

def iseven(y,x=' '):
    if (x==' '):
        print("Please mention arg")
    elif (x%2==0):
        return True
    else:
        return False   
#%%

def print_hello_world_thrice():
     print("Hello World")
     print("Hello World")
     print("Hello World")

print_hello_world_thrice()

#%%



def print_hello_world(no_of_times):
    print("Hello World")
    print(no_of_times)
 
#print_hello_world()

print_hello_world(1)

#%%
def print_multiplication_table(table):
    
    for i in range(1,11):
        print(f"{table} * {i} = {table * i}")
#%%
print_multiplication_table(7)

#%%




# define a function with one argument and no return values 
def print_this(x): print(x) 

print_this(2)


# # Loops

#%%
class Planet:
   def __init__(self): 
 
Planet()

#%%
class Planet:
    def __init__(self):
        self.speed = 10
        self.name = "earth"
        self.distance_from_sun = 10000
 
earth = Planet()
#%%
earth.name
#%%

earth.speed

#%%

class Animal:
    def bark(self):
        print("bark")

animal = Animal()

animal.bark()

#%%
# Open File/Resource

try:
    # Business Logic to read
    i = 0 # Not hardcoded, getting a input from user
    j = 10/i
    values = [1,2]
    sum(values)
except TypeError:
    print("TypeError")
    j = 10
except ZeroDivisionError:
    print("ZeroDivisionError")
    j = 0
except:
    print("OtherError")
    j = 5
else:
    print("Else")
finally:
    # Close
    print("Finally")

print(j)
print("End")

#%%

try:
    sum([1,'1'])
except TypeError as error:
    print(error)
print("End")


# State

# make
# radius
# color
# speed
# is_on

# Behavior

# switch_on
# switch_off
# increase_speed
# decrease_speed
#%%
class Fan:
    def __init__(self, make, radius, color):
        self.make = make
        self.radius = radius
        self.color = color
        self.speed = 0
        self.is_on = False

    def __repr__(self):
        return repr((self.make,self.radius,self.color,self.speed,self.is_on))

    def switch_on(self):
        self.is_on = True
        self.speed = 3

    def switch_off(self):
        self.is_on = False
        self.speed = 0

# increase_speed
# decrease_speed


fan = Fan('Manufacturer 1', 5, 'Green')
fan.switch_on()
print(fan)
fan.switch_off()
print(fan)


#%%

#list coprehension
Syntax of List Comprehension
[expression for item in list]

#%%

[ x for x in range(20) if x % 2 == 0]

x
for x in range(20):
    if x%2==0:
        print(x)
  
    
    
#%%

li=[1,2,3,4,5,5]    

li*5
li+5
 #%%

li=["hi",33,44,566]
li=np.array(li)
newli=li.view()

print(newli)



newli[3]=67

newli

print(li)
    
 #%%
np.linspace(2,20,4)  
 #%%
 
 l1=[1,2,3,4,44556,6]

l1[:]
    
#%%

number_list = [ x for x in range(20) if x % 2 == 0]
print(number_list)

#%%
num_list = [y for y in range(100) if y % 2 == 0  if y % 5 == 0]
print(num_list)

#%%
obj = ["Even" if i%2==0 else "Odd" for i in range(10)]
print(obj)
#%%

#lambda arguments : expression
x = lambda a : a + 10
print(x(5))
#%%
x = lambda a, b : a * b
print(x(5, 6))