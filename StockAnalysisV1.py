import pandas_datareader.data as web
import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt


#date range
start= dt.date.today().replace(day=1)
#end = '2020-12-10'
end=dt.date.today()

#Stock
Pfizer= web.DataReader("PFE",'yahoo', start, end)


#Plotting 
op= Pfizer['Open'].plot(label='open price')
cl = Pfizer['Close'].plot(label='close price')
Pfizer['High'].plot(label='High')

plt.legend()
plt.show()
