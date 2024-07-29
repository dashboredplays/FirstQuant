from statsmodels.regression.rolling import RollingOLS
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import statsmodels.api as sm
import pandas as pd
import numpy as np
import datetime as dt
import yfinance as yf
import pandas_ta
import warnings
warnings.filterwarnings('ignore')

#pandas read html
sp500 = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]

#clean data
sp500['Symbol'] = sp500['Symbol'].str.replace('.','-')

symbols_list = sp500['Symbol'].unique().tolist()
#this list is not survivorship bias free. This means that some of the companies in the list are not in the S&P 500 anymore.

end_date = '2023-09-27'
start_date = pd.to_datetime(end_date) - pd.DateOffset(365*8)

df = yf.download(tickers=symbols_list, 
                 start=start_date, 
                 end=end_date)

print(df.head())
