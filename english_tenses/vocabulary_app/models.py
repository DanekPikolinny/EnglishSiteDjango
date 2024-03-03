from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class TextSection(models.Model):
    HARD = 'H'
    MEDIUM = 'M'
    EASY = 'E'
    
    dif = [
        (HARD, 'HARD'),
        (MEDIUM, 'MEDIUM'),
        (EASY, 'EASY'),
    ]

    title = models.CharField(max_length=100)
    text = models.TextField()
    text_translate = models.TextField(null=True)
    rating = models.IntegerField()
    slug = models.SlugField(default='', null=False, db_index=True)
    difficulty = models.CharField(max_length=1, choices=dif, default=EASY)

    def get_url(self):
        return reverse('choosen_text', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(TextSection, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.title} with rated: {self.rating}'