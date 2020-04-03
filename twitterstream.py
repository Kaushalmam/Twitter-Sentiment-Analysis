import tweepy
from tweepy import OAuthHandler

api_key = "Insert key here"
api_secret = "Insert secret here"
access_token = "Insert token here" 
access_token_secret = "Insert token secret here"

 
auth = OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
 
api = tweepy.API(auth)    
    
from tweepy import Stream
from tweepy.streaming import StreamListener
 
class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('tweets.json', 'a') as f:  
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())

#change the keyword here
twitter_stream.filter(track=['#cars'])





