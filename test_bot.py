import urllib2
import os
import requests

TOKEN = os.environ['TGTOKEN']
CHAT_ID = os.environ["TGCHATID"]

#print 'qwe'

URL = "https://api.telegram.org/bot" + TOKEN + "/"
#?chat_id=" + CHAT_ID + "&text=testmassage"
#get = urllib2.urlopen(URL.encode('UTF-8'))




def send_message(chat_id, text="bla bla bla"):
	url = URL + "sendMessage" + '&' + CHAT_ID
	#answer = {"char_id": chat_id, "text": text}
	r = requests.get(url)