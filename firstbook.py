#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello Anaconda....")


# In[5]:


things = ['bmw',10,'car']


# In[6]:


print(things)


# In[7]:


print(things[1])


# In[8]:


car ='audi'


# In[10]:


things1=['ford',20,car]


# In[11]:


things1


# In[18]:


cars = {'audi', 'ford', 'bmw'}


# In[19]:


for i in range(cars):
    print('cars = ', i)


# In[24]:


for brand in cars:
    print(cars)


# In[29]:


index = 1 
while index < 10:
    print(index)
    index += 1


# In[30]:


len(cars)


# In[32]:


len(things)


# In[33]:


def say_hi():
    print('Hi from here, say what')


# In[34]:


say_hi()


# In[38]:


print("hello " + "edwin")


# In[44]:


print("hello", 5)


# In[46]:


print('hello ' + str(6))


# In[47]:


print('I\'m macbook air')


# In[48]:


print(7+7)


# In[51]:


print(1/7)


# In[53]:


print(5**3)
print((7+8)*6)


# In[54]:


name='macy'


# In[56]:


print(name)


# In[57]:


number=15


# In[68]:


print(number  + 5)


# In[85]:


list1= [78, 56, 6]


# In[86]:


list2 =[76, 54, 4]


# In[82]:


cars =['bwm','mercedes','honda','nissan','kia','ford']


# In[83]:


print(cars)


# In[84]:


print(cars[3])


# In[91]:


print(list2) 
print(list1)


# In[93]:


cars[0]='ferrari'


# In[94]:


print(cars)


# In[100]:


print(cars[2:])


# In[101]:


print(cars[:4])


# In[103]:


cars[1:3]= ['plane','cruise']


# In[104]:


cars


# In[108]:


print('not just cars') 
print(cars)


# In[110]:


cars.append('something else')


# In[111]:


cars


# In[112]:


print(cars)


# In[113]:


tuple_1 =('house','car','land')


# In[114]:


print(tuple_1)


# In[115]:


tuple_1[0] ='dog'


# In[116]:


number =(6,)


# In[117]:


number


# In[118]:


number2=(8,)


# In[119]:


number2


# In[121]:


print(number[0]+number2[0])


# In[122]:


book = {'chapter1':'prologue','chapter2':'The visit','chapter3':'The fight','chapter4':'epilogue'}


# In[126]:


book['chapter2']


# In[127]:


print(book['chapter3'])


# In[2]:


number1=12


# In[3]:


number2=13


# In[4]:


if number1>number2:
    print('number1 is greater then number2')
elif number1<number2:
    print('number1 is smaller than number2')
else:
    print('both are same')


# In[10]:


starter=5
while starter<=50:
    print(starter)
    starter +=5


# In[1]:


5*6


# In[2]:


students=['Peter','John','Maria','steph','lucy']


# In[3]:


for value in students:
    print(value)


# In[5]:


for v in range(1, 10):
    print(v)


# In[6]:


string ='hey, its python here and its a string'


# In[11]:


for x in string:
    if x=='r':
        break
    print(x)


# In[12]:


for y in string:
    if y=='s':
        continue
    print(y)


# In[15]:


def hello():
    print("welcome to the world of programming")
    print('this is going to be amazing')
    print('Just stay put and smile')


# In[16]:


hello()


# In[17]:


def get_url(website):
    print(website)
get_url('myhomeorg.com')


# In[24]:


def get_url(website):
    if website =='myhomeorg.com':
        print(website + ' is the official website. Please check it out..')
get_url('myhomeorg.com')


# In[29]:


def globalfun():
    global s
    s ='this is a string from inside the function'
    print(s)

s='this is a string from outside the function'
globalfun()
print(s)


# In[30]:


def calculate_number(num1,num2):
    total = num1+num2
    print(total)

calculate_number(56,44)


# In[31]:


calculate_number(7,5)


# In[34]:


def calculate_num(num1,num2):
    total1 = num1+num2
    return total1
total2 = calculate_num(56,45)
number3= 200
print(total2+number3)


# In[35]:


print(number3 - total2)


# In[36]:


def flexible_args(*arguments):
    total = 0
    for x in arguments:
        total += x
        print(total)


# In[37]:


flexible_args(50)


# In[40]:


flexible_args(30,30,50,365,2873278,9887545677,7461961619)


# In[41]:


def area_square(width,length):
    area = width * length
    print(area)


# In[43]:


area_square(5,5)


# In[48]:


square_area = [20,30]


# In[49]:


area_square(square_area[0], square_area[1])


# In[50]:


area_square(*square_area)


# In[57]:


pow(4,5)


# In[60]:


import math
float_number = 3.5
print(math.ceil(float_number))


# In[61]:


print(math.floor(float_number))


# In[62]:


file = open('example.txt', 'w')
file.write('I love python because I can do anything with it')
file.close()


# In[64]:


file = open('example.txt', 'r')
content = file.read()
print(content)


# In[1]:


file = open('torename.txt', 'w')
file.write('I want to learn it')
file.close()


# In[2]:


import os
os.rename('torename.txt', 'renamed.txt')


# In[4]:


import os 
os.remove('renamed.txt')


# In[5]:


l = [1,2,3]


# This is a markdown text. Do write your comments here!!

# In[ ]:




