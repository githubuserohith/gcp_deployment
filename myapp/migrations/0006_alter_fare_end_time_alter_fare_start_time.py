# Generated by Django 5.0.2 on 2024-04-03 20:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0005_fare"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fare",
            name="end_time",
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name="fare",
            name="start_time",
            field=models.DateTimeField(),
        ),
    ]
