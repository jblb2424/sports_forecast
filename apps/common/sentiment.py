import re
from textblob import TextBlob

class Sentiment():
	def clean_tweet(self, tweet):
		return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())


	def get_tweet_sentiment(self, tweet):
		'''
		Utility function to classify sentiment of passed tweet
		using textblob's sentiment method
		'''
		# create TextBlob object of passed tweet text
		analysis = TextBlob(self.clean_tweet(tweet))
		# set sentiment
		if analysis.sentiment.polarity > 0:
			return 'positive'
		elif analysis.sentiment.polarity == 0:
			return 'neutral'
		else:
			return 'negative'


	def team_supported_one_team_mentioned(self, team1, team2, tweet):
		result = self.get_tweet_sentiment(tweet)
		team_from_tweet = ""
		opposing_team = ""

		if team1 in tweet:
			team_from_tweet = team1
			opposing_team = team2
		elif team2 in tweet:
			team_from_tweet= team2
			opposing_team = team1

		if result == 'positive':
			return team_from_tweet
		elif result == 'negative':
			return opposing_team
		else:
			return "Neutral"
