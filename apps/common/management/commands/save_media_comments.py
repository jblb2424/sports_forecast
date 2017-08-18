from twython import Twython #Twitter API wrapper
from django.core.management.base import BaseCommand
from common.models import Comment, Game, Team
from common.sentiment import Sentiment
from common.twitter_wrapper import TwitterGenerator

#TODO: More comprehensive social media analysis, fix duplicate comments
#Twitter, retweets and stuff

class Command(BaseCommand):
	
	def handle(self, *args, **options):
		Twitter = TwitterGenerator()
		games = Game.objects.all()
		for game in games:
			teams = game.teams.all()
			team1 = teams[0].name
			team2 = teams[1].name
			Twitter.generate_sentiment_and_save(team1, team2)


