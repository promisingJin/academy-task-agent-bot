# Generated by Django 5.2.4 on 2025-07-04 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0002_teacher"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Teacher",
        ),
    ]
