# Generated by Django 3.2.13 on 2023-03-11 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0048_alter_user_friends'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='my_friends', to='users.Friend'),
        ),
    ]