# Generated by Django 3.2.13 on 2023-03-03 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_auto_20230303_1024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='prof',
        ),
    ]
