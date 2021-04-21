from selenium import webdriver
import pandas as pd
from pandas import Series, ExcelWriter
from webdriver_manager.chrome import ChromeDriverManager
import openpyxl 
import os.path
from os import path


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(30)

filepath = 'C:\\Users\\aravi8\\Documents\\PythonProjects\\Tickers\\WebullTickers.xlsx'

# if os.path.exists(filepath):
#     os.remove(filepath)

url = 'https://finance.yahoo.com/screener/unsaved/a286bcb9-b12c-4fff-8c31-29bb5b90c728?dependentField=sector&dependentValues=Communication%20Services'


driver.get(url)

screenertable = driver.find_element_by_xpath('//*[@id="screener-results"]')

# # screenertablepd=pd.read_html(screenertable).get_attribute('outerHTML')[0]
# screenertablepd=pd.read_html(screenertable)[0]

from xml.etree import ElementTree as ET


table = ET.XML(screenertable )
rows = iter(table)
headers = [col.text for col in next(rows)]
for row in rows:
    values = [col.text for col in row]
    print(dict(zip(headers, values)))


# if os.path.exists(filepath):
#     with ExcelWriter (filepath,mode = 'a') as writer:
#         screenertable.to_excel (writer, sheet_name = 'SmallCapWebull')
# else:
#     with ExcelWriter (filepath) as writer:
#        screenertable.to_excel (writer, sheet_name = 'SmallCapWebull') 
