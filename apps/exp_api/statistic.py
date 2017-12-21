from collections import Counter
class Statistic(): #Wrapper for performing statistics on JSON data
	def count_tweets(self, resp):
		all_id = [d['team_to_win'] for d in resp]
		c = Counter(all_id)
		ret_dict = dict(c)
		return ret_dict

	def mean():
		pass