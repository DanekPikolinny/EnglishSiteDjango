# Generated by Django 4.2 on 2024-03-02 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocabulary_app', '0002_textsection_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='textsection',
            name='difficulty',
            field=models.CharField(choices=[('H', 'HARD'), ('M', 'MEDIUM'), ('E', 'EASY')], default='E', max_length=1),
        ),
    ]
