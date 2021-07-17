import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

# #downloading data
# stockData = yf.download('SBIN.NS', period='5y')
# indexData = yf.download('^NSEI', period='5y')
# sectorData = yf.download('^CNXAUTO', period='5y')
# # print(stockData)

# #closing values
# stockData_close = stockData['Adj Close']
# indexData_close = indexData['Adj Close']
# sectorData_close = sectorData['Adj Close']

# print(plt.plot(stockData_close))


data = pd.DataFrame()

portfolio = ['HEROMOTOCO.NS', '^NSEI']

for stock in portfolio:
    data[stock] = yf.download(stock, period='5y')['Adj Close']

fig, axes = plt.subplots()
axes.plot(data)
plt.show()




data2 = pd.DataFrame()
portfolio2 = ['HEROMOTOCO.NS', 'TVSMOTOR.NS', 'BAJAJ-AUTO.NS']

for stock in portfolio2:
    data2[stock] = yf.download(stock, period='5y')['Adj Close']

fig, axes = plt.subplots()
axes.plot(data2)
plt.legend(data2.columns)
plt.show()

