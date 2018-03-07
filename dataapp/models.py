from django.db import models

# Create your models here.


class Content(models.Model):
    page = models.CharField(max_length=25)
    title = models.CharField(max_length=30)
    content = models.TextField()

