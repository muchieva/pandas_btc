import os
import pandas as pd
import matplotlib.pyplot as plt

os.environ['TCL_LIBRARY'] = r'C:\Users\rasa7\AppData\Local\Programs\Python\Python313\tcl\tcl8.6'

btc = pd.read_csv('files/bitcoin.csv', index_col=0, parse_dates=True)
print(btc)
bnb = pd.read_csv('files/BNB.csv', index_col=0, parse_dates=True)
print(bnb)
xrp = pd.read_csv('files/xrp.csv', index_col=0, parse_dates=True)
print(xrp)

prices = pd.DataFrame(index=btc.index)
prices.head()
prices['Bitcoin'] = btc['Close']
prices['BNB'] = bnb['Close']
prices['XRP'] = xrp['Close']
prices.ffill()
print(prices.fillna(0))

prices.plot()
plt.show()


