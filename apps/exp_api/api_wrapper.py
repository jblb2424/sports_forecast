import urllib.request
import json
class API():
	url = 'http://localhost:8000/api/v1/'

	def get_games(self):
		game_url = self.url+ "games/"
		request = urllib.request.Request(game_url)
		resp_games = urllib.request.urlopen(request).read().decode('utf-8')
		json_games = json.loads(resp_games)
		return json_games

	def get_teams(self):
		team_url = self.url+ "teams/"
		request = urllib.request.Request(team_url)
		resp_teams = urllib.request.urlopen(request).read().decode('utf-8')
		json_teams = json.loads(resp_teams)
		return json_teams

	def get_comments(self):
		pass

	def get_team_detail(self, pk):
		team_url = self.url+ "teams/" + pk
		request = urllib.request.Request(team_url)
		resp_teams = urllib.request.urlopen(request).read().decode('utf-8')
		json_teams = json.loads(resp_teams)
		return json_teams

	def get_comments_detail(self, pk):
		comments_url = self.url+ "comments/" + pk
		request = urllib.request.Request(comments_url)
		resp_comments = urllib.request.urlopen(request).read().decode('utf-8')
		json_comments = json.loads(resp_comments)
		return json_comments