import streamlit as st
from matplotlib import pyplot as plt
import seaborn as sns
from get_crypto import get_crypto
import pandas as pd
import os
os.environ['TCL_LIBRARY'] = r'C:\Users\rasa7\AppData\Local\Programs\Python\Python313\tcl\tcl8.6'

st.title("Cryptocurrency Volatility Analysis")

st.write(
    "**Hypothesis:** Certain cryptocurrencies are more volatile than others, and this volatility creates trading opportunities.")

if "crypto_list" not in st.session_state:
    st.session_state.crypto_list = ['Bitcoin', 'Ethereum']

crypto_list = st.multiselect(
    "Select cryptocurrencies to analyze:",
    options=['Bitcoin', 'Ethereum', 'Aave', 'ApeCoin'],
    default=st.session_state.crypto_list,
    key="crypto_selection"
)

st.session_state.crypto_list = crypto_list

def volatility(selected_cryptos):
    if not selected_cryptos:
        st.warning("Please select at least one cryptocurrency.")
        return

    df = get_crypto(selected_cryptos)
    returns = df.pct_change().fillna(0)

    st.subheader("Daily Returns")
    fig, ax = plt.subplots(figsize=(10, 6))
    returns.plot(ax=ax, title="Daily Returns")
    ax.set_ylabel("Percentage Change")
    st.pyplot(fig)

    st.subheader("30-Day Rolling Volatility")
    volatility = returns.rolling(window=30).std()
    fig, ax = plt.subplots(figsize=(10, 6))
    volatility.plot(ax=ax, title="30-Day Rolling Volatility")
    ax.set_ylabel("Volatility")
    st.pyplot(fig)

if st.button("Analyze Volatility"):
    volatility(st.session_state.crypto_list)