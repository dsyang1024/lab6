# Generated by Django 5.1.2 on 2024-10-22 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("acrelog", "0009_rename_primary_key_event_event_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="event",
            name="event_id",
        ),
        migrations.AddField(
            model_name="event",
            name="id",
            field=models.BigAutoField(
                auto_created=True,
                default=0,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
            preserve_default=False,
        ),
    ]
