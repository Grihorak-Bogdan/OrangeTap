# Generated by Django 3.2.13 on 2023-02-19 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20230219_2059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='following',
        ),
        migrations.AddField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(related_name='my_friends', to='users.Friend'),
        ),
    ]
