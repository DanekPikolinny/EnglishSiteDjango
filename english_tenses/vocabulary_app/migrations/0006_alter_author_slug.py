# Generated by Django 4.2 on 2024-03-06 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocabulary_app', '0005_author_textsection_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='slug',
            field=models.SlugField(default='', null=True),
        ),
    ]
