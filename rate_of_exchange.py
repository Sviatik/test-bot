import requests

URL = 'http://bank-ua.com/export/exchange_rate_cash.json'



def get_usd():
	r = requests.get(URL).json()
	return r[8]['rateSale']	




