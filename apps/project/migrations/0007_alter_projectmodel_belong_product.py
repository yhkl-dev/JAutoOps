# Generated by Django 3.2.6 on 2021-08-26 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
        ('project', '0006_alter_projectmodel_belong_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectmodel',
            name='belong_product',
            field=models.ForeignKey(default=None, help_text='belong product', on_delete=django.db.models.deletion.CASCADE, related_name='belong_product', to='product.productmodel', verbose_name='belong product'),
        ),
    ]
