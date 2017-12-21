import urllib.request
import json
import datetime as DT
from datetime import datetime
from common.models import Game, Team

class GameGenerator():
	abbreviations = {"football": "FO", "baseball": "BA", "soccer": "SO", "hockey": "HO", "tennis": "TE", "basketball": "BS"}
	
	def configure_url(self, team_name, team_city):
		compiled_name = (team_city.lower() + "-" + team_name.lower()).replace(" ", "-")
		#The API used is called Seat Geek
		url = "https://api.seatgeek.com/2/events?&performers.slug=" + compiled_name + "&client_id=ODQ4MzIyMXwxNTAyNDgyMjU1LjQz&client_secret=c3dc5e6c5cd0d1ca48fc24ac6f35ced578671bcdf345b8ef0988db29e8e74ea0"
		return url




	def save_games_for_team(self, team_name, team_city):
		
		url = self.configure_url(team_name, team_city)

		returned_json = urllib.request.urlopen(url).read().decode("UTF-8")
		decoded_json = json.loads(returned_json)
		games = decoded_json["events"] # <-----upcoming games for a given team
		today = DT.date.today()
		week_later = today + DT.timedelta(days=7) 

		for game in games:
			date = game["datetime_local"]# <-----the date of the game
			datetime_object = datetime.strptime(date[0:10],  "%Y-%m-%d").date()

			#If the game is coming up, and within this week...
			if datetime_object < week_later:
				teams = []
				#Grab the team names from the JSON and save it to new game object
				for team in game["performers"]: # <-----the teams in play
					city_and_name = team["name"].split()
					#Ex. Giants in "New York Giants"
					if city_and_name[-1] == "Blazers": #Hardcode for Trail Blazers, weird case
						teams.append(city_and_name[-2]  + " " + city_and_name[-1])
					else:
						teams.append(city_and_name[-1])
					print(teams)
				sport = team_obj = Team.objects.get(name = teams[0]).sport #figure out which sport we're playing!
				team_obj1 = Team.objects.get(name = teams[0])
				team_obj2 = Team.objects.get(name = teams[1])
				if Game.objects.filter(teams = team_obj1).filter(teams=team_obj2).exists() == False:
					game_obj = Game.objects.create(sport = self.abbreviations[sport], date = datetime_object)
					team_obj1.games.add(game_obj)
					team_obj2.games.add(game_obj)
		print('done!')