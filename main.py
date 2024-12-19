import os
import pandas as pd
import matplotlib.pyplot as plt

os.environ['TCL_LIBRARY'] = r'C:\Users\rasa7\AppData\Local\Programs\Python\Python313\tcl\tcl8.6'

btc = pd.read_csv('files/bitcoin.csv', index_col=0, parse_dates=True)
print(btc)
bnb = pd.read_csv('files/BNB.csv', index_col=0, parse_dates=True)
print(bnb)
eth = pd.read_csv('files/ethereum.csv', index_col=0, parse_dates=True)
print(eth)

# prices = pd.DataFrame(index=btc.index)
# prices.head()
# prices['Bitcoin'] = btc['Close']
# prices['BNB'] = bnb['Close']
# prices['XRP'] = xrp['Close']
# prices.ffill()
# print(prices.fillna(0))

prices = pd.concat(
    [btc['Close'].rename('Bitcoin'),
     bnb['Close'].rename('BNB'),
     eth['Close'].rename('Ethereum')],
    axis=1, join='outer'
)
prices.ffill()
print(prices.fillna(0))
# prices.plot()
prices.loc["2022-05-01":"2022-08-20"].plot()
plt.show()


