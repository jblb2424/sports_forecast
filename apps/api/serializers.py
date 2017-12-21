
from rest_framework import serializers
from common.models import Game,Team,Comment


class GameSerializer(serializers.ModelSerializer):
	teams = serializers.StringRelatedField(many=True)
	class Meta:
		model = Game
		fields = "__all__"


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = "__all__"



class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"