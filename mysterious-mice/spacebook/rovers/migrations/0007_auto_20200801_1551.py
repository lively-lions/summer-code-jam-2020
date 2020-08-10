# Generated by Django 3.0.8 on 2020-08-01 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rovers", "0006_rover_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="rover",
            name="status",
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="rover",
            name="image",
            field=models.ImageField(
                default="profile_pictures/default.jpg", upload_to="profile_pictures"
            ),
        ),
    ]
