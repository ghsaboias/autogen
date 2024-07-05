# filename: stock_price_plot.py
import yfinance as yf
import matplotlib.pyplot as plt

# Downloading the stock data for TSLA and AAPL from Jan 2021 to Jan 2022
tsla_data = yf.download('TSLA', start='2021-01-01', end='2022-01-01')
aapl_data = yf.download('AAPL', start='2021-01-01', end='2022-01-01')

# Plotting the stock prices
plt.figure(figsize=(12, 6))
plt.plot(tsla_data['Close'], label='TSLA')
plt.plot(aapl_data['Close'], label='AAPL')
plt.title('Stock Prices of TSLA and AAPL from Jan 2021 to Jan 2022')
plt.xlabel('Date')
plt.ylabel('Stock Price (USD)')
plt.legend()
plt.grid()
plt.savefig('stock_price_plot.png')
plt.show()