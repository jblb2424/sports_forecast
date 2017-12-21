from django.shortcuts import render
from common.models import Game, Team, Comment
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAdminUser


from . import serializers
# Create your views here.

class get_games(generics.ListAPIView):
	queryset = Game.objects.all()
	serializer_class = serializers.GameSerializer

class get_teams(generics.ListAPIView):
	queryset = Team.objects.all()
	serializer_class = serializers.TeamSerializer


class post_game(generics.CreateAPIView):
	queryset = Game.objects.all()
	serializer_class = serializers.GameSerializer


class post_comment(generics.CreateAPIView):	
	queryset = Comment.objects.all()
	serializer_class = serializers.CommentSerializer
	#permission_classes = (IsAdminUser,)

class get_comments_from_game(generics.ListAPIView):
	serializer_class = serializers.CommentSerializer

	def get_queryset(self):
		game = self.kwargs['pk']
		return Comment.objects.filter(game=game)


class get_comments(generics.ListAPIView):
	queryset = Comment.objects.all()
	serializer_class = serializers.CommentSerializer
	

class game_detail(generics.RetrieveAPIView):
	queryset = Game.objects.all()
	serializer_class = serializers.GameSerializer


class team_detail(generics.RetrieveAPIView):
	queryset = Team.objects.all()
	serializer_class = serializers.TeamSerializer
