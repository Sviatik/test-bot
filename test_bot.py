import urllib2
import os


TOKEN = "$TGTOKEN"
CHAT_ID = "TGCHATID"

print 'print some output'
print os.environ['testvar']

testvar = os.environ['testvar']

testvar = "$testvar"
testvar = $testvar


print testvar

URL = "https://api.telegram.org/bot" + TOKEN + "/sendMessage?chat_id=" + CHAT_ID + "&text=testmassage"
get = urllib2.urlopen(URL.encode('UTF-8'))