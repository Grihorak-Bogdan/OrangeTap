# Generated by Django 3.2.13 on 2023-02-22 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20230222_1254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='fri',
        ),
        migrations.AddField(
            model_name='user',
            name='fri',
            field=models.ManyToManyField(related_name='fri', to='users.Friend'),
        ),
    ]
