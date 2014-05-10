import requests
from BeautifulSoup import BeautifulSoup

urls = {
	"top": "https://news.google.com/",
	"technology": "https://news.google.com/news/section?pz=1&cf=all&topic=tc&siidp=d0efb8be4bc7ba6cc8df32977c99fad01f8b",
	"science": "https://news.google.com/news/section?pz=1&cf=all&topic=snc&siidp=d0efb8be4bc7ba6cc8df32977c99fad01f8b",
	"health": "https://news.google.com/news/section?pz=1&cf=all&topic=m&siidp=d0efb8be4bc7ba6cc8df32977c99fad01f8b",
	"world": "https://news.google.com/news/section?pz=1&cf=all&topic=w&siidp=d0efb8be4bc7ba6cc8df32977c99fad01f8b",
	"us": "https://news.google.com/news/section?pz=1&cf=all&topic=n&siidp=d0efb8be4bc7ba6cc8df32977c99fad01f8b",
	"business": "https://news.google.com/news/section?pz=1&cf=all&topic=b&siidp=d0efb8be4bc7ba6cc8df32977c99fad01f8b",
	"entertainment": "https://news.google.com/news/section?pz=1&cf=all&topic=e&siidp=d0efb8be4bc7ba6cc8df32977c99fad01f8b",
	"sports": "https://news.google.com/news/section?pz=1&cf=all&topic=s&siidp=d0efb8be4bc7ba6cc8df32977c99fad01f8b&ict=ln"
}

topics = {}

for i in urls.keys():
	link = urls[i]
	page = requests.get(link)
	html = page.content

	soup = BeautifulSoup(html)
	topic_elements = soup.find("div", {"class": "topic-list"}).contents
	topics[i] = map(lambda x: str(x.text), topic_elements)

query_params = {
	'apikey': 'cc6a5b98c9f6426584c174bc737776c0'
}

endpoint = 'http://capitolwords.org/api/text.json'
