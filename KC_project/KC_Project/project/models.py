from django.db import models
from django.utils import timezone

# Create your models here.
class news(models.Model):
    Id=models.IntegerField(default="")
    Date=models.DateField(default='timezone.now')
    Title= models.CharField(max_length=30,default='SOME STRING')
    Details=models.CharField(max_length=100,default='SOME STRING')
    Newsfrom=models.CharField(max_length=50,default='SOME STRING')
    URLofnews=models.CharField(max_length=100,default='SOME STRING')
    

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['title']
    class Admin:
        pass