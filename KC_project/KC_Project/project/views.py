from django.shortcuts import render

# Create your views here.
from project.models import news

def newslist(request):
    headlines = news.objects.all()
    return render(request,'homepage.html',{'headlines':headlines})
