from django.db import models

# Create your models here.
class TextSection(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.IntegerField()