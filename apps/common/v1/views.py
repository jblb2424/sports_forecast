from django.shortcuts import render
from django.http import HttpResponse
import urllib.request
from common.exp_api_wrapper import EXP_API

api = EXP_API()
def index(request):
	data = api.load_teams()
	teams = data['data']
	return render(request, 'index.html', {'teams': teams})


def detail(request, pk):
	data = api.load_games(pk)
	games = data['data']
	comment_data = {}
	count_data = []
	for game in games['games']:
		game_id = game['id']
		matchup = game['matchup']
		comments = api.load_comments(str(game_id))
		stats = api.load_stats(str(game_id))
		team_detail = api.team_detail(pk)

		comment_data[matchup] = comments['data']
		count_data.append(stats['counts'])
	return render(request, 'teamDetail.html', {'game_detail': comment_data, 'counts' : count_data, 'team': team_detail})