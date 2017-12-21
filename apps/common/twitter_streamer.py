from twython import TwythonStreamer
from common.models import Comment, Game, Team
from common.sentiment import Sentiment
from twython import Twython #Twitter API wrapper
from django.views.decorators.csrf import csrf_exempt
import urllib.request
import urllib.parse

class MyStreamer(TwythonStreamer):
	names = ['Cardinals', 'Falcons', 'Ravens', 'Bills', 'Panthers', 'Bears',
		'Bengals', 'Browns', 'Cowboys', 'Cowboys', 'Broncos', 'Lions', 'Packers',
		'Texans', 'Colts', 'Jaguars', 'Chiefs', 'Dolphins', 'Vikings', 'Patriots',
		'Saints', 'Giants', 'Jets', 'Raiders', 'Eagles', 'Steelers','Chargers','49ers',
		'Seahawks', 'Rams', 'Buccaneers', 'Titans', 'Redskins'
			]



	def on_success(self, data):
		if 'text' in data:
			t = data['text']
			self.main(t, self.names, 'football')

			#teams = []
			# for name in self.names:
			# 	if name in t:
			# 		teams.append(name)
			# if len(teams) == 2: #Change this!
			# 	team_supported = self.generate_sentiment(teams[0], teams[1], t)
			# 	associated_game = self.find_game(teams[0], teams[1])
			# 	print('NO!    ' + t)
			# 	if associated_game != None:
			# 		print('YES!!!!    ' + t)
			# 		self.save_comment(team_supported, t, associated_game)



	def on_error(self, status_code, data):
		print(status_code)


	def find_game(self,team1, team2):
		try:
			associated_game = Game.objects.filter(teams = team1).get(teams = team2)
			return associated_game
		except:
			return None


	def generate_sentiment(self, team1, team2, comment):
		analyzer = Sentiment()
		team_supported = analyzer.team_supported_two_teams_mentioned(team1, team2, comment)
		return team_supported


	@csrf_exempt
	def save_comment(self,team_supported, t, game):
		if team_supported != "Neutral" and team_supported != "" and team_supported != None:
			team_supported_obj = Team.objects.get(name = team_supported)
			media_outlet = 'TW'
			comment_text = t
			print('saving....')
			url = 'http://localhost:8000/api/v1/comments/create/'
			data = {'media_outlet': media_outlet, 'comment_text': comment_text, 
			'team_to_win' : team_supported_obj.pk, 'game' : game.pk}
			
			data = bytes( urllib.parse.urlencode( data ).encode() )
			handler = urllib.request.urlopen(url, data);


	def main(self,t, arr, sport):
		teams = []
		for name in self.names:
			if name in t:
				teams.append(name)

		if len(teams) == 2: #Change this!
			team1 = teams[0]
			team2 = teams[1]
			team_obj_1 = Team.objects.filter(name = team1).get(sport = sport)
			team_obj_2 = Team.objects.filter(name = team2).get(sport = sport)
			
			team_supported = self.generate_sentiment(teams[0], teams[1], t)
			associated_game = self.find_game(team_obj_1, team_obj_2)
			
			print('NO!    ' + t)
			if associated_game != None:
				print('YES!!!!    ' + t)
				self.save_comment(team_supported, t, associated_game)
			