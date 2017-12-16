import requests

URL = "https://yobit.net/api/3/ticker/"

bitcoin = 'btc_usd'

def get_btc():
	url = URL + bitcoin
	r = requests.get(url).json()
	price = r['btc_usd']['avg']
	return price


if __name__ == '__main__':
	get_btc()
