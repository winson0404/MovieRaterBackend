# Generated by Django 3.2.5 on 2022-01-23 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_aired_at_movie_aired_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image_url',
            field=models.URLField(default='https://i.kym-cdn.com/entries/icons/original/000/020/002/memeeman.jpg'),
        ),
    ]