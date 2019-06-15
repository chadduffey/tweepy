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

api = tweepy.API(auth)

try:
	api.verify_credentials()
	print("Auth ok")
except:
	print("Error during authentication")

