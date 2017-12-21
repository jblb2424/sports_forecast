from django.conf.urls import url

from . import views

urlpatterns = [
url(r'comments/create/', views.post_comment.as_view(), name = 'post_comments'),
url(r'games/create/', views.post_game.as_view(), name = 'post_games'),
url(r'games/(?P<pk>\d+)', views.game_detail.as_view(), name = 'game_detail'),
url(r'teams/(?P<pk>\d+)', views.team_detail.as_view(), name = 'team_detail'),
url(r'comments/(?P<pk>\d+)', views.get_comments_from_game.as_view(), name = 'games'),
url(r'games/', views.get_games.as_view(), name = 'games'),
url(r'teams/', views.get_teams.as_view(), name = 'teams'),
url(r'comments/', views.get_comments.as_view(), name = 'comments'),


]
