import urllib2

TOKEN = "$TGTOKEN"
CHAT_ID = "TGCHATID"

testvar = "$testvar"

print testvar

URL = "https://api.telegram.org/bot" + TOKEN + "/sendMessage?chat_id=" + CHAT_ID + "&text=testmassage"
get = urllib2.urlopen(URL.encode('UTF-8'))