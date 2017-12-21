from common.models import Comment, Game, Team
from common.sentiment import Sentiment
import praw as Praw
from praw.models import MoreComments

class RedditGenerator():
	abbreivations = {"Facebook": "FB",  "Twitter": "TW",  "Instagram": "IG",  "Reddit": "RE"}
	def get_authentication(self):
		reddit = Praw.Reddit(client_id='CQXo3JmLvsZq_g',
                 client_secret='yZH2mkiAdVXR9XV6foCjMfoL-rU',
                 user_agent='davehodg/0.1')
		return reddit


	def analyze_all_comments(self, team1, team2, league):
		praw = self.get_authentication()
		subreddits = list(praw.subreddits.search(team1))
		
		for subreddit in subreddits:
			print(subreddit)
			comments = subreddit.comments(limit = 10000)
			for comment in comments:
				if team1 in comment.body and team2 in comment.body:
					print(comment.body)
					# team_supported = self.generate_sentiment(team1, team2, comment.body)
					# self.save_comment(comment.body, team_supported)




	def generate_sentiment(self, team1, team2, comment):
		analyzer = Sentiment()
		team_supported = analyzer.team_supported_two_teams_mentioned(team1, team2, comment)
		return team_supported



	def save_comment(self, comment, team_supported):
		if team_supported != "Neutral" and team_supported != "" and team_supported != None:
			print("Team" + " " + team_supported)
			team_supported_obj = Team.objects.get(name = team_supported)
			Comment.objects.create(
				media_outlet = self.abbreivations["Reddit"],
				comment_text = comment,
				team_to_win = team_supported
			)