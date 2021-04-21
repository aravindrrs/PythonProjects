
import pandas as pd
import math
import numpy as np
import pandas_datareader as web
from sklearn.preprocessing import MinMaxScaler as ms
from keras.models import Sequential
from keras.layers import Dense,LSTM 
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

df= web.DataReader('SQ',data_source='yahoo',start='2020-01-01',end='2020-12-31')
print (df)
print(df.shape)

plt.figure(figsize=(16,8))
plt.title('closing price')
plt.plot(df['Close'])
plt.xlabel('Date')
plt.ylabel('Price $')
plt.show()


# data=df.filter(['Close'])
# dataset=data.values
# training_len= math.ceil(len(dataset)*.8)

# scaler=ms(feature_range=(0,1))
# scaled_data = scaler.fit_transform(dataset)

# #create a training set from scaled data

# train_data_scaled= scaled_data [0:training_len,:]


