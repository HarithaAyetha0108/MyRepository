# Generated by Django 5.0.1 on 2024-01-25 05:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0004_remove_person_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="person",
            name="status",
            field=models.CharField(default="Active", max_length=30),
        ),
    ]
