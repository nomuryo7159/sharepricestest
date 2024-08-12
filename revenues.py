import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib_fontja
import numpy as np


# Streamlitのタイトル
st.title("企業の売上推移グラフ")

# ティッカーシンボルの選択肢を用意する
ticker_options = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"]
ticker_symbol = st.selectbox("企業のティッカーシンボルを選択してください", ticker_options)

# ティッカーシンボルが選択された場合に処理を行う
if ticker_symbol:
    # yfinanceを使って企業のデータを取得
    ticker = yf.Ticker(ticker_symbol)
    try:
        # 財務情報を取得
        financials = ticker.financials

        # 売上高を取得
        if 'Total Revenue' in financials.index:
            revenue = financials.loc['Total Revenue']

            # データを整形
            revenue = revenue.sort_index(ascending=True)
            dates = revenue.index
            values = revenue.values

            # グラフを作成
            plt.figure(figsize=(10, 6))
            plt.plot(dates, values, marker='o', linestyle='-', color='b')
            plt.title(f"{ticker_symbol} の売上推移")
            plt.xlabel("年")
            plt.ylabel("売上高 (USD)")
            plt.grid(True)

            # グラフをStreamlitに表示
            st.pyplot(plt)
        else:
            st.error("指定された企業の売上高データが見つかりませんでした。")
    except Exception as e:
        st.error(f"データ取得中にエラーが発生しました: {e}")