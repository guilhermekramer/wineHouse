# Generated by Django 5.0.6 on 2024-06-17 23:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apiWine', '0007_wine_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='favorites',
        ),
        migrations.DeleteModel(
            name='Favorite',
        ),
    ]
