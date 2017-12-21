from twython import Twython #Twitter API wrapper
from twython import TwythonStreamer
from django.core.management.base import BaseCommand
from common.models import Comment, Game, Team
from common.sentiment import Sentiment
from common.twitter_wrapper import TwitterGenerator
from common.twitter_streamer import  MyStreamer
from common.reddit_wrapper import RedditGenerator

#TODO: More comprehensive social media analysis, fix duplicate comments
#Twitter, retweets and stuff

class Command(BaseCommand):
	def handle(self, *args, **options):
		Twitter = TwitterGenerator()
		APP_KEY = '2GV8V8dlFzTJGfZZg89bmKedq'
		APP_SECRET = 'kYjQAwx5dOi5gQsCW0agG74FW7roY02SEugMNUjNSTIYcD91W0'
		ACCESS_TOKEN = '895502041950298112-DRTxX100gfvE2eJpue98cDTQk3Gb2ST'
		ACCESS_TOKEN_SECRET = 'xddY0m64M6IMziIFpeVnV6ZlTxu7fBj70WANjA9h7XPf1'

		oauth = Twitter.obtain_authentication()
		OAUTH_TOKEN = oauth['OAUTH_TOKEN']
		OAUTH_TOKEN_SECRET = oauth['OAUTH_TOKEN_SECRET']


		Twitter_Streamer =  MyStreamer(APP_KEY, APP_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
		# Reddit = RedditGenerator()
		# games = Game.objects.all()
		# for game in games:
		# 	teams = game.teams.all()
		# 	team1 = teams[0]
		# 	team2 = teams[1]
		# 	league = teams[0].league
		# 	Twitter.analyze_all_comments(team1, team2)
		names = ['Cardinals', 'Falcons', 'Ravens', 'Bills', 'Panthers', 'Bears',
		'Bengals', 'Browns', 'Cowboys', 'Cowboys', 'Broncos', 'Lions', 'Packers',
		'Texans', 'Colts', 'Jaguars', 'Chiefs', 'Dolphins', 'Vikings', 'Patriots',
		'Saints', 'Giants', 'Jets', 'Raiders', 'Eagles', 'Steelers','Chargers','49ers',
		'Seahawks', 'Rams', 'Buccaneers', 'Titans', 'Redskins'
		]
		Twitter_Streamer.statuses.filter(track=names)
			# Reddit.analyze_all_comments(team1, team2, league)


