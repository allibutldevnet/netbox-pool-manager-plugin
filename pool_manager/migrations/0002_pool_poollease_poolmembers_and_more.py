# Generated by Django 4.2.6 on 2023-11-07 03:02

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers
import utilities.json


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0098_webhook_custom_field_data_webhook_tags'),
        ('pool_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('range', models.TextField(blank=True)),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='PoolLease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('requester_id', models.PositiveIntegerField()),
                ('app_type', models.CharField(blank=True, max_length=30)),
                ('pool3', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lease_to_pool', to='pool_manager.pool')),
            ],
            options={
                'ordering': ('pool3', 'requester_id'),
            },
        ),
        migrations.CreateModel(
            name='PoolMembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=utilities.json.CustomFieldJSONEncoder)),
                ('range_number', models.PositiveIntegerField()),
                ('lease', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='lease_to_members', to='pool_manager.poollease')),
                ('pool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='pool_manager.pool')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'ordering': ('pool', 'range_number'),
            },
        ),
        migrations.AlterUniqueTogether(
            name='poolmanagerrule',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='poolmanagerrule',
            name='destination_prefix',
        ),
        migrations.RemoveField(
            model_name='poolmanagerrule',
            name='pool_manager',
        ),
        migrations.RemoveField(
            model_name='poolmanagerrule',
            name='source_prefix',
        ),
        migrations.RemoveField(
            model_name='poolmanagerrule',
            name='tags',
        ),
        migrations.DeleteModel(
            name='PoolManager',
        ),
        migrations.DeleteModel(
            name='PoolManagerRule',
        ),
        migrations.AddField(
            model_name='poollease',
            name='pool_member2',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='member_to_lease', to='pool_manager.poolmembers'),
        ),
        migrations.AddField(
            model_name='poollease',
            name='tags',
            field=taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag'),
        ),
        migrations.AlterUniqueTogether(
            name='poollease',
            unique_together={('pool3', 'requester_id')},
        ),
    ]
