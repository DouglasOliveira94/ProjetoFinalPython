from django.urls import reverse
from rest_framework import status

def test_get_historical_data(client):
    url = reverse('historical-data', kwargs={'ticker': 'AAPL'})
    response = client.get(url)
    
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()['data']) == 365
    # Adicione mais asserções conforme necessário para verificar os dados retornados

def test_get_historical_data_invalid_ticker(client):
    url = reverse('historical-data', kwargs={'ticker': 'INVALID'})
    response = client.get(url)
    
    assert response.status_code == status.HTTP_404_NOT_FOUND
    # Adicione mais asserções conforme necessário para verificar a resposta

def test_get_forecast(client):
    url = reverse('forecast', kwargs={'ticker': 'AAPL'})
    response = client.get(url)
    
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()['forecast']) == 30
    # Adicione mais asserções conforme necessário para verificar os dados retornados

def test_get_forecast_invalid_ticker(client):
    url = reverse('forecast', kwargs={'ticker': 'INVALID'})
    response = client.get(url)
    
    assert response.status_code == status.HTTP_404_NOT_FOUND
    # Adicione mais asserções conforme necessário para verificar a resposta
