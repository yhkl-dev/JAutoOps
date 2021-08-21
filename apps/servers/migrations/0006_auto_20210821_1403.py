# Generated by Django 3.2.6 on 2021-08-21 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0005_serveralicloudinstancemodel_lastupdatetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serveralicloudinstancemodel',
            name='InstanceName',
            field=models.CharField(default=None, help_text='InstanceName', max_length=100, null=True, verbose_name='实例名称'),
        ),
        migrations.AlterField(
            model_name='serveralicloudinstancemodel',
            name='SerialNumber',
            field=models.CharField(default=None, help_text='SerialNumber', max_length=100, null=True, unique=True, verbose_name='实例序列号'),
        ),
    ]