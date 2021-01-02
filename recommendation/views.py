from django.shortcuts import render
from django.http import HttpResponse
from .models import Service
# Create your views here.

def index(request):
	return render(request,'recommendation/home.html')

def productOverview(request):
    return render(request,'recommendation/productOverview.html')


def writeReview(request):
    return render(request,'recommendation/writeReview.html')    	

def login(request):
    return render(request,'recommendation/login.html')    


def search(request):
	query=request.GET['query']
	allResults=Service.objects.filter(serviceType__icontains=query)
	params={'allResults':allResults}
	return render(request,'recommendation/search.html',params)
