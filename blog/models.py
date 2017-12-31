# Create your models here.
from django.db import models
from . import views

class Post(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    date = models.DateField()
    description = models.URLField(max_length=255)
    model_pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

    def picture(self):
        return self.model_pic.name


