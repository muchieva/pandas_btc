import streamlit as st
from matplotlib import pyplot as plt
import seaborn as sns
from get_crypto import get_crypto
import os

os.environ['TCL_LIBRARY'] = r'C:\Users\rasa7\AppData\Local\Programs\Python\Python313\tcl\tcl8.6'

st.title("Cryptocurrency Correlation Analysis")
st.write("**Hypothesis:** Cryptocurrencies move in sync.")

if "crypto_list" not in st.session_state:
    st.session_state.crypto_list = ['Bitcoin', 'Ethereum']
crypto_list = st.multiselect(
    "Select cryptocurrencies to analyze:",
    options=['Bitcoin', 'Ethereum', 'Aave', 'ApeCoin'],
    default=st.session_state.crypto_list,
    key="crypto_selection"
)

st.session_state.crypto_list = crypto_list

def correlation(selected_cryptos):
    if not selected_cryptos:
        st.warning("Please select at least one cryptocurrency.")
        return

    df = get_crypto(selected_cryptos)

    st.subheader("Raw Data")
    st.dataframe(df)

    correlation_matrix = df.corr()

    st.subheader("Correlation Matrix")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', ax=ax)
    ax.set_title("Correlation Matrix")
    st.pyplot(fig)

    st.subheader("Cryptocurrency Prices")
    fig, ax = plt.subplots(figsize=(10, 6))
    df.plot(ax=ax, title="Cryptocurrency Prices")
    ax.set_ylabel("Price")
    st.pyplot(fig)

if st.button("Analyze Correlation"):
    correlation(st.session_state.crypto_list)
