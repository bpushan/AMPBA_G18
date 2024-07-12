#!/usr/bin/env python
import streamlit as st
import pandas as pd
import numpy as np
import re
from plotly import graph_objs as go

st.set_page_config(page_title= "Predicting Stock Prices for Informed Investment Decisions", layout="wide")
## Load the dataset

def load_price_data():
    file_data = pd.read_csv("stock_prc_data.csv",encoding = "ISO-8859-1")
    return file_data
    
def load_pred_data():
    file_data = pd.read_csv("Stock_Prediction.csv",encoding = "ISO-8859-1")
    file_data = pd.DataFrame(file_data)
    return file_data

def get_unique_stocks(cols):
    stocks = []
    for c in cols[1:]:
        split = c.split('_')
        if split[0] == 'HUL':
            stocks.append("Hindustan Uniliver")
        elif split[0] == 'HDFC':
            stocks.append("HDFC Bank")
        else:
            stocks.append(split[0])
    stocks = set(stocks)
    return stocks
    
def plot_historical():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=Stock_prices['Date'], y=Stock_prices['Open'], name='stock_open'))
    fig.add_trace(go.Scatter(x=Stock_prices['Date'], y=Stock_prices['Close'], name='stock_close'))
    fig.layout.update(title_text="Historical Stock Price Plot")
    st.plotly_chart(fig)

def plot_predctions(Pred_prices,stock):
    fig = go.Figure()
    fig.add_trace(go.Scatter( y=Pred_prices[stock], name='stock_predction'))
    fig.layout.update(title_text="Predicted Stock Price Plot")
    st.plotly_chart(fig)
    
## -----------------------------------------------------------------------------------------##
##        SCREEN                                                                            ##   
## -----------------------------------------------------------------------------------------##
     
## Header Section - Intro
Header = st.container()
Header.subheader("Predicting Stock Prices for an Informed Investment Decisions")
Header.write("Hi,")
Header.write("AMPBA Group 18 presents stock price prediction.")
##
## Sidebar with Team info
st.sidebar.title("Foundational Project 2")
st.sidebar.write("Group 18  members:")
st.sidebar.write("Vinayak Mishra, 12310073")
st.sidebar.write("Vijay Tyagi, 12310105")
st.sidebar.write("Sharath Chandra Paladugu, 12310026")
st.sidebar.write("Sri Chirravuri, 12310023")
st.sidebar.write("Pushan Banerjee, 12310015")

## Container for Stock input
Stock_input = st.container()

stock_prc_data = load_price_data()

Pred_data = load_pred_data()

columns = stock_prc_data.columns
stocks_list = get_unique_stocks(columns)

## dropdown for stock list.
Stock = Stock_input.selectbox("Please choose a stock: ",
                              stocks_list)

## Sliderto allow to choose the prediction period.
n_time = st.slider("Number of Days of Prediction: ", 2, 200)

pred_load_state = st.text("Load data...")
#data_load_state.text = st.text("Loading data...done!")

# getting the data for the selected stock created
if Stock == "Hindustan Uniliver":
    stk = "HUL"
elif Stock == "HDFC Bank":
    stk = "HDFC"
else:
    stk = Stock
    
find = r'\b' + stk
stock_cols = []
stock_cols.append(columns[0])
for c in columns:
    if re.search(find,c):
        stock_cols.append(c)
        
st.subheader("Historical Data: ")
Stock_prices = stock_prc_data[stock_cols]
Stock_prices.columns = ['Date', 'Open', 'Close']
plot_historical()

Pred_prices = Pred_data[Stock][0:n_time]
st.subheader("Predictions Data: ")
st.write(Pred_prices)
#plot_predctions(Pred_prices, Stock)




