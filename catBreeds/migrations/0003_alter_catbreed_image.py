# Generated by Django 4.1.7 on 2023-03-10 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catBreeds', '0002_rename_name_catbreed_breed_catbreed_adaptability_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catbreed',
            name='image',
            field=models.URLField(blank=True),
        ),
    ]
