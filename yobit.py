import requests

URL = "https://yobit.net/api/3/ticker/"

bitcoin = 'btc_usd'

def get_price():
	url = URL + bitcoin
	r = requests.get(url).json()
	price = r['btc_usd']['avg']
	return price
