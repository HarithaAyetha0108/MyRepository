# Generated by Django 5.0.1 on 2024-01-25 05:28

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0003_alter_person_status"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="person",
            name="status",
        ),
    ]
