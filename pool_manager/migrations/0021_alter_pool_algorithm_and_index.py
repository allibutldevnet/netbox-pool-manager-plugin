# Generated by Django 5.0.9 on 2024-09-05 04:26

import django.core.validators
import django.db.models.deletion
import taggit.managers
import utilities.json
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pool_manager', '0020_alter_pool_range'),
    ]

    operations = [
        migrations.AddField(
            model_name='pool',
            name='algorithm',
            field=models.CharField(default='first_available', max_length=50)
        ),
        migrations.AddField(
            model_name='pool',
            name='index',
            field=models.PositiveIntegerField(blank=True, default=0)
        ),
    ]