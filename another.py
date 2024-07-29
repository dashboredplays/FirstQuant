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
import scipy.stats as si


warnings.filterwarnings('ignore')

# Function to calculate the Black-Scholes price
def black_scholes(S, K, T, r, sigma, option_type='call'):
    """
    S: current stock price
    K: option strike price
    T: time to maturity (in years)
    r: risk-free interest rate (annual)
    sigma: volatility of the underlying stock (annual)
    option_type: 'call' or 'put'
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    if option_type == 'call':
        option_price = (S * si.norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * T) * si.norm.cdf(d2, 0.0, 1.0))
    elif option_type == 'put':
        option_price = (K * np.exp(-r * T) * si.norm.cdf(-d2, 0.0, 1.0) - S * si.norm.cdf(-d1, 0.0, 1.0))
    
    return option_price

# Fetch historical stock data for Apple
start = dt.datetime(2022, 1, 1)
end = dt.datetime(2023, 1, 1)
data = yf.download("AAPL", start=start, end=end)

# Parameters for the Black-Scholes model
K = 150  # Strike price
r = 0.01  # Risk-free interest rate (1%)
sigma = 0.2  # Volatility (20%)

# Calculate time to maturity in years (we'll use 30 days to maturity)
T = 30 / 365

# Calculate the Black-Scholes price for each trading day
data['Option_Price'] = data['Close'].apply(lambda S: black_scholes(S, K, T, r, sigma, option_type='call'))

# Plot the results
plt.figure(figsize=(14, 7))
plt.plot(data.index, data['Close'], label='AAPL Close Price')
plt.plot(data.index, data['Option_Price'], label='Call Option Price (30 days to maturity)')
plt.legend()
plt.title('AAPL Stock Price and European Call Option Price (Black-Scholes)')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()