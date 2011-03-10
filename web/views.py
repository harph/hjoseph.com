from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render_to_response
from django.utils import simplejson
from datetime import datetime
from urllib import urlopen


def index(request):
	return render_to_response("index.html")


def get_tweets(request):
	tweets = []
	try:
		f = urlopen('http://api.twitter.com/1/statuses/user_timeline/harph.json')
		timeline = f.read()
		f.close()
		tweets = [dict(text = tweet["text"], date = _parse_tweet_date(tweet["created_at"])) for tweet in simplejson.loads(timeline)[:5]]
	except Exception, e:
		tweets = []
		
	template_values = {'tweets' : tweets}
	return render_to_response("twitter.html", template_values)


def _parse_tweet_date(strDate):
	return strDate[:11] + strDate[-4:] + ' ' + strDate[12:19]


def get_posts(request):
	posts = []
	try:
		f = urlopen('http://blog.hjoseph.com/api/read/json')
		blog_posts = f.read()[22:-2]
		f.close()
		post_index = 0
		json_posts =  simplejson.loads(blog_posts)['posts']
		while len(posts) < 3:
			if json_posts[post_index]["type"] == 'regular':
				posts.append(dict(
					regularTitle =  json_posts[post_index]['regular-title'],
					regularBody =  json_posts[post_index]['regular-body'],
					date =   _parse_blog_date(json_posts[post_index]['date-gmt'])
				))
			post_index += 1
	except Exception, e:
		print e
		posts = []

	template_values = {'posts' : posts}
	return render_to_response("blog.html", template_values)

def _parse_blog_date(strDate):
	monthName = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
	strDate = datetime.strptime(strDate[:-4], '%Y-%m-%d %H:%M:%S')
	return monthName[strDate.month - 1] + ' ' + str(strDate.day) + ' ' + str(strDate.year) 
	
	
def get_portafolio_project(request, project_name):
	return render_to_response("portafolio_projects/%s.html" % project_name, {'project_name': project_name})
