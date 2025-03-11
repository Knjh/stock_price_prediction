# Stock Prediction and Analysis   

This is a **Stock Prediction and Analysis** web application built using **Streamlit**. It allows users to analyze stock data and predict future stock prices using time series forecasting models.

## 📌 Features  

### **1. Home Page**  
- Displays a welcome message and project overview.  

### **2. Analysis Page**  
- Fetches historical stock data using **Yahoo Finance (yfinance)**.  
- Provides rolling mean analysis for trend detection.  
- Performs stationarity checks using the **ADF (Augmented Dickey-Fuller) test**.  
- Displays interactive visualizations using **Plotly**.  

### **3. Prediction Page**  
- Predicts the next **30 days' closing prices** of a stock.  
- Uses **ARIMA (AutoRegressive Integrated Moving Average)** for time series forecasting.  
- Evaluates the model using **Root Mean Squared Error (RMSE)**.  
- Scales and inverse scales data using **StandardScaler**.  
- Displays forecasted data in an interactive table.  


