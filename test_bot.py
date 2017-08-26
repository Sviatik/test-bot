import urllib2
import os


TOKEN = os.environ['TGTOKEN']
CHAT_ID = os.environ["TGCHATID"]


URL = "https://api.telegram.org/bot" + TOKEN + "/sendMessage?chat_id=" + CHAT_ID + "&text=testmassage"
get = urllib2.urlopen(URL.encode('UTF-8'))