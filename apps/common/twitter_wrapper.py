from common.models import Comment, Game, Team
from common.sentiment import Sentiment
from twython import Twython #Twitter API wrapper

class TwitterGenerator():
	abbreivations = {"Facebook": "FB",  "Twitter": "TW",  "Instagram": "IG",  "Reddit": "RE"}
	APP_KEY = '2GV8V8dlFzTJGfZZg89bmKedq'
	APP_SECRET = 'kYjQAwx5dOi5gQsCW0agG74FW7roY02SEugMNUjNSTIYcD91W0'
	CONSUMER_KEY = '2GV8V8dlFzTJGfZZg89bmKedq'
	CONSUMER_SECRET = 'kYjQAwx5dOi5gQsCW0agG74FW7roY02SEugMNUjNSTIYcD91W0'
	twitter = Twython(APP_KEY, APP_SECRET) #Twitter API wrapper
	
	def obtain_authentication(self):
		auth = self.twitter.get_authentication_tokens(callback_url='https://mysite.com/callback')
		OAUTH_TOKEN = auth['oauth_token']
		OAUTH_TOKEN_SECRET = auth['oauth_token_secret']
		return {'OAUTH_TOKEN': OAUTH_TOKEN, 'OAUTH_TOKEN_SECRET': OAUTH_TOKEN_SECRET}


	def grab_twitter_comments(self, team1, team2):
		print(team1.name + " " + team2.name)
		results = results = twitter.cursor(twitter.search, q = '''"''' + team1.name + '''"''' + " " + '''"''' + team2.name + '''"''' , count = 100, tweet_mode='extended', return_pages = True) #Query tweets with BOTH teams in the name
			# results1 = twitter.search(q = team1, count = 3)
			# results2 = twitter.search(q = team2, count = 3)
		all_tweets = []
		for page in results:
			for item in page:
				all_tweets.append(item)
				print()
		return all_tweets
			

	def find_game(self,team1, team2):
		# compiled_team = sorted([team1, team2]) #Team names in order in database
		associated_game = Game.objects.filter(teams = team1).get(teams = team2)
		print('working')
		return associated_game
	


	def analyze_all_comments(self, team1, team2):
		tweets = self.grab_twitter_comments(team1, team2)


		for comment in tweets:
			t = comment["full_text"]
			team_supported_obj = None

			if (team1.name in t and team2.name in t):

				team_supported = self.generate_sentiment(team1, team2, t)
				associated_game = self.find_game(team1, team2)
				self.save_comment(team_supported, t, associated_game)


	def generate_sentiment(self, team1, team2, comment):
		analyzer = Sentiment()
		team_supported = analyzer.team_supported_two_teams_mentioned(team1.name, team2.name, comment)
		return team_supported


	def save_comment(self,team_supported, comment, game):
		if team_supported != "Neutral" and team_supported != "" and team_supported != None:
			team_supported_obj = Team.objects.get(name = team_supported)
			if Comment.objects.all().filter(comment_text = comment).exists() == False:
				Comment.objects.create(
					media_outlet = self.abbreivations["Twitter"],
					comment_text = comment,
					team_to_win = team_supported_obj,
					game = game
				)
