import tweepy
import csv



####input your credentials here
consumer_key = 'qjBKfredGfs5DeH69SDNLdEXN'
consumer_secret = 'YoXs5jEOC4EkLKl7MvkNNkpp55L70vqKvmfWofHPVijutnAa5f'
access_token = '4275253119-VvaVvbgAZRmRQnX8CM4Lr23UVpJeDnfD0Q5f5ys'
access_token_secret = 'py4IZRw0HNdWNCBUmK4WZyvcKvZfoUwq6h7TWOJf79TsX'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

query=input("hashtag you want to observe: ")

suspicious_screen_names=[]

for tweet in tweepy.Cursor(api.search,q=query, lang="de").items(): 
    print(tweet.user.screen_name)
    print(tweet.created_at)
            



#for x in suspicious_screen_names:
    #userlook_up=api.lookup_users(screen_names=x)
    #print(userlook_up)
