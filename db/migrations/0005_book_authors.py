# Generated by Django 4.2.7 on 2023-11-27 10:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("db", "0004_author"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="authors",
            field=models.ManyToManyField(to="db.author"),
        ),
    ]
