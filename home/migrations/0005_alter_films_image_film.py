# Generated by Django 3.2.8 on 2021-10-11 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_films_short_info_film'),
    ]

    operations = [
        migrations.AlterField(
            model_name='films',
            name='image_film',
            field=models.ImageField(blank=True, upload_to='databaseImageFiles'),
        ),
    ]