#!/usr/bin/env python
# coding: utf-8

# ## IPL EDA 

# In[19]:


import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


# In[4]:


ipl=pd.read_csv(r'C:\Users\Abhi\Downloads\matches.csv')


# In[5]:


ipl.head() #first five rows


# In[6]:


ipl.shape


# In[8]:


ipl['player_of_match'].value_counts() #determine most man of match by value


# In[9]:


ipl['player_of_match'].value_counts()[0:10] #top 10 player


# In[10]:


list(ipl['player_of_match'].value_counts()[0:10].keys()) #name of players


# In[31]:


plt.figure(figsize=(11,5))   #ploting top 10 man of match
plt.bar(list(ipl['player_of_match'].value_counts()[0:10].keys()),list(ipl['player_of_match'].value_counts()[0:10]),color ='b')
plt.title("Top 10 Man of match")
plt.xlabel("palyers")
plt.ylabel("frequency")


# In[20]:


ipl['result'].value_counts() #value of result column


# In[22]:


ipl['toss_winner'].value_counts().head() #teams won most no of toss


# In[25]:


Batting_first=ipl[ipl['win_by_runs']!=0] #detemine team that won by batting first
Batting_first.head()


# In[32]:


plt.figure(figsize=(7,7))
plt.hist(Batting_first["win_by_runs"])  #histogram of team win by runs
plt.title("Runs_Distribution")
plt.xlabel("Runs")
plt.ylabel("frequency")
plt.plot


# In[38]:


Batting_first["winner"].value_counts().head() #win by bat first top 5 teams


# In[54]:


plt.figure(figsize=(7,7)) 
plt.bar(list(Batting_first["winner"].value_counts()[0:3].keys()),list(Batting_first["winner"].value_counts()[0:3]),color=("blue","yellow","orange"))
plt.title("top 3 winning teams")
plt.xlabel("Teams")                             #top 3 winning team
plt.ylabel("no of win")


# In[64]:


plt.figure(figsize=(7,7))              #pie chart of teams winning by batting first
plt.pie(list(Batting_first["winner"].value_counts()),labels=list(Batting_first["winner"].value_counts().keys()))


# In[8]:


batting_secound = ipl[ipl["win_by_wickets"]!=0] #batting secound


# In[9]:


batting_secound.head() #top 5 teams win by batting secound


# In[13]:


plt.figure(figsize=(6,6))
plt.hist(batting_secound["win_by_wickets"],bins=30)      #histogram that determine the team winning freq
plt.xlabel("Teams")
plt.ylabel("frequency")
plt.show


# In[15]:


batting_secound["winner"].value_counts().head()   #top five team win by batting secound


# In[24]:


plt.figure(figsize=(5,5))
plt.bar(list(batting_secound["winner"].value_counts()[0:3].keys()),list(batting_secound["winner"].value_counts()[0:3]),color=["brown","blue","red"])
plt.xlabel("teams")
plt.ylabel("wining count")           #top 3 teams win by batting secound
plt.title("win by wicket")


# In[27]:


plt.figure(figsize=[5,5])
plt.pie(list(batting_secound["winner"].value_counts()),labels=list(batting_secound["winner"].value_counts().keys()),autopct='%0.1f%%')


# In[29]:


ipl["season"].value_counts() #no of matches played in each season


# In[30]:


ipl["city"].value_counts() #city with no of matches played


# In[32]:


import numpy as np                                  #count of win the match wrt tass win
np.sum(ipl["toss_winner"]==ipl["winner"])


# In[33]:


393/756 #ratio of winning by winning toss


# In[35]:


ipl["city"].unique() # differ cities where matches are held 


# In[40]:


city=ipl[ipl["city"]=="Mumbai"] # match that are played in mumbai


# In[42]:


city.head() #top 5 match played in mumbai


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




