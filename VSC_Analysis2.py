"""Based on https://www.reddit.com/r/algotrading/comments/lma5z9/beginner_tutorial_separating_historic_data_by/

"""

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
        start_date = end_date-timedelta(days=100) #arbitrary number of days
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
        ticker_dataframe['days'] = np.arange(len(ticker_dataframe)) # adding one more column into the dataframe to help plotting
        ticker_dataframe.plot(x='days',y='Close')
        plt.draw()
        
        return ticker_dataframe
    
    def plot_trends(self,x,y,lb):
        clist = ['r','orange','g', 'b','m']
        nclasses = len(np.unique(lb))
        for i in range(nclasses):
            xx = x[lb==i]
            yy = y[lb==i]
            plt.scatter(xx,yy,c=clist[i],label=str(i))
        plt.legend(fontsize='x-large')
        plt.draw()
        
        
        return 0

#s= stock(ticker = input("input your 'stock ticker' --> "))

s=stock('sq')
#print (s.getdata())
print (s.plotting())



c = s.plotting().Close.values
print (type(c))
lr = np.diff(np.log(c)) #log returns
km_obs = KMeans(5).fit(lr.reshape(-1,1))
xr = np.arange(len(lr))
y = c[1:]
lb = km_obs.labels_


print (s.plot_trends(xr,y,lb))

plt.show()












"""
lessons learned:
1.you can call another function inside a call only using self.another function..inside a class,everything is a class self obj
2. always put fuction (self): while defining it , for eg: def plotting (self) and call it with fucntion(). because python will always pass self to all its functions inside class
3. you cannot access local variable to a funtion instead return that variable in the fucntion return and then use it elsewhere
4. you can return as many local variables you want
"""