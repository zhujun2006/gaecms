# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

def hello(request):
	return HttpResponse("Hello World!")

def home(request):
	# return HttpResponseRedirect('base.html')
	return render_to_response('base.html')