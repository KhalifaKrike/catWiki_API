# Generated by Django 4.1.7 on 2023-06-03 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catBreeds', '0003_alter_catbreed_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='catbreed',
            name='popularity',
            field=models.IntegerField(default=0),
        ),
    ]
