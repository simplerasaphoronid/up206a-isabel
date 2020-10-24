#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[5]:


df = pd.read_csv('data/Route20CensusTracts.csv')


# In[6]:


df.shape


# In[7]:


df.head()


# In[8]:


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


# In[9]:


df.sample()


# In[10]:


df.info(verbose=True, null_counts=True)


# In[11]:


df.Geo_STATE.head()


# In[14]:


df=pd.read_csv(
    'data/Route20CensusTracts.csv',   
     dtype=
    {
        'Geo_FIPS':str,
        'Geo_STATE':str,
        'Geo_COUNTY': str
    }
)


# In[15]:


df.info(verbose=True, null_counts=True)


# In[16]:


df.columns[df.isna().all()].tolist()


# In[17]:


df = df.dropna(axis=1,how="all")


# In[18]:


df.head()


# In[20]:


df.shape


# In[21]:


columns_to_drop = ['Geo_GEOID','Geo_STUSAB','Geo_SUMLEV','Geo_GEOCOMP','Geo_FILEID','Geo_LOGRECNO']


# In[22]:


df = df.drop(columns_to_drop,axis=1)
df.head()


# In[23]:


columns_to_dropa = ['SE_A00002_001','SE_A00002_002','SE_A00002_003','SE_A02001_001']


# In[24]:


df = df.drop(columns_to_dropa,axis=1)


# In[25]:


df.shape


# In[26]:


columns_to_dropb = ['SE_A02001_002','SE_A02001_003']


# In[27]:


df = df.drop(columns_to_dropb,axis=1)


# In[28]:


columns_to_dropc = ['SE_A01001_001','SE_A01001_002','SE_A01001_003','SE_A01001_004','SE_A01001_005', 'SE_A01001_006']


# In[29]:


df = df.drop(columns_to_dropc,axis=1)


# In[30]:


columns_to_dropd = ['SE_A01001_007','SE_A01001_008','SE_A01001_009','SE_A01001_010','SE_A01001_011', 'SE_A01001_012','SE_A01001_013']


# In[31]:


df = df.drop(columns_to_dropd,axis=1)


# In[32]:


df.shape


# In[33]:


columns_to_drope = ['SE_A01004_001','SE_A01004_002','SE_A01004_003','SE_A03001_001']


# In[34]:


df = df.drop(columns_to_drope,axis=1)


# In[35]:


df.shape


# In[36]:


columns_to_dropf = ['SE_A10008_001','SE_A10008_002','SE_A10008_003','SE_A10008_004','SE_A10008_005','SE_A10008_006','SE_A10008_007','SE_A10008_008','SE_A10008_009']


# In[37]:


df = df.drop(columns_to_dropf,axis=1)


# In[38]:


columns_to_dropg = ['SE_A12003_001','SE_A12003_002','SE_A12003_003','SE_A10001_001','SE_A10060_001','SE_A10060_002','SE_A10060_003']


# In[39]:


df = df.drop(columns_to_dropg,axis=1)


# In[40]:


df.shape


# In[42]:


df.head()


# In[43]:


columns_to_droph = ['SE_A11001_001','SE_A11001_002','SE_A11001_003','SE_A11001_004','SE_A11001_005','SE_A11001_006']


# In[44]:


df = df.drop(columns_to_droph,axis=1)


# In[45]:


columns_to_dropi = ['SE_A10044_001','SE_A10044_002','SE_A10044_003','SE_A10047_001','SE_A10047_002','SE_A10047_003','SE_A10047_004']


# In[46]:


df = df.drop(columns_to_dropi,axis=1)


# In[47]:


columns_to_dropj = ['SE_A10032_001','SE_A10032_002','SE_A10032_003','SE_A10032_004','SE_A10032_005','SE_A10032_006','SE_A10032_007','SE_A10032_008','SE_A10032_009','SE_A10032_010','SE_A10032_011','SE_A10032_012']


# In[48]:


df = df.drop(columns_to_dropj,axis=1)


# In[49]:


df.shape


# In[50]:


columns_to_dropk = ['SE_A10057_001','SE_A10034_001','SE_A10034_002','SE_A10034_003','SE_A10034_004','SE_A10034_005','SE_A10034_006','SE_A10034_007','SE_A10034_008']


# In[52]:


df = df.drop(columns_to_dropk,axis=1)


# In[53]:


columns_to_dropl = ['SE_A10037_001','SE_A10037_002','SE_A10037_003','SE_A13002_001','SE_A13002_002','SE_A13002_003','SE_A13002_004','SE_A13002_005','SE_A13002_006','SE_A13002_007','SE_A13002_008','SE_A13002_009','SE_A13002_010','SE_A13002_011']


# In[54]:


df = df.drop(columns_to_dropl,axis=1)


# In[55]:


columns_to_dropm = ['SE_A13004_001','SE_A13004_002','SE_A13004_003','SE_A13004_004','SE_A13004_005','SE_A13004_006','SE_A13004_007']


# In[56]:


df = df.drop(columns_to_dropm,axis=1)


# In[57]:


columns_to_dropn = ['SE_B13004_001','SE_B13004_002','SE_B13004_003','SE_B13004_004','SE_B13004_005']


# In[58]:


df = df.drop(columns_to_dropn,axis=1)


# In[59]:


columns_to_dropo = ['SE_A06001_001','SE_A06001_002','SE_A06001_003','SE_A06001_004','SE_A06001_005']


# In[60]:


df = df.drop(columns_to_dropo,axis=1)


# In[61]:


columns = list(df)
columns


# In[62]:


df.columns = ['FIPS',
 'Geo_NAME',
 'Geo_QName',
 'Geo_STATE',
 'Geo_COUNTY',
 'Geo_TRACT',
 'Total Pop',
 'White',
 'Black',
 'AmIndian_AlaskaNative',
 'Asian',
 'HAW_PI',
 'Other',
 'Two_or_more',
 'Total Popn',
 'Not_Hispanic_or_Latino',
 'NHWhite',
 'NHBlack',
 'NHAmIndian_AlaskaNative',
 'NHAsian',
 'NHHaw_PI',
 'NHOther',
 'NHTwo_or_more',
 'Hispanic_or_Latino',
 'HLWhite',
 'HLBlack',
 'HLAmIndian_AlaskaNative',
 'HLAsian',
 'HLHaw_PI',
 'HLOther',
 'HLTwo_or_more',
 'Totalpopulation',
 'Less_than_high_school',
 'High_school_graduate',
 'Some_college',
 'Bachelors_degree',
 'Masters_degree',
 'Prof_school_degree',
 'Doctorate_degree',
 'Med_hh_income',
 'Med_housevalue_ooccupied',
 'Median_gross_rent',
 'Median_gross_rent_aspct']


# In[63]:


df.head()


# In[64]:


df['pctWhite']=df['White']/df['Total Pop']


# In[65]:


df.head()


# In[66]:


df['pctBlack']=df['Black']/df['Total Pop']


# In[67]:


df['pctAmIndian_AlaskaNative']=df['AmIndian_AlaskaNative']/df['Total Pop']


# In[68]:


df['pctAsian']=df['Asian']/df['Total Pop']


# In[69]:


#no data
#df['pctHAW_PI']=df['HAW_PI']/df['Total Pop']


# In[70]:


df['pctOther']=df['Other']/df['Total Pop']


# In[71]:


df['pctTwo_or_more']=df['Two_or_more']/df['Total Pop']


# In[72]:


df.head()


# In[73]:


df['White'].describe()


# In[74]:


df['Black'].describe()


# In[75]:


df['Asian'].describe()


# In[76]:


len(df)


# In[77]:


df.isna().sum()


# In[78]:


df_sorted = df.sort_values(by='Med_hh_income',ascending = False)


# In[79]:


df_sorted[['Geo_NAME','Med_hh_income']].head(5)


# In[80]:


df_sorted.head(5).plot.bar(x='Geo_NAME',
                            y='Med_hh_income', 
                            title='Top 5 Census Tracts with Highest Median Household Income along bus route 20')


# In[81]:


df_sortedB=df.sort_values(by='Median_gross_rent', ascending=False)


# In[82]:


df_sortedB[['Geo_NAME','Median_gross_rent']].head(5)


# In[83]:


df_sortedB.head(5).plot.bar(x='Geo_NAME',
                            y='Median_gross_rent', 
                            title='Top 5 Census Tracts with Highest Median Gross Rent along bus route 20')


# In[84]:


df_sortedC = df.sort_values(by='pctWhite',ascending = False)


# In[85]:


df_sortedC[['Geo_NAME','pctWhite']].head(5)


# In[86]:


df_sortedC.head(5).plot.bar(x='Geo_NAME',
                            y='pctWhite', 
                            title='Top 5 Census Tracts with Highest percent of white residents along the 20 bus route')


# In[87]:


df_sortedD = df.sort_values(by='pctBlack',ascending = False)


# In[88]:


df_sortedD.head(5).plot.bar(x='Geo_NAME',
                            y='pctBlack', 
                            title='Top 5 Census Tracts with Highest percent of Black residents along the 20 bus route')


# In[89]:


df_sortedE = df.sort_values(by='pctAsian',ascending = False)


# In[90]:


df_sortedE.head(5).plot.bar(x='Geo_NAME',
                            y='pctAsian', 
                            title='Top 5 Census Tracts with Highest percent of Asian residents along the 20 bus route')


# In[91]:


import geopandas as gpd


# In[ ]:





# In[ ]:




