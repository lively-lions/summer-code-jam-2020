# Generated by Django 3.0.8 on 2020-08-03 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200803_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='topic_name',
            field=models.CharField(default='', max_length=20, unique=True),
        ),
    ]
