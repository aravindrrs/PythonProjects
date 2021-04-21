import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web
from sklearn.cluster import KMeans
from datetime import datetime,timedelta


class stock:

    def __init__(self,ticker):
        self.ticker= ticker
        print ("The stock ticker you have chose is : ", self.ticker.upper())
        
    def getdata(self):
        print ("entering getdata fucntion")
        self.ticker = self.ticker.upper()
        end_date = datetime.today()
        start_date = end_date-timedelta(days=1000) #arbitrary number of days
        start_date = start_date.strftime('%Y-%m-%d')
        end_date = end_date.strftime('%Y-%m-%d')
        df = web.DataReader(self.ticker,'yahoo',start_date,end_date) #type=pandas DataFrame
        return df


    # how to call the get data
    #aapl = getdata('aapl') #Loads AAPL data
    #SQ= getdata('sq') #loads SQ data

    #Plotting
    # Need to add a column to plot the data against so i added the days
    def plotting(self):
       
        ticker_dataframe= self.getdata()
        print ("ticker_dataframe inside plotting method", ticker_dataframe)
        ticker_dataframe['days'] = np.arange(len(ticker_dataframe)) # adding one more column into the dataframe to help plotting
        ticker_dataframe.plot(x='days',y='Close')
        plt.show()
    
        return 0


#s= stock(ticker = input("input your 'stock ticker' --> "))
s=stock('pfe')
print (s.plotting())

"""
lessons learned:
you can call another function inside a call only using self.another function..inside a class,everything is a class self obj
always put fuction (self): while defining it , for eg: def plotting (self) and call it with fucntion(). because python will always pass self to all its functions inside class
"""


