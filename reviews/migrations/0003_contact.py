# Generated by Django 5.0.7 on 2024-08-19 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0002_review_university"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                ("title", models.TextField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                ("text", models.TextField(max_length=2555)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("completed", models.BooleanField(default=False)),
            ],
        ),
    ]
