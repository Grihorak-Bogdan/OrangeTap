# Generated by Django 3.2.13 on 2023-02-11 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20230211_1427'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='Friend',
        ),
        migrations.RenameField(
            model_name='friend',
            old_name='profile',
            new_name='prof',
        ),
        migrations.RemoveField(
            model_name='user',
            name='friend',
        ),
        migrations.AddField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(related_name='my_friends', to='users.Friend'),
        ),
    ]