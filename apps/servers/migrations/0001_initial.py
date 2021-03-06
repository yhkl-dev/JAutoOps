# Generated by Django 3.2.6 on 2021-08-22 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServerAliCloudInstanceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('InstanceName', models.CharField(default=None, help_text='InstanceName', max_length=100, null=True, verbose_name='实例名称')),
                ('SerialNumber', models.CharField(default=None, help_text='SerialNumber', max_length=100, null=True, unique=True, verbose_name='实例序列号')),
                ('CreationTime', models.DateTimeField(default=None, help_text='CreationTime', null=True, verbose_name='实例创建时间')),
                ('Status', models.CharField(default=None, help_text='Status', max_length=20, null=True, verbose_name='实例状态')),
                ('OSNameEn', models.CharField(default=None, help_text='OSNameEn', max_length=100, null=True, verbose_name='实例操作系统的英文名称')),
                ('InstanceNetworkType', models.CharField(default=None, help_text='InstanceNetworkType', max_length=100, null=True, verbose_name='InstanceNetworkType')),
                ('Memory', models.CharField(default=None, help_text='Memory(MB)', max_length=10, null=True, verbose_name='Memory')),
                ('Cpu', models.CharField(default=None, help_text='Cpu', max_length=10, null=True, verbose_name='Cpu')),
                ('HostName', models.CharField(default=None, help_text='Cpu', max_length=100, null=True, verbose_name='HostName')),
                ('IpAddress', models.CharField(default=None, help_text='IpAddress', max_length=39, null=True, verbose_name='IpAddress')),
                ('OSType', models.CharField(default=None, help_text='OSType', max_length=40, null=True, verbose_name='OSType')),
                ('RegionId', models.CharField(default=None, help_text='RegionId', max_length=40, null=True, verbose_name='RegionId')),
                ('StartTime', models.DateTimeField(help_text='start time', null=True, verbose_name='StartTime')),
                ('ExpiredTime', models.DateTimeField(help_text='expired time', null=True, verbose_name='ExpiredTime')),
                ('LastUpdateTime', models.DateTimeField(auto_now=True, help_text='last update time', verbose_name='last update datetime')),
                ('resource_name', models.ForeignKey(help_text='resource name', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='t_resource_name', to='resources.resource', verbose_name='resource info')),
            ],
            options={
                'db_table': 't_server',
                'ordering': ['id'],
            },
        ),
    ]
