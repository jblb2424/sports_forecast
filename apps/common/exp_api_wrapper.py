
import urllib.request
import json
class EXP_API():
	url = 'http://localhost:8000/exp_api/v1/'
	def load_teams(self):
		team_url = self.url+ "load_teams/"
		request = urllib.request.Request(team_url)
		resp_teams = urllib.request.urlopen(request).read().decode('utf-8')
		json_teams = json.loads(resp_teams)
		return json_teams

	def load_games(self, pk):
		team_url = self.url+ "load_games_from_team/" + pk
		request = urllib.request.Request(team_url)
		resp_teams = urllib.request.urlopen(request).read().decode('utf-8')
		json_teams = json.loads(resp_teams)
		return json_teams

	def load_comments(self, pk):
		game_url = self.url+ "load_comments_from_game/" + pk
		request = urllib.request.Request(game_url)
		resp_game = urllib.request.urlopen(request).read().decode('utf-8')
		json_game = json.loads(resp_game)
		return json_game


	def load_stats(self, pk):
		stat_url = self.url+ "load_stats/" + pk
		request = urllib.request.Request(stat_url)
		resp_stat = urllib.request.urlopen(request).read().decode('utf-8')
		json_stat = json.loads(resp_stat)
		return json_stat
	

	def team_detail(self, pk):
		team_url = self.url+ "team_detail/" + pk
		request = urllib.request.Request(team_url)
		resp_teams = urllib.request.urlopen(request).read().decode('utf-8')
		json_teams = json.loads(resp_teams)
		return json_teams
