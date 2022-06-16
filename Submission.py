#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# In[7]:


class Web_Scraping():
    def scraping(self):
        District = []
        Ad = []
        FM_Numbers = []
        BDI = []
        Short_Description = []
        Number_of_Contracts_Awarded = []
        Contract_Threshold = []
        Major_Work_Types = []
        Minor_Work_Types = []
        Under_Utilized_Work_Groups = []
        Contract_Amount_Limit = []
        Advertisement_Date = []
        Response_Deadline_Date_Time = []
        Shortlist_Selection_Date = []
        Final_Selection_Date = []
        Selection_Method = []
        Standard_Notes = []

        driver = webdriver.Chrome(ChromeDriverManager().install())
        url = "https://pdaexternal.fdot.gov/Pub/AdvertisementPublic/AllAdDetail/PS/A"
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        spans = soup.select('.left-top:nth-child(1)')
        spans1 = soup.select('a.ng-binding')
        spans2 = soup.select('.left-top:nth-child(3) .ng-binding')
        spans3 = soup.select('.ng-binding:nth-child(4)')
        spans4 = soup.select('.ng-binding:nth-child(5)')
        spans5 = soup.select('.ng-binding:nth-child(6)')
        spans6 = soup.select('.ng-scope+ .ng-binding.ng-scope')
        spans7 = soup.select('.ng-binding+ .ng-scope .ng-binding')
        spans8 = soup.select('.ng-scope:nth-child(9) .ng-binding')
        spans9 = soup.select('.ng-scope:nth-child(10) .ng-binding')
        spans10 = soup.select('.ng-binding:nth-child(11)')
        spans11 = soup.select('.ng-binding:nth-child(12)')
        spans12 = soup.select('.ng-binding:nth-child(13)')
        spans13 = soup.select('.ng-binding:nth-child(14)')
        spans14 = soup.select('.ng-binding:nth-child(15)')
        spans15 = soup.select('.left-top:nth-child(16) .ng-binding')
        spans16 = soup.select('.ng-scope:nth-child(17) .ng-binding')
       
        
        for span in spans:
            District.append(span.text.strip())
        for span in spans1:
            Ad.append(span.text.strip())
        for span in spans2:
            FM_Numbers.append(span.text.strip())
        for span in spans3:
            BDI.append(span.text.strip())
        for span in spans4:
            Short_Description.append(span.text.strip())
        for span in spans5:
            Number_of_Contracts_Awarded.append(span.text.strip())
        for span in spans6:
            Contract_Threshold.append(span.text.strip())
        for span in spans7:
            Major_Work_Types.append(span.text.strip())
        for span in spans8:
            Minor_Work_Types.append(span.text.strip())
        for span in spans9:
            Under_Utilized_Work_Groups.append(span.text.strip())
        for span in spans10:
            Contract_Amount_Limit.append(span.text.strip())
        for span in spans11:
            Advertisement_Date.append(span.text.strip())
        for span in spans12:
            Response_Deadline_Date_Time.append(span.text.strip())
        for span in spans13:
            Shortlist_Selection_Date.append(span.text.strip())
        for span in spans14:
            Final_Selection_Date.append(span.text.strip())
        for span in spans15:
            Selection_Method.append(span.text.strip())
        for span in spans16:
            Standard_Notes.append(span.text.strip())
            
        df=pd.DataFrame({'District':District,
                 'Ad':Ad,
                 'FM_Numbers':FM_Numbers,
                 'BDI':BDI,
                 'Short_Description':Short_Description,
                 'Number_of_Contracts_Awarded':Number_of_Contracts_Awarded,
                 'Contract_Threshold':Contract_Threshold,
                 'Major_Work_Types':Major_Work_Types,
                 'Minor_Work_Types':Minor_Work_Types,
                 'Under_Utilized_Work_Groups':Under_Utilized_Work_Groups,
                 'Contract_Amount_Limit':Contract_Amount_Limit,
                 'Advertisement_Date':Advertisement_Date,
                 'Response_Deadline_Date_Time':Response_Deadline_Date_Time,  
                 'Shortlist_Selection_Date':Shortlist_Selection_Date,
                 'Final_Selection_Date':Final_Selection_Date,
                 'Selection_Method':Selection_Method,
                 'Standard_Notes':Standard_Notes,                         
                }) 
        df.to_csv('data.csv', index=False, encoding='utf-8')    
        return "scrapping successful"
    
if __name__ == "__main__":
    process = Web_Scraping()
    process.scraping()


# In[ ]:




