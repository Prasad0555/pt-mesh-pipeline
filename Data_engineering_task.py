#!/usr/bin/env python
# coding: utf-8

# In[27]:


from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd

class Web_Scraping():
    def scraping(self):
        S_No = []
        Organisation_Name = []
        Tender_Count = []

        options = Options()
        options.add_argument("start-maximized")
        driver = webdriver.Chrome(options=options)
        driver.get("https://etenders.gov.in/eprocure/app?page=FrontEndTendersByOrganisation&service=page")
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        spans = soup.select('#table td:nth-child(1)') 
        spans1 = soup.select('#table td:nth-child(2)')
        spans2 = soup.select('#table td~ td+ td')

        for span in spans:
            S_No.append(span.text.strip())
        for span in spans1:
            Organisation_Name.append(span.text.strip())
        for span in spans2:
            Tender_Count.append(span.text.strip())

        df=pd.DataFrame({'S_No':S_No,
                         'Organisation_Name':Organisation_Name,
                         'Tender_Count':Tender_Count,                         
                        })
        data = df[1:]
        data.to_csv('file.csv', index=False, encoding='utf-8')    
        return "scrapping successful"
    
if __name__ == "__main__":
    process = Web_Scraping()
    process.scraping()


# In[28]:


data


# In[ ]:




