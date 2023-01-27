import requests
import json

def cbr(event):
    dol = requests.get("https://www.cbr-xml-daily.ru/daily_json.js").json()
    btc = requests.get ("https://api.blockchain.com/v3/exchange/tickers").json()
   

    value_usd = dol["Valute"]["USD"]["Value"]
    value_eur = dol ["Valute"]["EUR"]["Value"]
    name_eur= dol["Valute"]["EUR"]["Name"]
    bt = btc[35]["last_trade_price"]
    
    doll = f"""Курс валют:
    Доллар : {(value_usd)} ₽
    {name_eur} : {value_eur} ₽
    BTC : {bt} $
    """
    event.message_send(doll)
    
HandleCmd('курс', 0, cbr)
