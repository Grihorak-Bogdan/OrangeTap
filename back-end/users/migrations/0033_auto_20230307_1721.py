# Generated by Django 3.2.13 on 2023-03-07 14:21

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0032_alter_user_friends'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='my_friends', to='users.Friend'),
        ),
    ]
