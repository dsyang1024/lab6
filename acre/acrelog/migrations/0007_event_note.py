# Generated by Django 5.1.2 on 2024-10-22 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("acrelog", "0006_event_remove_operation_date_remove_operation_event_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="note",
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]