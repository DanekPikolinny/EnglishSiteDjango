# Generated by Django 4.2 on 2024-03-01 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocabulary_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='textsection',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]