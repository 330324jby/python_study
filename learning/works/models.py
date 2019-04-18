from django.db import models

# Create your models here.
class movie_name(models.Model):
    name=models.CharField(max_length=100)
    def __unicode__(self):
        return self.name

class artical(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    def __unicode__(self):
        return self.title,self.content