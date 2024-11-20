# Generated by Django 5.0.7 on 2024-08-15 07:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0001_initial"),
        ("universities", "0002_alter_university_options_university_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="review",
            name="university",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="universities.university",
            ),
        ),
    ]