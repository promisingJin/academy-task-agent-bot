# Generated by Django 5.2.4 on 2025-07-04 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Teacher",
            fields=[
                ("teacher_id", models.IntegerField(primary_key=True, serialize=False)),
                ("passwd", models.CharField(max_length=100)),
                ("age", models.IntegerField()),
                ("name", models.CharField(max_length=100)),
                ("position", models.CharField(max_length=100)),
                ("sex", models.CharField(max_length=100)),
            ],
        ),
    ]
