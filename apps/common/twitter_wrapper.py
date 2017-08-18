from common.models import Comment, Game, Team
from common.sentiment import Sentiment
from twython import Twython #Twitter API wrapper

class TwitterGenerator():
	abbreivations = {"Facebook": "FB",  "Twitter": "TW",  "Instagram": "IG",  "Reddit": "RE"}

	def grab_twitter_comments(self, team1, team2):
			APP_KEY = '2GV8V8dlFzTJGfZZg89bmKedq'
			APP_SECRET = 'kYjQAwx5dOi5gQsCW0agG74FW7roY02SEugMNUjNSTIYcD91W0'

			twitter = Twython(APP_KEY, APP_SECRET) #Twitter API wrapper
			results = twitter.search(q = team1 + " " + team2, count = 3) #Query tweets with BOTH teams in the name
			# results1 = twitter.search(q = team1, count = 3)
			# results2 = twitter.search(q = team2, count = 3)
			tweets = results['statuses']
			return tweets
			

	def generate_sentiment_and_save(self, team1, team2):
		tweets = self.grab_twitter_comments(team1, team2)
		analyzer = Sentiment()

		for comment in tweets:
			t = comment["text"]
			team_supported_obj = None

			if (team1 in t and team2 in t) == True: #CHANGE THIS :)
				team_supported = analyzer.team_supported_one_team_mentioned(team1, team2, t)
				

				if team_supported != "Neutral" and team_supported != "" and team_supported != None:
					print("Team" + " " + team_supported)
					team_supported_obj = Team.objects.get(name = team_supported)
					Comment.objects.create(
						media_outlet = self.abbreivations["Twitter"],
						comment_text = t,
						team_to_win = team_supported_obj
					)