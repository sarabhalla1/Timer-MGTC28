#!/usr/bin/env python
# coding: utf-8

# In[8]:


# This program for the Nerve of Steel game


import time # The time library has a sleep function that will pause the script for a specifized amount of time
import random #The random library will give a random number from 5-25 seconds 

def nerve_of_steel():
    print('Players Stand')
    time.sleep(random.randint(5,25))
    print ('Time up. Last to sit down wins')
    return input("Is the last player still standing? (yes/no): ").lower() == 'yes' #Asking the users if the last player is still standing or not

if nerve_of_steel():
    print("You win!")
else:
    print("You lose.")


# In[ ]:





# In[ ]:




