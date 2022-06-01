from django.db import models

# Create your models here.
class List(models.Model):
    icon_img = models.CharField(max_length=2000)
    # CharField defaults to 200
    icon_description = models.CharField
    time_todo = models.CharField

