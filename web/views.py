from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render_to_response


def index(request):
	return render_to_response("index.html")
