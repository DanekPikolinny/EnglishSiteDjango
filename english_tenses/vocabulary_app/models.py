from typing import Iterable
from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class TextTranslate(models.Model):
    translated_text = models.TextField()


class Author(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    age = models.IntegerField()
    slug = models.SlugField(default="", db_index=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.first_name} {self.last_name}")
        super(Author, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    

class TextSection(models.Model):
    HARD = 'H'
    MEDIUM = 'M'
    EASY = 'E'
    
    DIF_CHOICES = [
        (HARD, 'HARD'),
        (MEDIUM, 'MEDIUM'),
        (EASY, 'EASY'),
    ]

    title = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.IntegerField()
    slug = models.SlugField(default='', null=False, db_index=True)
    difficulty = models.CharField(max_length=1, choices=DIF_CHOICES, default=EASY)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name='texts', null=True)

    def get_url(self):
        return reverse('choosen_text', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(TextSection, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.title} with rated: {self.rating}'
    