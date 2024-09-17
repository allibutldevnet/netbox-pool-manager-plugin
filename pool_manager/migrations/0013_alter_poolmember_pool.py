# Generated by Django 4.2.6 on 2023-11-08 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pool_manager', '0012_alter_poolmember_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poolmember',
            name='pool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='members', to='pool_manager.pool'),
        ),
    ]
