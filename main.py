import yfinance as yf
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt
import pandas as pd

# https://pypi.org/project/yfinance/
data = yf.download('AAPL', start='2023-01-01', end='2024-06-11')

close_prices = data['Close']

# Fit the ARIMA model
# ARIMA(5,1,0) is an example order, you might need to adjust it
model = ARIMA(close_prices, order=(5, 1, 0))
model_fit = model.fit()

# Print model summary
print(model_fit.summary())

# Step 4: Predict the next week (5 trading days)
forecast = model_fit.forecast(steps=5)
print("Next week's forecasted prices:")
print(forecast)

# Create a new series to append the forecasted values
last_date = close_prices.index[-1]
forecast_dates = pd.date_range(start=last_date + pd.Timedelta(days=1), periods=5, freq='B')
forecast_series = pd.Series(forecast.values, index=forecast_dates)

print(forecast_series)

# Plot the original data, fitted values, and forecasted values
plt.figure(figsize=(12, 8))
plt.plot(close_prices, label='Original')
plt.plot(model_fit.fittedvalues, label='Fitted', color='red')

# Plot the forecasted values
plt.plot(forecast_series, label='Forecast', color='green', marker='o')

# Enhance the plot
plt.title('ARIMA Model for AAPL Stock Prices')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.legend()
plt.show()
