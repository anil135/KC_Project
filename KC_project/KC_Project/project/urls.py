from django.urls import path,include
from project.views import newslist
from . import views 
urlpatterns = [
     path('articles',views.newslist,name='articles')
]
