import urllib, urllib.request
# url = 'http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=2'
url = 'http://export.arxiv.org/api/query?search_query=au:del_maestro'
data = urllib.request.urlopen(url)
print(data.read().decode('utf-8'))