# Generated by Django 4.2.7 on 2023-11-26 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("db", "0004_rename_format_literaryformat_name_alter_book_format"),
    ]

    operations = [
        migrations.RenameField(
            model_name="literaryformat",
            old_name="name",
            new_name="format",
        ),
        migrations.AlterField(
            model_name="book",
            name="format",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="db.literaryformat"
            ),
        ),
    ]