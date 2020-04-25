import tweepy # importin' t w e e p e h ! ! !

# hookin' up our twitter acc to the code
auth = tweepy.OAuthHandler("<insert api key here>", "<insert api secret key here>")
auth.set_access_token("<insert access token here>", "<insert access token secret here>")
api = tweepy.API(auth)

tweet = "<insert your tweet here>"

# tweet it!
api.update_status(status = (tweet))
