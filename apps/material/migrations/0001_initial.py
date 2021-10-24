# Generated by Django 3.2.6 on 2021-10-24 09:32

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
            name='HandoverTypeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(default=None, help_text='type_name', max_length=100, null=True, verbose_name='type_name')),
                ('comment', models.CharField(default=None, help_text='comment', max_length=100, null=True, verbose_name='comment')),
                ('create_at', models.DateTimeField(auto_now_add=True, help_text='create time', verbose_name='create time')),
            ],
            options={
                'db_table': 't_handover_type',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ImportanceLevelModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_name', models.CharField(default=None, help_text='level_name', max_length=100, null=True, verbose_name='level_name')),
                ('comment', models.CharField(default=None, help_text='comment', max_length=100, null=True, verbose_name='comment')),
                ('create_at', models.DateTimeField(auto_now_add=True, help_text='create time', verbose_name='create time')),
            ],
            options={
                'db_table': 't_importance_level',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='MaterialGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(default=None, help_text='plant_name', max_length=100, null=True, verbose_name='group_name')),
                ('comment', models.CharField(default=None, help_text='plant_name', max_length=100, null=True, verbose_name='comment')),
                ('create_at', models.DateTimeField(auto_now_add=True, help_text='create time', verbose_name='create time')),
            ],
            options={
                'db_table': 't_material_group',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant_name', models.CharField(default=None, help_text='plant_name', max_length=100, null=True, verbose_name='零件号')),
                ('plant_code', models.CharField(default=None, help_text='plant_name', max_length=100, null=True, verbose_name='零件号')),
                ('comment', models.CharField(default=None, help_text='plant_name', max_length=100, null=True, verbose_name='零件号')),
                ('create_at', models.DateTimeField(auto_now_add=True, help_text='create time', verbose_name='create time')),
            ],
            options={
                'db_table': 't_plant',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='PurchaseTypeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_type_name', models.CharField(default=None, help_text='purchase_type_name', max_length=100, null=True, verbose_name='purchase_type_name')),
                ('comment', models.CharField(default=None, help_text='comment', max_length=100, null=True, verbose_name='comment')),
                ('create_at', models.DateTimeField(auto_now_add=True, help_text='create time', verbose_name='create time')),
            ],
            options={
                'db_table': 't_purchase_type',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='TechnologyCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant_tech_code_name', models.CharField(default=None, help_text='plant_name', max_length=100, null=True, verbose_name='零件号')),
                ('plant_tech_code', models.CharField(default=None, help_text='plant_name', max_length=100, null=True, verbose_name='零件号')),
                ('comment', models.CharField(default=None, help_text='plant_name', max_length=100, null=True, verbose_name='零件号')),
                ('create_at', models.DateTimeField(auto_now_add=True, help_text='create time', verbose_name='create time')),
            ],
            options={
                'db_table': 't_plant_technology_code',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='MaterialModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MaterialDescriptionEN', models.CharField(default=None, help_text='MaterialDescriptionEN', max_length=100, null=True, verbose_name='MaterialDescriptionEN')),
                ('MaterialDescriptionZH', models.CharField(default=None, help_text='MaterialDescriptionZH', max_length=100, null=True, verbose_name='MaterialDescriptionZH')),
                ('ManufacturerName', models.CharField(default=None, help_text='ManufacturerName', max_length=100, null=True, verbose_name='ManufacturerName')),
                ('ManufacturerPartNumber', models.CharField(default=None, help_text='ManufacturerPartNumber', max_length=100, null=True, verbose_name='ManufacturerPartNumber')),
                ('ManufacturerModel', models.CharField(default=None, help_text='ManufacturerModel', max_length=100, null=True, verbose_name='ManufacturerModel')),
                ('Unit', models.CharField(default=None, help_text='Unit', max_length=100, null=True, verbose_name='Unit')),
                ('Calibration', models.CharField(default=None, help_text='Calibration', max_length=100, null=True, verbose_name='Calibration')),
                ('Repairable', models.CharField(default=None, help_text='Repairable', max_length=100, null=True, verbose_name='Repairable')),
                ('Material', models.CharField(default=None, help_text='Material', max_length=100, null=True, verbose_name='Material')),
                ('CCCorCCCRelated', models.CharField(default=None, help_text='CCCorCCCRelated', max_length=100, null=True, verbose_name='CCCorCCCRelated')),
                ('PositionNumber', models.CharField(default=None, help_text='PositionNumber', max_length=100, null=True, verbose_name='PositionNumber')),
                ('MaterialMainClassification', models.CharField(default=None, help_text='MaterialMainClassification', max_length=100, null=True, verbose_name='MaterialMainClassification')),
                ('MaterialSubClassification', models.CharField(default=None, help_text='MaterialSubClassification', max_length=100, null=True, verbose_name='MaterialSubClassification')),
                ('ManufactureModelOld1', models.CharField(default=None, help_text='ManufactureModelOld1', max_length=100, null=True, verbose_name='ManufactureModelOld1')),
                ('ManufactureModelOld2', models.CharField(default=None, help_text='ManufactureModelOld2', max_length=100, null=True, verbose_name='ManufactureModelOld2')),
                ('ManufacturePNOld1', models.CharField(default=None, help_text='ManufacturePNOld1', max_length=100, null=True, verbose_name='ManufacturePNOld1')),
                ('ManufacturePNOld2', models.CharField(default=None, help_text='ManufacturePNOld2', max_length=100, null=True, verbose_name='ManufacturePNOld2')),
                ('Dimension', models.CharField(default=None, help_text='Dimension', max_length=100, null=True, verbose_name='Dimension')),
                ('MaterialSpecialTreatment', models.CharField(default=None, help_text='MaterialSpecialTreatment', max_length=100, null=True, verbose_name='MaterialSpecialTreatment')),
                ('MPRemark', models.CharField(default=None, help_text='MPRemark', max_length=100, null=True, verbose_name='MPRemark')),
                ('TechRemark', models.CharField(default=None, help_text='TechRemark', max_length=100, null=True, verbose_name='TechRemark')),
                ('SupplierName', models.CharField(default=None, help_text='SupplierName', max_length=100, null=True, verbose_name='SupplierName')),
                ('SurplusPoint', models.CharField(default=None, help_text='SurplusPoint', max_length=100, null=True, verbose_name='SurplusPoint')),
                ('InstallQty', models.CharField(default=None, help_text='InstallQty', max_length=100, null=True, verbose_name='InstallQty')),
                ('create_at', models.DateTimeField(auto_now_add=True, help_text='create time', verbose_name='create time')),
                ('HandoverType', models.ForeignKey(help_text='HandoverType', on_delete=django.db.models.deletion.CASCADE, related_name='HandoverType', to='material.handovertypemodel', verbose_name='HandoverType')),
                ('ImportanceLevel', models.ForeignKey(help_text='ImportanceLevel', on_delete=django.db.models.deletion.CASCADE, related_name='ImportanceLevel', to='material.importancelevelmodel', verbose_name='ImportanceLevel')),
                ('MaterialGroup', models.ForeignKey(help_text='MaterialGroup', on_delete=django.db.models.deletion.CASCADE, related_name='MaterialGroup', to='material.materialgroup', verbose_name='MaterialGroup')),
                ('PlantTechCode', models.ForeignKey(help_text='TechnologyCode', on_delete=django.db.models.deletion.CASCADE, related_name='TechnologyCode', to='material.technologycode', verbose_name='RespInfo')),
                ('RespInfo', models.ForeignKey(help_text='负责人信息', on_delete=django.db.models.deletion.CASCADE, related_name='RespInfo', to=settings.AUTH_USER_MODEL, verbose_name='RespInfo')),
            ],
            options={
                'db_table': 't_material',
                'ordering': ['id'],
            },
        ),
    ]
