# Generated by Django 3.2.6 on 2021-08-21 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0002_auto_20210821_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='update_at',
            field=models.DateTimeField(auto_now=True, help_text='update time', verbose_name='update time'),
        ),
    ]
