# Generated by Django 5.1.2 on 2024-10-22 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("acrelog", "0007_event_note"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="event",
            name="id",
        ),
        migrations.AddField(
            model_name="event",
            name="primary_key",
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
