# Generated by Django 4.1.3 on 2022-11-27 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Passengers",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fname", models.CharField(max_length=20)),
                ("lname", models.CharField(max_length=20)),
                ("travel_points", models.CharField(max_length=200)),
            ],
        ),
    ]