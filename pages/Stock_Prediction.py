import streamlit as st
from pages.utils.model_train import get_data, get_rolling_mean, get_differencing_order, scaling, evaluate_model, get_data, get_forecast, inverse_scaling
import pandas as pd
from pages.utils.plotly_figure import plotly_table, Moving_average_forecast

st.set_page_config(
    page_title="Stock Prediction",
    page_icon="📈",
    layout="wide"
)

col1 = st.container()
with col1:
    if st.button("🏠", key="home_button"):
        st.switch_page("Trading_App.py")

st.title("Stock Prediction")

col1,col2,col3 = st.columns(3)

with col1:
    ticker = st.text_input('Stock Ticker(e.g. GOOGL,META,AAPL,AMZN,TSLA,NFLX)', 'TSLA')

st.subheader('Prediciting Next 30 days Close Price for: '+ ticker)

close_price = get_data(ticker)
rolling_price = get_rolling_mean(close_price)

differencing_order = get_differencing_order(rolling_price)
scaled_data, scaler = scaling(rolling_price)
rmse = evaluate_model(scaled_data, differencing_order)

st.write("**Model RMSE Score:**",rmse)

forecast = get_forecast(scaled_data, differencing_order)

forecast['Close'] = inverse_scaling(scaler, forecast['Close'])

st.write('##### Forecast Data (Next 30 Days)')
fig_tail = plotly_table(forecast.sort_index(ascending=True).round(3))
fig_tail.update_layout(height = 220)
st.plotly_chart(fig_tail, use_container_width=True)


forecast = pd.concat([rolling_price, forecast])


st.plotly_chart(Moving_average_forecast(forecast.iloc[150:]), use_container_width=True)

