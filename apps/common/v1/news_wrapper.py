from newsapi.articles import articles
from newsapi.sources import Sources

s = Sources(API_KEY="3f7f2beb76764ae8a3e89f45954a235a")


a = Articles(API_KEY="3f7f2beb76764ae8a3e89f45954a235a")

s.get()