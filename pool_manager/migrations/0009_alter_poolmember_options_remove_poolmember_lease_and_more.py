# Generated by Django 4.2.6 on 2023-11-07 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pool_manager', '0008_rename_poolmembers_poolmember'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='poolmember',
            options={'ordering': ('range_number',)},
        ),
        migrations.RemoveField(
            model_name='poolmember',
            name='lease',
        ),
        migrations.RemoveField(
            model_name='poolmember',
            name='pool',
        ),
    ]