# Generated by Django 5.0.6 on 2024-06-16 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiWine', '0002_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='isAdmin',
            field=models.BooleanField(default=False),
        ),
    ]
