import pandas as pd
import numpy as np

# Parameters
trading_days = 252
initial_price = 100
volatility = 0.20

# Calculate the mean daily return for upward and downward trends (5% over a year)
mean_return_up = (1.15)**(1/trading_days) - 1
mean_return_down = (0.85)**(1/trading_days) - 1

# Generate random daily returns based on the volatility and mean return
daily_returns_up = np.random.normal(mean_return_up, volatility / np.sqrt(trading_days), trading_days)
daily_returns_down = np.random.normal(mean_return_down, volatility / np.sqrt(trading_days), trading_days)

# Calculate the stock price based on the daily returns
stock_prices_up = [initial_price]
stock_prices_down = [initial_price]

for i in range(1, trading_days):
    stock_prices_up.append(stock_prices_up[i-1] * (1 + daily_returns_up[i]))
    stock_prices_down.append(stock_prices_down[i-1] * (1 + daily_returns_down[i]))

# Create a DataFrame
date_range = pd.bdate_range(start='2023-01-01', periods=trading_days)
stock_data = pd.DataFrame({
    'Date': date_range,
    'Close_Upward_Trend': stock_prices_up,
    'Close_Downward_Trend': stock_prices_down
})

