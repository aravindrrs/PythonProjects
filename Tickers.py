from selenium import webdriver
import pandas as pd
from pandas import Series, ExcelWriter
from webdriver_manager.chrome import ChromeDriverManager
import openpyxl 
import os
import time
#from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.implicitly_wait(30)

url = 'https://finance.yahoo.com/screener/new'
filepath = 'C:\\Users\\aravi8\\Documents\\PythonProjects\\Tickers\\Tickers.xlsx'

if os.path.exists(filepath):
    os.remove(filepath)

# def TickerScreener (marketcapchoice):
driver.get(url)
marketcap = driver.find_element_by_xpath ('//*[@id="screener-criteria"]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div/button[2]').click()
addsector  = driver.find_element_by_xpath ('//*[@id="screener-criteria"]/div[2]/div[1]/div[1]/div[4]/div/div[1]/div[2]/ul/li/div/div').click()

commservices = driver.find_element_by_xpath('//*[@id="dropdown-menu"]/div/div[2]/ul/li[8]/label/span').click()
# actions = ActionChains(driver)
# actions.click(commservices )
# actions.perform()
clickoutside = driver.find_element_by_xpath ('//*[@id="screener-criteria"]/div[2]/div[1]/div[1]/div[4]/div/div[1]/div[2]').click()
findstocks= driver.find_element_by_xpath('//*[@id="screener-criteria"]/div[2]/div[1]/div[3]/button[1]').click()
print ("")
   

    




# capsizeinput = str(input ("Enter market capitalization size --> small, mid, large, mega"))

# def CapSize(capsizeinput):
#     switcher = {
#         'small': '//*[@id="screener-criteria"]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div/button[1]',
#         'mid' :'//*[@id="screener-criteria"]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div/button[2]',
#         'large' : '//*[@id="screener-criteria"]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div/button[3]',
#         'mega' : '//*[@id="screener-criteria"]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div/button[4]'

#     }

#     return switcher.get(capsizeinput, "Invalid cap")

# marketcapchoice = CapSize(capsizeinput)
# TickerScreener (marketcapchoice)