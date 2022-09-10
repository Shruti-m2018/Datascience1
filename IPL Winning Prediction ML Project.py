#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importing All Necessary Libraries of python #

import numpy as np


# In[2]:


import pandas as pd


# In[3]:


import matplotlib.pyplot as plt


# In[4]:


import seaborn as sns


# In[5]:


# Importing BOTH DataSets #
# Rectifying date datatype using parse_dates#

match_data=pd.read_csv('C:\\Users\\ML Projects\\IPL match ML\\IPL Matches 2008-2020.csv',parse_dates=['date'])
Ball_data= pd.read_csv('C:\\Users\\ML Projects\\IPL match ML\\IPL Ball-by-Ball 2008-2020.csv')


# In[6]:


# Showing Top 5 Rows od Datasets #
match_data.head()


# In[7]:


# Showing Top 5 Rows od Datasets #

Ball_data.head()


# In[8]:


# Viweing Null values in Ball dataset #

Ball_data.isnull().sum()


# In[9]:


# Viweing Null values in match dataset #

match_data.isnull().sum()


# In[10]:


# Viewing NUmber of rows & Columns of match dataset #

match_data.shape


# In[11]:


# Viewing NUmber of rows & Columns of ball dataset #

Ball_data.shape


# In[12]:


# Viewing  Columns name of match dataset #

match_data.columns


# In[13]:


# Printing Match , City , team Played data #

print('Matches Played so far :,match_data.shape[0]')
print('\n Cities played at:',match_data['city'].unique())
print('\n Team played at:',match_data['team1'].unique())


# In[14]:


# Viewing Data types of match Dataset #

match_data.dtypes


# In[15]:


# data type of match dataset date column #

type(match_data.date[2])


# In[16]:


# Creating New column Season in mactch Dataset #

match_data['Season']=pd.DatetimeIndex(match_data['date']).year
match_data.head()


# In[19]:


# Calculating Match Per season # 

match_per_season=match_data.groupby(['Season'])['id'].count().reset_index().rename(columns={'id':'matches'})
match_per_season


# In[22]:


# Creating Bar chart using seaborn library for data visulisation # 

sns.countplot(match_data['Season'])
plt.xticks(rotation=45,fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel('Season',fontsize=10)
plt.ylabel('count',fontsize=10)
plt.title('Total matches played in each season',fontsize=10,fontweight="bold")


# In[25]:


# Merging Match_data & Ball_data Using merge to make new dataset i.e.main_match_data #

main_match_data=match_data[['id','Season']].merge(Ball_data,left_on='id',right_on='id',how='left').drop('id',axis=1)
main_match_data.head()


# In[40]:


# Total run scored in each season #

TR_season=main_match_data.groupby(['Season'])['total_runs'].sum().reset_index()
p=TR_season.set_index('Season')
ax=plt.axes()
ax.set(facecolor="gray")
sns.lineplot(data=p,palette="magma")
plt.title('Total Runs In Each Season',fontsize=12,fontweight="bold")
plt.show()




# In[112]:


# Run score per Match each season #

runs_per_season=pd.concat([match_per_season,TR_season.iloc[:,1]],axis=1)
runs_per_season['Runs scored per match']=runs_per_season['total_runs']/runs_per_season['matches']
runs_per_season.set_index('Season',inplace=True)
runs_per_season



# In[48]:


# Number Of tosses won by each team #

toss=match_data['toss_winner'].value_counts()
ax=plt.axes()
ax.set(facecolor='grey')
sns.set(rc={'figure.figsize':(10,5)},style='darkgrid')
ax.set_title('No Of Tosses Won By Each Team',fontsize=15,fontweight="bold")
sns.barplot(y=toss.index,x=toss,orient='h',palette="icefire",saturation=1)
plt.xlabel('No of tosses won')
plt.ylabel('Teams')
plt.show()


# In[50]:


#  Toss decision across seasons #

ax=plt.axes()
ax.set(facecolor='grey')
sns.countplot(x='Season',hue='toss_decision',data=match_data,palette="magma",saturation=1)
plt.xticks(rotation=60,fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel('\n Season',fontsize=15)
plt.ylabel('\n Count',fontsize=15)
plt.title('Toss decision across season',fontsize=12,fontweight="bold")
plt.show()


# In[51]:


# No of results Count #

match_data['result'].value_counts()


# In[53]:


# Which stadium is best for winning by Wicket #

match_data.venue[match_data.result!='runs'].mode()


# In[54]:


# Which stadium is best for winning by Runs #

match_data.venue[match_data.result!='wickets'].mode()


# In[56]:


# For Any IPL Team Which stadium is best when  win the toss #

match_data.venue[match_data.toss_winner=='Kolkata Knight Riders'][match_data.toss_winner=='Kolkata Knight Riders'].mode()


# In[58]:


# Which is the best chasing Team that won the max number of matches batting Second #

match_data.winner[match_data.result!='runs'].mode()


# In[59]:


# Which is the best defending Team that won the max number of matches batting Dirst #

match_data.winner[match_data.result!='wickets'].mode()


# In[66]:


# Does Winning The Toss Means Winning The Match #


toss=match_data['toss_winner']==match_data['winner']
plt.figure(figsize=(10,5))
sns.countplot(toss)
plt.show()
                               


# In[68]:


# Does Coosing Batting or Balling  Means Winning The Match #

plt.figure(figsize=(12,4))
sns.countplot(match_data.toss_decision[match_data.toss_winner==match_data.winner])


# In[71]:


# How A Player Performed throughout The Match #

player=(Ball_data['batsman']=='SK Raina')
df_raina=Ball_data[player]
df_raina.head()


# In[75]:


# How Player dismissed Throughout The IPL in all the season # 

df_raina['dismissal_kind'].value_counts().plot.pie(autopct='%1.1f%%',shadow=True,rotatelabels=True)
plt.title('dismissal_kind',fontweight="bold",fontsize=25)


# In[80]:


# Runs Scored By player in 1,2,3,4,6 #

def count(df_raina,runs):
    return len(df_raina[df_raina['batsman_runs']==runs])*runs


# In[81]:


print("Runs scored from 1's/:",count(df_raina,1))
print("Runs scored from 2's/:",count(df_raina,2))
print("Runs scored from 3's/:",count(df_raina,3))
print("Runs scored from 4's/:",count(df_raina,4))
print("Runs scored from 5's/:",count(df_raina,6))


# In[83]:


#  Match having Biggest Win in terms of run margin # 

match_data[match_data['result_margin']==match_data['result_margin'].max()]


# In[90]:


# Players who scored max number of runs So far in IPL #

runs=Ball_data.groupby(['batsman'])['batsman_runs'].sum().reset_index()
runs.columns=['batsman','runs']
y=runs.sort_values(by='runs',ascending=False).head(10).reset_index().drop('index',axis=1)
y


# In[101]:


#  Top 10 Players who scored max number of runs Visulisation with Bar chart

ax=plt.axes()
ax.set(facecolor="grey")
sns.barplot(x=y['batsman'],y=y['runs'],palette='rocket',saturation=1)
plt.xticks(rotation=90,fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel('\n player',fontsize=15)
plt.ylabel('\n Total runs',fontsize=15)
plt.title('TOP 10 Runs scorer in IPL',fontsize=15,fontweight='bold')


# In[103]:


# Players who won 'Man of the match' max number of times #

ax=plt.axes()
ax.set(facecolor="black")
match_data.player_of_match.value_counts()[:10].plot(kind='bar')
plt.xlabel('players')
plt.ylabel("count")
plt.title("height mom award winning",fontsize=15,fontweight="bold")


# In[ ]:




