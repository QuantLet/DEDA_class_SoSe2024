import tweepy

# Replace with your own credentials
consumer_key = 'FV3FC3OOojtWgAqrdDXVwvBlk'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAJudtwEAAAAAyeYEb6xDQFv83R1eX0nFdz9lKw8%3DHN5fOyrGGaZE4uGvvIugi0uT1ijeNzpmePtn6KPECQD7o8ASJF'
consumer_secret = 'RW97oqiCzPtKn7FPzwsQXhPwGLQDDfbuGHHnArdrxUZMLtoeAN'
access_token = '1791398915113205760-obLLCohz2A2qN0xzkTag9nAibDNQre'
access_token_secret = 'CPP7DKKcBI3zwtl2wjMBy4HbdbaAdvXxuNghHKgPA4u9I'

auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

hashtag = '#ChatGPT'
tweets = tweepy.Cursor(api.search_tweets, q=hashtag, lang="en").items(5)

tweet_texts = [tweet.text for tweet in tweets]

from textblob import TextBlob

for tweet in tweet_texts:
    analysis = TextBlob(tweet)
    print(f'Tweet: {tweet}\nSentiment: {analysis.sentiment}\n')

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

for tweet in tweet_texts:
    vs = analyzer.polarity_scores(tweet)
    print(f'Tweet: {tweet}\nSentiment: {vs}\n')

import matplotlib.pyplot as plt

sentiments = [analyzer.polarity_scores(tweet)['compound'] for tweet in tweet_texts]

plt.hist(sentiments, bins=20)
plt.xlabel('Sentiment Score')
plt.ylabel('Frequency')
plt.title('Sentiment Analysis of #YourBrand')
plt.show()