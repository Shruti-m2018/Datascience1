#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy as np
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# In[16]:


import nltk
nltk.download('stopwords')


# In[17]:


# Printing the stopwords in English
print(stopwords.words('english'))


# In[ ]:


# Data Preprocessing 


# In[19]:


# Loading to dataset to pandas Dataframe 
news_dataset1=pd.read_csv('C:\\Users\\Lenovo\\Downloads\\train.csv')


# In[20]:


news_dataset1.head()


# In[21]:


news_dataset1.shape


# In[22]:


news_dataset1.isnull().sum()


# In[23]:


# replacing the null value with empty string 

news_dataset1=news_dataset1.fillna('')


# In[26]:


# merging the authur name and news title 

news_dataset1['content']=news_dataset1['author']+''+news_dataset1['title']


# In[27]:


print(news_dataset1['content'])


# In[66]:


# Seperating the data & lable 

x=news_dataset1.drop(columns='label',axis=1)
y=news_dataset1['label']


# In[30]:


print(x)
print(y)


# In[67]:


# Stemming Procedure #

port_stem=PorterStemmer()


# In[38]:


def stemming(content):
    stemmed_content=re.sub('[^a-z,A-Z]','',content)
    stemmed_content=stemmed_content.lower()
    stemmed_content=stemmed_content.split()
    stemmed_content=[port_stem.stem(word) for word in stemmed_content if not word in stopwords.words('english')]
    stemmed_content=''.join(stemmed_content)
    return stemmed_content


# In[40]:


news_dataset1['content'] = news_dataset1['content'].apply(stemming)


# In[41]:


# Seprating the data and label 

x=news_dataset1['content'].values
y=news_dataset1['label'].values


# In[42]:


print(x)


# In[43]:


print(y)


# In[44]:


y.shape


# In[46]:


# Converting the textual data to numerical Data #

vectorizer=TfidfVectorizer()
vectorizer.fit(x)
x=vectorizer.transform(x)

print(x)


# In[48]:


# Splitting the dataset to training & test data 

x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.2,stratify=y,random_state=2)


# In[49]:


# Training the Model : Logistic Regression #


model=LogisticRegression()


# In[50]:


model.fit(x_train,y_train)


# In[51]:


# Accuracy score on training data #

x_train_prediction=model.predict(x_train)
training_data_accuracy=accuracy_score(x_train_prediction,y_train)


# In[52]:


print('Accuracy score of the training data :',training_data_accuracy)


# In[58]:


# Accuracy score on the test data 
x_test_prediction=model.predict(x_test)
test_data_accuracy=accuracy_score (x_train_prediction,y_train)


# In[59]:


print('Accuracy score on the training data :',test_data_accuracy)



# In[65]:


# Making a Predictive system

x_new=x_test[6]

prediction=model.predict(x_new)
print(prediction)

if (prediction[0]==0):
    print('The news is Real')
else:
    print('The news is Fake')
    
    
    
    


# In[ ]:




