# Generated by Django 3.2.8 on 2021-10-13 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_films_image_film'),
    ]

    operations = [
        migrations.AlterField(
            model_name='films',
            name='video_film',
            field=models.FileField(blank=True, upload_to='media/databaseVideoFilms'),
        ),
    ]
