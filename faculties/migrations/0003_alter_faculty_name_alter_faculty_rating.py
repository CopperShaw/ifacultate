# Generated by Django 5.0.7 on 2024-09-18 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("faculties", "0002_faculty_county"),
    ]

    operations = [
        migrations.AlterField(
            model_name="faculty",
            name="name",
            field=models.CharField(db_index=True, max_length=128),
        ),
        migrations.AlterField(
            model_name="faculty",
            name="rating",
            field=models.DecimalField(
                decimal_places=1, default=0.0, max_digits=2, null=True
            ),
        ),
    ]