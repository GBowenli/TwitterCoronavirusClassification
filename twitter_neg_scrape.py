import tweepy
import numpy as np
import csv

# load txt file that contains twitter dev keys
dev_keys = np.loadtxt('twitter_dev_keys.txt', dtype=str, delimiter='\n')

# set twitter dev keys in variables
consumer_key = dev_keys[0]
consumer_secret = dev_keys[1]
access_token = dev_keys[2]
access_token_secret = dev_keys[3]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# search keyword 'e' as it is the most common letter
search_words = "e -filter:retweets"

# change the number of items to 60000 to get the negative set
tweets = tweepy.Cursor(api.search_tweets,
              q=search_words,
              lang="en").items(250)

# corona keywords in the positive set
corona_keywords = np.loadtxt('./keywords.tsv', dtype=str, delimiter='\n')

file = open('./dataset/neg/neg_tweets.csv', 'w', encoding='utf-8', newline='')
file_info = open('./dataset/neg/info/neg_tweets_info.csv', 'w', encoding='utf-8', newline='')
file_all = open('./dataset/neg/info/all_tweets.csv', 'w', encoding='utf-8', newline='')

writer = csv.writer(file)
writer_info = csv.writer(file_info)
writer_all = csv.writer(file_all)

for index, tweet in enumerate(tweets):
    # replace newline characters with space
    tweet_text = tweet.text.replace('\n', ' ')
    if not any(keyword in tweet_text.lower() for keyword in corona_keywords):
        writer.writerow([tweet_text])
        writer_info.writerow([tweet_text, tweet.id, tweet.created_at, tweet.geo])

    writer_all.writerow([tweet_text, tweet.id, tweet.created_at, tweet.geo])
file.close()
file_info.close()
file_all.close()
