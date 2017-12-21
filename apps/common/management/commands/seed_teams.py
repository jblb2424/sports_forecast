from django.core.management.base import BaseCommand
from common.models import Team
import csv
import os



class Command(BaseCommand):
	help = 'Seeds teams for the site'
	def handle(self, *args, **options):
		teams_nfl_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'teams_NFL.csv')
		teams_nba_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'teams_NBA.csv')
		with open(teams_nfl_file) as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				city_and_name = row["Team Name"].split()
				#this whole portion groups city names together that are more than 1 word

				name = city_and_name[-1]
				print(name)
				city = " ".join(city_and_name[0: len(city_and_name)-1])
				sport = "football"
				league = "nfl"

				new_team = Team.objects.get_or_create(name=name, sport = sport, city = city)


		with open(teams_nba_file) as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				city_and_name = row["name"].split()
				#this whole portion groups city names together that are more than 1 word

				name = city_and_name[-1]
				print(name)
				city = " ".join(city_and_name[0: len(city_and_name)-1])
				sport = "basketball"
				league = "nba"
				if name == "Blazers": #Hardcode a weird name case :(
					new_team = Team.objects.get_or_create(name="Trail Blazers", sport = sport, city = 'Portland')
				else:
					new_team = Team.objects.get_or_create(name=name, sport = sport, city = city)
		print("Teams Done!")
