#!/usr/bin/env python
# coding: utf-8

# In[2]:


start_date=input("Enter start date in format DD MMM YYYY like 14 Jan 2020: ")
end_date=input("Enter end date in format DD MMM YYYY like 14 Jan 2020: ")
tickerf=input("Which currency cross do you want to write in capital eg. 'EURUSD' for Euro to dollar : ")


# In[3]:


from findatapy.market import Market, MarketDataRequest, MarketDataGenerator

market = Market(market_data_generator=MarketDataGenerator())


# In[4]:


md_request = MarketDataRequest(start_date=start_date, finish_date=end_date,
                               category='fx', fields=['close'], freq='tick', data_source='dukascopy', tickers=[tickerf])

df = market.fetch_market(md_request)
print(df.tail(n=10))


# In[5]:


df


# In[6]:


df=df.reset_index()
df


# In[7]:


df.to_csv('data.csv')


# In[ ]:





# In[ ]:




