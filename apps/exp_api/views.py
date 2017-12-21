from django.shortcuts import render
from django.http import HttpResponse
import urllib.request
from exp_api.api_wrapper import API
from django.http import JsonResponse
from .statistic import Statistic
# Create your views here.

api = API()
def load_games(request): #Do I need this?
	teams = api.get_teams()
	games = api.get_games()
	composed_game_names = {}


	for game in games:
		teams = game['teams']
		sport = game['sport']

		if composed_game_names.get(sport) == None:
			composed_game_names[sport] = []

		if len(teams) == 2:
			verbose_name = teams[0] + " vs " + teams[1]
			composed_game_names[sport].append(verbose_name)

	return JsonResponse({'data': composed_game_names})


def load_teams(request):
	teams = api.get_teams()
	composed_team_names = {}
	for team in teams:
		sport = team['sport']
		city = team['city']
		name = team['name']
		pk = team['id']
		verbose_name = city + " " + name

		if composed_team_names.get(sport) == None:
			composed_team_names[sport] = []

		
		composed_team_names[sport].append({'name' : verbose_name, 'pk': pk})

	return JsonResponse({'data': composed_team_names})


def load_games_from_team(request, pk):
	team  = api.get_team_detail(pk)
	games = api.get_games()
	city = team['city']
	name = team['name']
	verbose_name = city + " " + name
	current_games = []

	for game in games:
		if verbose_name in game['teams']:
			matchup = game['teams'][0] + "  vs.  " + game['teams'][1]
			if matchup not in current_games : current_games.append({'id': game['id'], 'matchup': matchup})

	return JsonResponse({'data': {'team': verbose_name, 'games' : current_games}})



def load_comments_from_game(request, pk):
	comments = api.get_comments_detail(pk)
	return JsonResponse({'data': comments})


def load_stats(request, pk):
	stats = Statistic()
	comments = api.get_comments_detail(pk)
	tweet_data = stats.count_tweets(comments)
	name_data = {}
	for pk in tweet_data.keys():
		team_info = api.get_team_detail(str(pk))
		name = team_info['name']
		name_data[name] = tweet_data[pk]
	return JsonResponse({'counts': name_data})


def team_detial(request, pk):
	detail = api.get_team_detail(pk)
	return JsonResponse(detail)
