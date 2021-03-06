import twitter

def extract_tweet_entities(statuses):

 # See https://dev.twitter.com/docs/tweet-entities for more details on tweet
 # entities
 if len(statuses) == 0:
 return [], [], [], [], []

 screen_names = [ user_mention['screen_name']
 for status in statuses
 for user_mention in status['entities']['user_mentions'] ]

 hashtags = [ hashtag['text']
 for status in statuses
 for hashtag in status['entities']['hashtags'] ]
 urls = [ url['expanded_url']
 for status in statuses
 for url in status['entities']['urls'] ]

 symbols = [ symbol['text']
 for status in statuses
 for symbol in status['entities']['symbols'] ]

 # In some circumstances (such as search results), the media entity
 # may not appear
 if status['entities'].has_key('media'):
 media = [ media['url']
 for status in statuses
 for media in status['entities']['media'] ]
 else:
 media = []
 return screen_names, hashtags, urls, media, symbols
# Sample usage
q = 'CrossFit'
statuses = twitter_search(twitter_api, q)
screen_names, hashtags, urls, media, symbols = extract_tweet_entities(statuses)