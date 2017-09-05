from newsapi.articles import Articles
from newsapi.sources import Sources
from attrdict import AttrDict

s = Sources(API_KEY="3f7f2beb76764ae8a3e89f45954a235a")


a = Articles(API_KEY="3f7f2beb76764ae8a3e89f45954a235a")


#iterate through each news source
for i in s.get_by_category('sport').sources:
	
	source_id = i['id']
	print(source_id)
	source = a.get(source = source_id)
	

	#for article in source.articles:
		#print(article['title'])