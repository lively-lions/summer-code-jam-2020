# Generated by Django 2.2.7 on 2020-08-09 02:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='HubUser',
        ),
    ]
