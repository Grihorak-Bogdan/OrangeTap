# Generated by Django 3.2.13 on 2023-03-03 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_auto_20230303_1352'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friend',
            old_name='profile',
            new_name='profi',
        ),
    ]
