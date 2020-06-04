from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

def index(request):
    return render(request,"shop/index.html")

def contact(request):
    pass


def about(request):
    pass 
def tracker(request):
    pass 
def search(request):
    pass 
def prodView(request):
    pass
def checkout(request):
    pass
