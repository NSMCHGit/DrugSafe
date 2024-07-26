
# Create your models here.
from __future__ import unicode_literals

from django.db import models

class Image(models.Model):
    #title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.image


class Document(models.Model):
	Name = models.CharField(max_length=255, blank=True)
	Age = models.CharField(max_length=10,blank=True)
	location = models.CharField(max_length=20,blank=True)
	
class safedrug(models.Model):
	drugname=models.CharField(max_length=255,blank=True)


