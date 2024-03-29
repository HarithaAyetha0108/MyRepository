# Generated by Django 5.0.1 on 2024-02-27 06:57

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Visit",
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
                ("name", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=100)),
                ("email", models.CharField(max_length=100)),
                ("floor", models.IntegerField()),
                ("resources", models.CharField(max_length=100)),
            ],
        ),
    ]
