# Projeto Django com previsão de ações

Este é um projeto Django que utiliza a biblioteca yfinance para obter dados históricos de ações e a biblioteca Prophet para realizar previsões dos próximos 30 dias. O projeto apresenta uma API para acessar os dados históricos e as previsões das ações.

## Requisitos

Certifique-se de ter os seguintes requisitos instalados em seu ambiente de desenvolvimento:

- Python 3
- Django
- yfinance
- Prophet
- djangorestframework

## Instalação

1. Clone este repositório para o seu ambiente local:

```shell
git clone https://github.com/seu-usuario/nome-do-projeto.git

## Uso da API
Obter dados históricos de uma ação
URL: /historical-data/<ticker>/

## Método: GET

Parâmetros:

<ticker>: A sigla da ação desejada (por exemplo, AAPL para Apple Inc.).
Resposta de exemplo:
{
  "ticker": "AAPL",
  "data": [
    {"date": "2022-01-01", "open": 123.45, "close": 124.56, "high": 125.67, "low": 122.34},
    {"date": "2022-01-02", "open": 124.56, "close": 125.67, "high": 126.78, "low": 123.45},
    ...
  ]
}

## Contribuição

Contribuições são bem-vindas! Se você quiser melhorar este projeto ou tiver alguma sugestão, fique à vontade para abrir uma issue ou enviar um pull request.

