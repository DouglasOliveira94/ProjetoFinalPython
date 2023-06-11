from django.shortcuts import render
import yfinance as yf
from prophet import Prophet
from django.shortcuts import render
import yfinance as yf
from prophet import Prophet
import pandas as pd

def home(request):
    return render(request, 'home.html')


def prediction(request):
    if request.method == 'POST':
        ticker = request.POST.get('ticker')
        data = yf.download(ticker, start="2022-06-01", end="2023-06-01")
        data = data.reset_index()
        data = data[["Date", "Close"]]
        data.columns = ["ds", "y"]
        
        model = Prophet(
        changepoint_prior_scale=0.05,
        seasonality_prior_scale=10.0,
        interval_width=0.95
    )
        model.fit(data)

        future = model.make_future_dataframe(periods=30)
        forecast = model.predict(future)
        forecast['ds'] = forecast['ds'].dt.strftime('%d de %B de %Y')
        context = {
            'ticker': ticker,
            'forecast': forecast.tail(30).to_dict('records')
        }
        
        
        return render(request, 'prediction.html', context)

    return render(request, 'prediction.html')

