import tweepy
import random
from time import sleep

last_don = "last_don.txt"
ckey = 'qnuK8Jmf0ofzN9QGCWoCN5qff'
csecret = 'y49eh5mvu731AmrFobBItYFofnVUn1VQUTVnjz856w5AxIhT3v'
atoken = '886441868069875712-ZgWx0wS57xvapyJ5FxZkf79CRUxL8up'
asecret = '8vJ8Si7Ocoj1GnvpQ0CZ0G1lifKB2rei39GCujUtiKmqN'
auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken,asecret)
api = tweepy.API(auth)


tweets = api.user_timeline(id = '@realDonaldTrump',count = '1')
#api.update_status("Hello World! I am a bot!")

file = open(last_don,"r")
old_id =file.read()
file.close()

last_tweet = tweets[0].id
print(old_id)
print(last_tweet)
test1 = int(old_id)
test2 = int(last_tweet)
if(test1 != test2):
	print("new tweet")
	file = open(last_don,"w")
	file.write(str(last_tweet))
	file.close()

	text = tweets[0].text
	http = "http"

	if http in text:
		link = text.find(http)
	else:
		link = len(text)

	textList = list(text)
	#print(link)

	count = 0
	while count < link:
		letter = textList[count] 
		if random.getrandbits(1) == 1:
			textList[count] = letter.upper()
		else:
			textList[count] =letter.lower()
		count += 1

	final = ''.join(textList)
	print(final)
	#api.update_status(final)










