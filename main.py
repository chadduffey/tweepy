import json
import os
import tweepy

try:
	api_key = os.environ['API_KEY'] 
	api_secret = os.environ['API_SECRET'] 
	token = os.environ['TOKEN'] 
	token_secret = os.environ['TOKEN_SECRET'] 
except:
	print('Environment Variables for Auth are missing. Exiting.')
	quit()

auth = tweepy.OAuthHandler(api_key,api_secret)
auth.set_access_token(token, token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True,
		wait_on_rate_limit_notify=True)

try:
	api.verify_credentials()
	print("Auth ok")
except:
	print("Error during authentication")

#Read from timeline sample:

timeline = api.home_timeline()
for tweet in timeline:
	print(f"{tweet.user.name} said {tweet.text}\n\n")


#Write to timeline sample:
print("Tweeting:")
#api.update_status("Test tweet from api")

#search user sample:
user = api.get_user("Scottduf")
print("User Details:")
print(user.name)
print(user.description)
print(user.location)
print("Last 20 followers:")
for f in user.followers():
	print(f.name)

#add a friend:
#api.create_friendship("realpython")

#update profile:
#api.update_profile(description="I do things...")

#like tweets...
tweets = api.home_timeline(count=1)
tweet = tweets[0]
print(f"Liking tweet {tweet.id} of {tweet.author.name}")
#api.create_favorite(tweet.id)

#who have you blocked?
for block in api.blocks():
	print(block.name)


#search
for tweet in api.search(q="Kali", lang="en", rpp=10):
	print(f"{tweet.user.name}:{tweet.text}\n\n")

#follow trends
#note - trends place 1 means World Wide, but you can list with api.trends_available()
trends_result = api.trends_place(1)
for trend in trends_result[0]["trends"]:
	print("Worldwide Trend: {}".format(trend["name"]))

#all_trends_available = api.trends_available()
#for t in all_trends_available:
#	print(t)

trends_result = api.trends_place(2490383)
for trend in trends_result[0]["trends"]:
	print("Seattle Trend: {}".format(trend["name"]))






