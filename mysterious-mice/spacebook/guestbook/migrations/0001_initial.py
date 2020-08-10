# Generated by Django 3.0.8 on 2020-08-03 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Guestbook",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("author", models.TextField()),
                ("text", models.TextField()),
                ("email", models.EmailField(max_length=254)),
                ("published_date", models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
