# Generated by Django 4.2 on 2024-03-06 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocabulary_app', '0006_alter_author_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
