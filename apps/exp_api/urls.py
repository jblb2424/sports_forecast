from django.conf.urls import url

from . import views

urlpatterns = [
url(r'load_teams', views.load_teams, name = 'load_teams'),
url(r'team_detail/(?P<pk>\d+)', views.team_detial, name = 'team_detail'),
url(r'load_games_from_team/(?P<pk>\d+)', views.load_games_from_team, name = 'load_games_from_team'),
url(r'load_comments_from_game/(?P<pk>\d+)', views.load_comments_from_game, name = 'load_comments_from_game'),
url(r'load_stats/(?P<pk>\d+)', views.load_stats, name = 'load_stats'),

]