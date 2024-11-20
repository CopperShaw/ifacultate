# Generated by Django 5.0.7 on 2024-08-30 17:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("faculties", "0002_faculty_county"),
        ("universities", "0002_alter_university_options_university_name_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="university",
            name="county",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="universities_set",
                to="faculties.county",
            ),
        ),
    ]