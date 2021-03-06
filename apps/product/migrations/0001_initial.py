# Generated by Django 3.2.6 on 2021-08-22 16:15

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
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(help_text='product name', max_length=50, unique=True, verbose_name='product_name')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='create time', verbose_name='create_time')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='update time', verbose_name='update_time')),
                ('create_user', models.ForeignKey(help_text='create user', on_delete=django.db.models.deletion.CASCADE, related_name='created_user', to=settings.AUTH_USER_MODEL, verbose_name='create user')),
            ],
            options={
                'db_table': 't_product',
                'ordering': ['id'],
            },
        ),
    ]
