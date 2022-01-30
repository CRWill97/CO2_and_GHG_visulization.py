#!/usr/bin/env python
# coding: utf-8

# GranulariTea Chemical Pollution Data
# 
# This data will be used as a visual for showing pollution per industry specifically in America. This data will show mainly a scope of chemical pollution and runoff by various sites across the US. Data cleaning and manip was needed to create the vertical bar charts. 

# In[69]:


import csv
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings(action='once')
import squarify


# In[70]:


ChemPolldf = pd.read_csv(r"C:\Users\willi\Documents\GranulariTea_Data\chemical_pollution.csv")


# In[71]:


print(ChemPolldf)


# In[72]:


ChemPolldf.drop('Unnamed: 0', inplace = True, axis = 1)


# In[73]:


ChemPolldf.drop('Unnamed: 0.1', inplace = True, axis = 1)


# In[74]:


print(ChemPolldf)


# In[75]:


ChemPoll_newdf = ChemPolldf[['industry sector', 'total releases']].groupby('industry sector').apply(lambda x: x.mean())
ChemPoll_newdf.sort_values('total releases', inplace = True)
ChemPoll_newdf.reset_index(inplace=True)


# In[76]:


ChemPoll_newdf = ChemPoll_newdf.rename(columns={"industry sector":"industry_sector", "total releases":"total_releases"})


# In[77]:


print(ChemPoll_newdf)


# In[81]:


chemHead = ChemPoll_newdf.head(15)


# In[80]:


chemTail = ChemPoll_newdf.tail(15)


# In[88]:


y_pos = np.arange(len(chemHead.industry_sector))
plt.barh(y_pos, chemHead.total_releases, align='center', alpha=0.5)
plt.yticks(y_pos, chemHead.industry_sector)
plt.xlabel('Chemical Runoff')
plt.title('Data taken from Toxic Release Inventory (TRI) of 2018 through the EPA website')
plt.savefig('Chem_head.png')


# In[89]:


y_pos = np.arange(len(chemTail.industry_sector))
plt.barh(y_pos, chemTail.total_releases, align='center', alpha=0.5)
plt.yticks(y_pos, chemTail.industry_sector)
plt.xlabel('Chemical Runoff')
plt.title('Data taken from Toxic Release Inventory (TRI) of 2018 through the EPA website')
plt.savefig('Chem_Tail.png')


# In[ ]:




