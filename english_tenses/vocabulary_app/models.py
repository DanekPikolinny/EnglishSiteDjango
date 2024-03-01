from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class TextSection(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.IntegerField()
    slug = models.SlugField(default='', null=False, db_index=True)

    def get_url(self):
        return reverse('choosen_text', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(TextSection, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.title} with rated: {self.rating}'