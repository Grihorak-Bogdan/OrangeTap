# Generated by Django 3.2.13 on 2023-03-11 08:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0042_auto_20230311_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='my_friends', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Friend',
        ),
    ]
