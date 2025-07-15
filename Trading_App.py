import streamlit as st

st.set_page_config(
    page_title = "Stock Guide",
    page_icon = "charts_with_downward_trend",
    layout = "wide"
)

col1 = st.container()
with col1:
    if st.button("🏠", key="home_button"):
        st.switch_page("Trading_App.py")  

st.title("Stocks Trading Guide App :bar_chart:")

st.header("We provide the Greatest platform for you to collect all prior information to investing in stocks.")

st.image("app.png")

st.markdown("## We provide the following services:")

st.markdown("### :one: Stock Information")
st.write("Through this page, you can see all the information about stocks of your choice, including the stock's business summary, sector, full-time employees, market cap, beta, EPS, PE ratio, quick ratio.We also help you visualise this data.This information is essential for making informed investment decisions.")
st.page_link("pages/Stock_Analysis.py", label="👉 Go to Stock Analysis", icon="📊")

st.markdown("### :two: Stock Prediction")
st.write("You can explore predicted closing prices for the next 30 days based on historical stock data and advanced forecasting models. Use this tool to gain valuable insights into the market trends and make informed investments decisions")
st.page_link("pages/Stock_Prediction.py", label="👉 Go to Stock Prediction", icon="📈")