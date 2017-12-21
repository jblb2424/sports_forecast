# from stattlepy import Stattleship #
from django.core.management.base import BaseCommand

from common.models import Game, Team
from common.seat_geek_wrapper import GameGenerator

class Command(BaseCommand):

	def handle(self, *args, **options):
		games = GameGenerator()
		teams = Team.objects.all()
		for team in teams:
			team_city = team.city
			team_name = team.name
			# print(team_name)
			games.save_games_for_team(team_name, team_city)
		print('done!')


