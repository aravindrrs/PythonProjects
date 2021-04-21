# To get stock data from Hedge Funds
# Track and list top 20 Hedge Funds and analyze their thier top holdings

# import webbrowser
# webbrowser. open('https://sec.report/Document/Search/')

import selenium
from selenium import webdriver as webd
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
driver = webd.Chrome (ChromeDriverManager().install())
driver.get('https://sec.report/Document/Search/')

def SecCompanyUrl(HedgeFundName):
    #input company name
    companyname= driver.find_element (By.ID,"filer1")
    companyname.send_keys (HedgeFundName)
    driver.find_element_by_xpath ('//*[@id="formType"]/option[22]').click()
    driver.find_element_by_xpath('//*[@id="searchtext"]/div[4]/div/div[2]/button').click()
    urllinks=driver.find_element_by_xpath('//*[@id="results"]/div[2]/table/tbody/tr[1]/td[1]/div[1]/a').parent.current_url
    #driver.find_element_by_xpath('//*[@id="results"]/div[2]/table/tbody/tr[1]/td[1]/div[1]/a').click()
    return   urllinks


Hedgies = ['Bridgewater Associates' , 'Renaissance Technologies' , 'Man Group','AQR Capital Management',
'Two Sigma Investments' , 'Millennium Management' , 'Elliott Management' , 'BlackRock' , 'Citadel Advisors' , 'Davidson Kempner Capital Management' ]

print (SecCompanyUrl('Citadel Advisors' ))