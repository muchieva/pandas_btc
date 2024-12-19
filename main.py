import os
import pandas as pd
import matplotlib.pyplot as plt

os.environ['TCL_LIBRARY'] = r'C:\Users\rasa7\AppData\Local\Programs\Python\Python313\tcl\tcl8.6'

btc = pd.read_csv('files/wrapped bitcoin.csv', index_col=0)
print(btc)
doge = pd.read_csv('files/dogecoin.csv')
print(doge)
shiba = pd.read_csv('files/Shiba Inu.csv')
print(shiba)

prices = pd.DataFrame(index=btc.index)
prices.head()
prices['Bitcoin'] = btc['Close']
prices['Dogecoin'] = doge['Close']
prices['Shiba Inu'] = shiba['Close']
print(prices.head())