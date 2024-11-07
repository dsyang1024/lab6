# Generated by Django 5.1.2 on 2024-10-24 19:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acrelog', '0011_remove_fertilizer_powerunit_type_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='log',
            old_name='log_date',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='log',
            name='fertilizer',
        ),
        migrations.RemoveField(
            model_name='log',
            name='operation',
        ),
        migrations.RemoveField(
            model_name='log',
            name='seed',
        ),
        migrations.AddField(
            model_name='log',
            name='event',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='acrelog.event'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='log',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='acrelog.location'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='log',
            name='operator',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='acrelog.operator'),
            preserve_default=False,
        ),
    ]
