import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf


#downloading the stock data as per user's demand

def getStockData(symbol):

    stockData = yf.download(symbol, period='2y')['Adj Close']      #only closing values
    return stockData

symbol = input("Please enter your stock/index's symbol: ")
stockData = getStockData(symbol)


#functioning building MACD

def macd(price, slow, fast, signal):
    fastLine = price.ewm(span = fast, adjust = True).mean()                      #ewm is exp weighted and then we've taken its mean to get ema
    slowLine = price.ewm(span = slow, adjust = True).mean()
    macdLine = pd.DataFrame(fastLine - slowLine).rename(columns={'Adj Close':'macdLine'})
    signalLine = pd.DataFrame(macdLine.ewm(span = signal, adjust = True).mean()).rename(columns={'macdLine':'signalLine'})
    histogram = pd.DataFrame(macdLine['macdLine'] - signalLine['signalLine']).rename(columns= {0:'histogram'})
    frames = [macdLine, signalLine, histogram]
    df = pd.concat(frames, join='inner', axis = 1)
    return df


macd = macd(stockData, 26,12,9)


#plotting MACd
def plotMACD(prices, macdLine, signalLine, histogram):
    axis1 = plt.subplot2grid((8,1), (0,0), rowspan=5, colspan=1)
    axis2 = plt.subplot2grid((8,1), (5,0), rowspan=3, colspan=1)

    axis1.plot(prices)
    axis2.plot(macdLine, color='blue', linewidth=1.5, label='MACD Line')
    axis2.plot(signalLine, color='red', linewidth=1.5, label='Signal Line')

    for i in range(len(prices)):
        if str(histogram[i])[0] == '-':
            axis2.bar(prices.index[i], histogram[i], color='red')
        else:
            axis2.bar(prices.index[i], histogram[i], color='green')

    plt.legend(loc = 'lower right')
    plt.show()

plotMACD(stockData, macd['macdLine'], macd['signalLine'], macd['histogram'] )







