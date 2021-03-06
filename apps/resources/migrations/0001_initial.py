# Generated by Django 3.2.6 on 2021-08-22 11:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(default=None, help_text='resource type name', max_length=30, verbose_name='resource type name')),
                ('type_icon', models.CharField(default=None, help_text='resource type icon', max_length=30, verbose_name='resource type icon')),
            ],
            options={
                'db_table': 't_resource_type',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource_name', models.CharField(db_index=True, default=None, help_text='resource name', max_length=50, unique=True, verbose_name='resource name')),
                ('access_key', models.CharField(default=None, help_text='access key', max_length=100, verbose_name='access key')),
                ('access_secret', models.CharField(default=None, help_text='access secret', max_length=100, verbose_name='access secret')),
                ('main_account', models.CharField(default=None, help_text='main account for tencent', max_length=100, null=True, verbose_name='main account')),
                ('ram_username', models.CharField(default=None, help_text='ram user', max_length=100, verbose_name='ram_user')),
                ('ram_password', models.CharField(default=None, help_text='ram user password', max_length=100, verbose_name='ram_password')),
                ('create_at', models.DateTimeField(auto_now_add=True, help_text='create time', verbose_name='create time')),
                ('update_at', models.DateTimeField(auto_now=True, help_text='update time', verbose_name='update time')),
                ('description', models.CharField(blank=True, default=None, help_text='description', max_length=200, verbose_name='description')),
                ('belong_user', models.ForeignKey(help_text='belong user', on_delete=django.db.models.deletion.CASCADE, related_name='belong_user', to=settings.AUTH_USER_MODEL, verbose_name='belong user')),
                ('resource_type', models.ForeignKey(help_text='resource type', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resource_type', to='resources.resourcetype', verbose_name='resource type')),
            ],
            options={
                'db_table': 't_resource',
                'ordering': ['id'],
            },
        ),
    ]
