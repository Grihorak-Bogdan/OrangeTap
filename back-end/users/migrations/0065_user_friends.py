# Generated by Django 3.2.13 on 2023-03-14 18:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0064_remove_user_friends'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='my_friends', to=settings.AUTH_USER_MODEL),
        ),
    ]
