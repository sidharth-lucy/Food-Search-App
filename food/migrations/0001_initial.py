# Generated by Django 4.2.2 on 2023-06-21 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Dish",
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
                ("dishId", models.IntegerField()),
                ("dishName", models.CharField(max_length=150)),
                ("location", models.CharField(max_length=150)),
                ("items", models.JSONField()),
                ("lat_long", models.CharField(max_length=30)),
                ("detail", models.JSONField()),
            ],
        ),
    ]
