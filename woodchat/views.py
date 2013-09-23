# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

def hello(request):
	return HttpResponse("Hello World!")

def index_page(request):
	# return HttpResponseRedirect('base.html')
	return render_to_response('index.html')

def about_us_page(request):
	# return HttpResponseRedirect('base.html')
	return render_to_response('aboutus.html')

def our_products_page(request):
	# return HttpResponseRedirect('base.html')
	return render_to_response('ourproducts.html')

def contact_us_page(request):
	# return HttpResponseRedirect('base.html')
	return render_to_response('contactus.html')			