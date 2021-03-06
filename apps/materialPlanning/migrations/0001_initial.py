# Generated by Django 3.2.6 on 2021-10-24 09:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('material', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MaterialPlanningModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GICategory', models.CharField(default=None, help_text='GICategoryID', max_length=100, null=True, verbose_name='GI类别')),
                ('StorageLocation', models.CharField(default=None, help_text='StorageLocation', max_length=100, null=True, verbose_name='存储库位')),
                ('PartDescriptionZh', models.CharField(default=None, help_text='PartDescriptionZh', max_length=100, null=True, verbose_name='零件描述(中文)')),
                ('PartDescriptionEN', models.CharField(default=None, help_text='PartDescriptionEN', max_length=100, null=True, verbose_name='零件描述(英文)')),
                ('Dimension', models.CharField(default=None, help_text='Dimension', max_length=100, null=True, verbose_name='技术数据')),
                ('MinStock', models.CharField(default=None, help_text='MinStock', max_length=100, null=True, verbose_name='安全库存')),
                ('MaxStock', models.CharField(default=None, help_text='MaxStock', max_length=100, null=True, verbose_name='最大库存量')),
                ('HandoverStock', models.CharField(default=None, help_text='HandoverStock', max_length=100, null=True, verbose_name='初始移交库存')),
                ('Unit', models.CharField(default=None, help_text='Unit', max_length=100, null=True, verbose_name='计量单位')),
                ('ManufacturerName', models.CharField(default=None, help_text='ManufacturerName', max_length=100, null=True, verbose_name='制造商名称')),
                ('ManufacturerModel', models.CharField(default=None, help_text='ManufacturerModel', max_length=100, null=True, verbose_name='制造商的规格型号')),
                ('ManufacturerPartNumber', models.CharField(default=None, help_text='ManufacturerPartNumber', max_length=100, null=True, verbose_name='制造商的订货号')),
                ('SupplierCode', models.CharField(default=None, help_text='SupplierCode', max_length=100, null=True, verbose_name='供应商编码')),
                ('SupplierName', models.CharField(default=None, help_text='SupplierName', max_length=100, null=True, verbose_name='供应商名称')),
                ('SupplierModel', models.CharField(default=None, help_text='SupplierModel', max_length=100, null=True, verbose_name='供应商的规格型号')),
                ('SupplierPartNumber', models.CharField(default=None, help_text='SupplierPartNumber', max_length=100, null=True, verbose_name='供应商的订货号')),
                ('SupplierContactPerson', models.CharField(default=None, help_text='SupplierContactPerson', max_length=100, null=True, verbose_name='供应商联系人')),
                ('SupplierContactPhone', models.CharField(default=None, help_text='SupplierContactPhone', max_length=100, null=True, verbose_name='供应商联系电话')),
                ('SupplierEmail', models.CharField(default=None, help_text='SupplierEmail', max_length=100, null=True, verbose_name='供应商邮箱')),
                ('FCNo', models.CharField(default=None, help_text='FCNo', max_length=100, null=True, verbose_name='框架协议号码')),
                ('UnitPrice', models.CharField(default=None, help_text='UnitPrice', max_length=100, null=True, verbose_name='单价')),
                ('Currency', models.CharField(default=None, help_text='Currency', max_length=100, null=True, verbose_name='货币')),
                ('EquipmentName', models.CharField(default=None, help_text='EquipmentName', max_length=100, null=True, verbose_name='设备名称')),
                ('Repairable', models.CharField(default=None, help_text='Repairable', max_length=100, null=True, verbose_name='可修理的零件')),
                ('Calibration', models.CharField(default=None, help_text='Calibration', max_length=100, null=True, verbose_name='校准件')),
                ('Drawing', models.CharField(default=None, help_text='Drawing', max_length=100, null=True, verbose_name='图纸号')),
                ('InstallationQuantity', models.CharField(default=None, help_text='InstallationQuantity', max_length=100, null=True, verbose_name='安装数量')),
                ('PartSpecialTreatment', models.CharField(default=None, help_text='PartSpecialTreatment', max_length=100, null=True, verbose_name='零件特殊处理')),
                ('SurplusStock', models.CharField(default=None, help_text='SurplusStock', max_length=100, null=True, verbose_name='剩余库存')),
                ('EngineerUser', models.ForeignKey(help_text='维修计划负责人', on_delete=django.db.models.deletion.CASCADE, related_name='EngineerUser', to=settings.AUTH_USER_MODEL, verbose_name='EngineerUser')),
                ('ImportanceLevel', models.ForeignKey(help_text='采购类型', on_delete=django.db.models.deletion.CASCADE, related_name='importance_level', to='material.importancelevelmodel', verbose_name='importance_level')),
                ('MaterialNumber', models.ForeignKey(help_text='零件号', on_delete=django.db.models.deletion.CASCADE, related_name='material_basic_info', to='material.materialmodel', verbose_name='material_basic_info')),
                ('PlantTechCode', models.ForeignKey(help_text='TechnologyCode', on_delete=django.db.models.deletion.CASCADE, related_name='plant_tech_code_info', to='material.technologycode', verbose_name='plant_tech_code_info')),
                ('PurchaseType', models.ForeignKey(help_text='采购类型', on_delete=django.db.models.deletion.CASCADE, related_name='purchase_type_info', to='material.purchasetypemodel', verbose_name='purchase_type_info')),
                ('material_group_name', models.ForeignKey(help_text='MaterialGroup', on_delete=django.db.models.deletion.CASCADE, related_name='material_group_name', to='material.materialgroup', verbose_name='material_group_name')),
                ('plant', models.ForeignKey(help_text='工厂代码', on_delete=django.db.models.deletion.CASCADE, related_name='plant_info', to='material.plant', verbose_name='plant_info')),
            ],
            options={
                'db_table': 't_material_planning',
                'ordering': ['id'],
            },
        ),
    ]
