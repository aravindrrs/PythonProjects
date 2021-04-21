from selenium import webdriver
import pandas as pd
from pandas import Series, ExcelWriter
from webdriver_manager.chrome import ChromeDriverManager
import openpyxl 
import os


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(30)

filepath = 'C:\\Users\\aravi8\\Documents\\PythonProjects\\HedgFundHoldings\\HoldingsBook.xlsx'
os.remove(filepath)
urls = ['https://sec.report/Document/0000950123-21-002786/#primary_doc.xml',
        'https://sec.report/Document/0000919574-21-001487/#primary_doc.xml',
        'https://sec.report/Document/0000950123-21-002766/#primary_doc.xml']


tablefromurl=[]
for url,i in zip((urls),(range(len(urls)))):
    driver.get(url)
    reportingdate=driver.find_element_by_xpath ("/html/body/div[1]/div/div[3]/div[2]/table/tbody/tr[1]").text
    summary = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/p").text
    companyname=driver.find_element_by_xpath ('//*[@id="breadcrumb"]/ol/li[2]/a/span').text
    tablefromurl.append(pd.read_html(driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[2]/table").get_attribute('outerHTML'))[0])
    
    if os.path.exists(filepath):
         with ExcelWriter (filepath,mode = 'a') as writer:
             tablefromurl[i].to_excel (writer, sheet_name = companyname)
    else:
         with ExcelWriter (filepath) as writer:
             tablefromurl[i].to_excel (writer, sheet_name = companyname)  
    
    wb = openpyxl.load_workbook(filepath)
    sheet = wb[companyname]
    sheet['A1']=  summary
    wb.save(filepath)
    wb.close()

