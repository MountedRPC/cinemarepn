# Generated by Django 3.2.8 on 2021-10-16 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20211016_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cinemas',
            name='image1_cinemas',
            field=models.ImageField(blank=True, upload_to='media/databaseImageFiles'),
        ),
        migrations.AlterField(
            model_name='cinemas',
            name='image2_cinemas',
            field=models.ImageField(blank=True, upload_to='media/databaseImageFiles'),
        ),
        migrations.AlterField(
            model_name='cinemas',
            name='image3_cinemas',
            field=models.ImageField(blank=True, upload_to='media/databaseImageFiles'),
        ),
    ]