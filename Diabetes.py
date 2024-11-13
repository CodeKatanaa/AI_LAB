#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[2]:


pip install pandas


# In[4]:


df=pd.read_csv("diabetes.csv")


# In[5]:


df.head()


# In[6]:


df.shape


# In[7]:


df.isnull().sum()


# In[8]:


X=df.iloc[:,:-1].to_numpy()
y=df.iloc[:,-1].to_numpy()


# In[9]:


df.iloc[:,:-1]


# In[10]:


X


# In[11]:


y


# In[12]:


X=df.iloc[:,:-1].to_numpy()
y=df.iloc[:,-1].to_numpy()


# In[18]:


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)


# In[19]:


from sklearn.tree import DecisionTreeClassifier
clf=DecisionTreeClassifier(criterion="entropy",random_state=0)
clf.fit(X_train,y_train)


# In[24]:


import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')
from sklearn.tree import plot_tree
plt.figure(figsize=(20,10))


# In[21]:


pip install matplotlib


# In[32]:


plot_tree(clf,feature_names=['Glucose','BMI'],class_names=['No','Yes'])
plt.show()


# In[36]:


clf.set_params(max_depth=2)


# In[33]:


clf.fit(X_train,y_train)


# In[37]:


clf.fit(X_train,y_train)
plt.figure(figsize=(20,10))
plot_tree(clf,feature_names=['Glucose','BMI'],class_names=['No','Yes'])
plt.show()


# In[38]:


predictions=clf.predict(X_test)


# In[39]:


predictions


# In[40]:


clf.predict([[23,20],[200,35]])


# In[42]:


from sklearn import metrics
cf=metrics.confusion_matrix(y_test,predictions)
cf


# In[ ]:




