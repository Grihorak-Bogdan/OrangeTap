# Generated by Django 3.2.13 on 2023-03-14 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0062_auto_20230314_2142'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ChatMessage',
        ),
    ]