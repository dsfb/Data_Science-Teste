
# coding: utf-8

# In[1]:


import pandas as pd
house = pd.read_csv('house_infos.csv')


# In[2]:


print(house)


# In[3]:


cont =0
for i in range (0,1459):
        if ((house.loc[i][1]>5000) and (house.loc[i][7]=='N')):
            cont=cont+1
print('Quantidade de casas que possuem “LotArea” > 5000 e “CentralAir” = {}'.format(cont))


# In[4]:


copy = house.filter(items=['GrLivArea'])
copy = copy.loc[copy['GrLivArea']>2000]
copy


# In[5]:


copy["SalePrice"]=0
copy


# In[6]:


copy.shape


# In[7]:


cont=0
s=0
e=0
h=0
for e in range (0,214):
    for h in range (0,1459):
        if copy.index[e]==house.index[h]:
            s =  ((house.loc[h][0]+house.loc[h][1]+house.loc[h][6]+house.loc[h][8])*house.loc[h][3])
            copy['SalePrice'][h]=s
        


# In[8]:


copy


# In[9]:


copy["AvgOverallQual"]=0
copy


# In[10]:


cont=0
s=0
e=0
h=0
for e in range (0,214):
    for h in range (0,1459):
        if copy.index[e]==house.index[h]:
            s =  (house.loc[h][4]/house.loc[h][3])
            copy['AvgOverallQual'][h]=s


# In[11]:


copy


# In[12]:


import pandas as pd
year = pd.read_csv('year_condition.csv')
year


# In[13]:


result = pd.concat([year,copy])


# In[14]:


result

