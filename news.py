import requests
from unidecode import unidecode
from BeautifulSoup import BeautifulSoup
from time import sleep

class statement(object):
	def __init__(self, first, last, state, quote, c_url, o_url, date):
		self.first = first
		self.last = last
		self.state = state
		self.quote = quote
		self.c_url = c_url
		self.o_url = o_url
		self.date = date

		choices = ["None", None, "null"]
		if first in choices or last in choices:
			str1 = "On %s, an Anonymous Speaker from " % date
		else:
			str1 = "On %s, %s %s from " % (date, first, last)
		if state in choices:
			str2 = "an unknown state said: \n\n%s" % '\n\n'.join(quote)
		else:
			str2 = "%s said:\n\n%s" % (state, '\n\n'.join(quote))
		self.data = (str1 + str2).split('\n')
		self.print_v = str1 + str2
	def __repr__(self):
		if self.last in ["None", None, "null"]:
			string = "<Statement 'Anonymous'>"
		else:
			string = "<Statement '%s'>" % self.last.encode('utf-8')
		return string


urls = {
	"top": "https://news.google.com/",
	"technology": "https://news.google.com/news/section?pz=1&cf=all&topic=tc&siidp=d0efb8be4bc7ba6cc8df32977c99fad01f8b",
	"science": "https://news.google.com/news/section?pz=1&cf=all&topic=snc&siidp=d0efb8be4bc7ba6cc8df32977c99fad01f8b",
	"health": "https://news.google.com/news/section?pz=1&cf=all&topic=m&siidp=d0efb8be4bc7ba6cc8df32977c99fad01f8b",
	"world": "https://news.google.com/news/section?pz=1&cf=all&topic=w&siidp=d0efb8be4bc7ba6cc8df32977c99fad01f8b",
	"us": "https://news.google.com/news/section?pz=1&cf=all&topic=n&siidp=d0efb8be4bc7ba6cc8df32977c99fad01f8b",
	"business": "https://news.google.com/news/section?pz=1&cf=all&topic=b&siidp=d0efb8be4bc7ba6cc8df32977c99fad01f8b",
	"entertainment": "https://news.google.com/news/section?pz=1&cf=all&topic=e&siidp=df2ca71c8c66d6de2740fe990f310a585159&ict=ln",
	"sports": "https://news.google.com/news/section?pz=1&cf=all&topic=s&siidp=8ee0c495033e0b8db8248317af6767f35d79&ict=ln"
}

topics = {}

for i in urls.keys():
	sleep(1)
	link = urls[i]
	page = requests.get(link)
	html = page.content

	soup = BeautifulSoup(html)
	topic_elements = soup.find("div", {"class": "topic-list"}).contents
	for x in topic_elements:
		place = topic_elements.index(x)
		x = x.text
		x = unidecode(x)
		topic_elements[place] = x

	new_dict = {}
	for y in topic_elements:
		new_dict.update({y: []})
	topics[i] = new_dict

query_params = {
	'apikey': 'cc6a5b98c9f6426584c174bc737776c0',
	'sort': 'date desc'
}

endpoint = 'http://capitolwords.org/api/text.json'

for i in topics.keys():
	for x in topics[i].keys():
		query_params['phrase'] = x
		response = requests.get(endpoint, params=query_params)
		sleep(1)
		data = response.json()["results"]
		
		for z in data:
			if data != []:
				date = z["date"]
				first = z["speaker_first"]
				last = z["speaker_last"]
				state = z["speaker_state"]
				quote = z["speaking"]
				c_url = z["capitolwords_url"]
				o_url = z["origin_url"]
				
				obj = statement(first, last, state, quote, c_url, o_url, date)
			else:
				obj = None
	
			topics[i][x].append(obj)
