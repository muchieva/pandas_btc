import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from get_crypto import get_crypto
#
os.environ['TCL_LIBRARY'] = r'C:\Users\rasa7\AppData\Local\Programs\Python\Python313\tcl\tcl8.6'

# prices = pd.concat(
#     [btc['Close'].rename('Bitcoin'),
#      bnb['Close'].rename('BNB'),
#      eth['Close'].rename('Ethereum')],
#     axis=1, join='outer'
# )
# prices.ffill()
# print(prices.fillna(0))
# # prices.plot()
# # prices.loc["2022-05-01":"2022-08-20"].plot(kind= 'hist')
# # plt.show()
# #
#
# # Correlation matrix
# correlation_matrix = prices.corr()
# print(correlation_matrix)
# sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
# plt.title("Correlation Matrix")
# plt.show()


# # Calculate daily returns
# returns = prices.pct_change()
# print(returns.fillna(0))
# returns.plot(figsize=(10, 6), title="Daily Returns")
# plt.ylabel("Percentage Change")
# plt.show()
# volatility = returns.rolling(window=30).std()
# volatility.plot(figsize=(10, 6), title="30-Day Rolling Volatility")
# plt.ylabel("Volatility")
# plt.show()


# # Monthly trend analysis
# prices['Month'] = prices.index.month
# monthly_avg = prices.groupby('Month').mean()
# print(monthly_avg)
# monthly_avg.plot(kind='bar', figsize=(10, 6))
# plt.title("Average Monthly Prices")
# plt.ylabel("Average Price")
# plt.show()

# Identifying dips
# dip_threshold = 0.2  # Define a 20% dip
# dips = (prices / prices.shift(1) - 1) < -dip_threshold
# print(dips)
# plt.figure(figsize=(10, 6))
# for crypto in prices.columns:
#     plt.plot(prices[crypto], label=crypto)
#     plt.scatter(prices[dips[crypto]].index, prices[crypto][dips[crypto]], label=f"{crypto} Dips", color='red')
# plt.legend()
# plt.title("Market Dips")
# plt.show()

# Calculate spreads
# spread = prices['Bitcoin'] - prices['Ethereum']
# plt.figure(figsize=(10, 6))
# plt.plot(spread, label='Spread (BTC - ETH)')
# plt.axhline(spread.mean(), color='red', linestyle='--', label='Mean Spread')
# plt.legend()
# plt.title("Bitcoin-Ethereum Spread")
# plt.show()
#


df = get_crypto([ 'Ethereum', 'Aave', 'ApeCoin'])
correlation_matrix = df.corr()
print(correlation_matrix)
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()


print(df)
df.plot()
plt.show()