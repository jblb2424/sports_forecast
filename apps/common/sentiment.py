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



	def team_supported_two_teams_mentioned(self, team1, team2, tweet):
		#index Location of both teams in the comment
		tweet_finer = tweet.lower()
		team_one_mention_index = tweet_finer.index(team1.lower()) 
		team_two_mention_index = tweet_finer.index(team2.lower())

		team_from_tweet = "" #First team mentioned
		opposing_team = ""   #Second team mentioned


		#Basically, figure out and record which team is mentioned first in the comment
		if team_one_mention_index < team_two_mention_index:
			team_one_mention_index += (len(team1) + 1)
			tweet_phrase = tweet[team_one_mention_index: team_two_mention_index]
			team_from_tweet = team1
			opposing_team = team2
		else:
			team_two_mention_index += (len(team2) + 1)
			tweet_phrase = tweet[team_one_mention_index: team_two_mention_index]
			team_from_tweet = team2
			opposing_team = team1
		
		#Grabs the sentiment of the phrase between the two teams mentioned
		#Ex "Giants will beat the Ravens" -> "will beat the"
		#This is to make sure there is sustanence in the tweet and not just "Giants vs Ravens"
		phrase_result = self.get_tweet_sentiment(tweet_phrase) 

		#The actual sentiment of the tweet
		result_full_tweet = self.get_tweet_sentiment(tweet) 


		if phrase_result == 'positive' or phrase_result == 'negative':
			if result_full_tweet == 'positive':
			
				return team_from_tweet
			elif result_full_tweet == 'negative':
	
				return opposing_team
			
		return "Neutral"




		

