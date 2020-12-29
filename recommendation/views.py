from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	return render(request,'recommendation/home.html')

def productOverview(request):
    return render(request,'recommendation/productOverview.html')


def writeReview(request):
    return render(request,'recommendation/writeReview.html')    	

def login(request):
    return render(request,'recommendation/login.html')    