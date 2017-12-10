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
	url = URL + "sendMessage" + '?chat_id=' + CHAT_ID + "&text=" + text
	#answer = {"char_id": chat_id, "text": text}
#	r = requests.get(url)
	get = urllib2.urlopen(url.encode('UTF-8'))	