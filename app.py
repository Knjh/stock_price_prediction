import streamlit as st
from src.analysis import show_analysis_page
from src.prediction import show_prediction_page

# Configure Streamlit page
st.set_page_config(
    page_title="StockLens: AI-Driven Price Analysis and Prediction",
    page_icon="📈",
    layout="wide"
)

# Sidebar Navigation
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Stock Analysis", "Stock Prediction"])

if page == "Home":
    st.title("StockLens: AI-Driven Price Analysis and Prediction")
    st.header("Empowering Your Investment Journey")
    
    # Introduction with Quotes
    st.subheader("“An investment in knowledge pays the best interest.” – Benjamin Franklin")
    st.write("Welcome to the **Trading App**, your trusted companion in navigating the financial markets.")
    st.image('stock_image.jpg', use_container_width=True)
    
    # Overview of Features
    st.markdown("## What We Offer")
    st.write("""
    - **Stock Information Page**: Learn about key financial metrics, historical data, and trends.
    - **Stock Analysis Page**: Dive deep into stock fundamentals and technical analysis.
    - **Stock Prediction Page**: Use advanced ML models to forecast stock performance.
    """)
    
    # Motivational Quote
    st.markdown("### 🌟 Quote of the Day")
    st.info("“The stock market is filled with individuals who know the price of everything but the value of nothing.” – Philip Fisher")
    
    # Getting Started
    st.markdown("### How to Get Started")
    st.write("""
    1. Go to **Stock Analysis** for market trends.
    2. Visit **Stock Prediction** to forecast stock prices.
    """)
    st.markdown("---")
    st.markdown("### Ready to take charge of your financial future? 🚀")
    
elif page == "Stock Analysis":
    show_analysis_page()

elif page == "Stock Prediction":
    show_prediction_page()