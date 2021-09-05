import requests
import datetime

    
    
def cbr(event):
    dol = requests.get("https://www.cbr-xml-daily.ru/daily_json.js").json()
    btc = requests.get("https://blockchain.info/ru/ticker").json()
    
    value_btc = btc["USD"]["last"]
    value_usd = dol["Valute"]["USD"]["Value"]
    value_eur = dol ["Valute"]["EUR"]["Value"]
    name_eur= dol["Valute"]["EUR"]["Name"]
    
    dol = f"""Курс валют:
    Доллар : {round(value_usd)} ₽
    {name_eur} : {round(value_eur)} ₽
    BTC : {value_btc} $
    """
    event.message_send(f"{dol}")
    
HandleCmd('курс', 0, cbr)