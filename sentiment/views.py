from django.shortcuts import render
from django.template import loader
from django.views.generic.base import TemplateView
from .scripts import sentimentnifty,sentiment
def index(request):
    return render(request, 'sentiment/home.html')

def about(request):
    return render(request, 'sentiment/about.html')

def aspire(request):
    return render(request, 'sentiment/aspire.html')

def result(request):
    Index_in = request.POST.get('Index',False)
    
    if(Index_in=='1'):
        print (Index_in)
        res=sentimentnifty.res()
    elif (Index_in=='2'):
        
        res=sentiment.res()
    context ={
        "res": res
        }
        
    return render(request, 'sentiment/result.html',context)
def indices(request):
    

    
    return render(request, 'sentiment/index.html')

    
