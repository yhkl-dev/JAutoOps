from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()



class GICategoryModel(models.Model):
    type_name = models.CharField('type_name', max_length=100, null=True, default=None, help_text='type name')
    comment = models.CharField('comment', max_length=100, null=True, default=None, help_text='comment')
    create_at = models.DateTimeField('create time', auto_now_add=True, help_text='create time')

    def __str__(self):
        return self.type_name

    class Meta:
        ordering = ['id']
        db_table = 't_gi_category'

class MaterialGroup(models.Model):
    group_name = models.CharField('group_name', max_length=100, null=True, default=None, help_text='plant_name')
    comment = models.CharField('comment', max_length=100, null=True, default=None, help_text='plant_name')
    create_at = models.DateTimeField('create time', auto_now_add=True, help_text='create time')

    def __str__(self):
        return self.group_name

    class Meta:
        ordering = ['id']
        db_table = 't_material_group'


class Plant(models.Model):
    plant_name = models.CharField('plant_name', max_length=100, null=True, default=None, help_text='plant_name')
    plant_code = models.CharField('plant_code', max_length=100, null=True, default=None, help_text='plant_name')
    comment = models.CharField('comment', max_length=100, null=True, default=None, help_text='plant_name')
    create_at = models.DateTimeField('create time', auto_now_add=True, help_text='create time')

    def __str__(self):
        return f"{self.plant_name}: {self.plant_code}"

    class Meta:
        ordering = ['id']
        db_table = 't_plant'

class TechnologyCode(models.Model):
    plant_tech_code_name = models.CharField('plant_tech_code_name', max_length=100, null=True, default=None, help_text='plant_name')
    plant_tech_code = models.CharField('plant_tech_code', max_length=100, null=True, default=None, help_text='plant_name')
    comment = models.CharField('comment', max_length=100, null=True, default=None, help_text='plant_name')
    create_at = models.DateTimeField('create time', auto_now_add=True, help_text='create time')

    def __str__(self):
        return self.plant_tech_code_name

    class Meta:
        ordering = ['id']
        db_table = 't_plant_technology_code'



class PurchaseTypeModel(models.Model):
    purchase_type_name = models.CharField('purchase_type_name', max_length=100, null=True, default=None, help_text='purchase_type_name')
    comment = models.CharField('comment', max_length=100, null=True, default=None, help_text='comment')
    create_at = models.DateTimeField('create time', auto_now_add=True, help_text='create time')

    def __str__(self):
        return self.purchase_type_name

    class Meta:
        ordering = ['id']
        db_table = 't_purchase_type'


class HandoverTypeModel(models.Model):
    type_name = models.CharField('type_name', max_length=100, null=True, default=None,
                                          help_text='type_name')
    comment = models.CharField('comment', max_length=100, null=True, default=None, help_text='comment')
    create_at = models.DateTimeField('create time', auto_now_add=True, help_text='create time')

    def __str__(self):
        return self.type_name

    class Meta:
        ordering = ['id']
        db_table = 't_handover_type'


class ImportanceLevelModel(models.Model):
    level_name = models.CharField('level_name', max_length=100, null=True, default=None,
                                 help_text='level_name')
    comment = models.CharField('comment', max_length=100, null=True, default=None, help_text='comment')
    create_at = models.DateTimeField('create time', auto_now_add=True, help_text='create time')

    def __str__(self):
        return self.level_name

    class Meta:
        ordering = ['id']
        db_table = 't_importance_level'


class MaterialModel(models.Model):
    HandoverType = models.ForeignKey(HandoverTypeModel, on_delete=models.CASCADE, null=False,
                                      verbose_name='HandoverType',
                                      related_name='HandoverType', help_text='HandoverType')

    RespInfo = models.ForeignKey(User, on_delete=models.CASCADE, null=False, verbose_name='RespInfo',
                                 related_name='RespInfo', help_text='负责人信息')

    PlantTechCode = models.ForeignKey(TechnologyCode, on_delete=models.CASCADE, null=False, verbose_name='RespInfo',
                                 related_name='TechnologyCode', help_text='TechnologyCode')

    ImportanceLevel = models.ForeignKey(ImportanceLevelModel, on_delete=models.CASCADE, null=False, verbose_name='ImportanceLevel',
                                      related_name='ImportanceLevel', help_text='ImportanceLevel')
    MaterialGroup = models.ForeignKey(MaterialGroup, on_delete=models.CASCADE, null=False, verbose_name='MaterialGroup',
                                      related_name='MaterialGroup', help_text='MaterialGroup')

    MaterialDescriptionEN = models.CharField('MaterialDescriptionEN', max_length=100, null=True, default=None, help_text='MaterialDescriptionEN')
    MaterialDescriptionZH = models.CharField('MaterialDescriptionZH', max_length=100, null=True, default=None, help_text='MaterialDescriptionZH')
    ManufacturerName = models.CharField('ManufacturerName', max_length=100, null=True, default=None, help_text='ManufacturerName')
    ManufacturerPartNumber = models.CharField('ManufacturerPartNumber', max_length=100, null=True, default=None, help_text='ManufacturerPartNumber')
    ManufacturerModel = models.CharField('ManufacturerModel', max_length=100, null=True, default=None, help_text='ManufacturerModel')
    Unit = models.CharField('Unit', max_length=100, null=True, default=None, help_text='Unit')
    Calibration = models.CharField('Calibration', max_length=100, null=True, default=None, help_text='Calibration')
    Repairable = models.CharField('Repairable', max_length=100, null=True, default=None, help_text='Repairable')
    Material = models.CharField('Material', max_length=100, null=True, default=None, help_text='Material')
    CCCorCCCRelated = models.CharField('CCCorCCCRelated', max_length=100, null=True, default=None, help_text='CCCorCCCRelated')
    PositionNumber = models.CharField('PositionNumber', max_length=100, null=True, default=None, help_text='PositionNumber')
    MaterialMainClassification = models.CharField('MaterialMainClassification', max_length=100, null=True, default=None, help_text='MaterialMainClassification')
    MaterialSubClassification = models.CharField('MaterialSubClassification', max_length=100, null=True, default=None, help_text='MaterialSubClassification')
    ManufactureModelOld1 = models.CharField('ManufactureModelOld1', max_length=100, null=True, default=None, help_text='ManufactureModelOld1')
    ManufactureModelOld2 = models.CharField('ManufactureModelOld2', max_length=100, null=True, default=None, help_text='ManufactureModelOld2')
    ManufacturePNOld1 = models.CharField('ManufacturePNOld1', max_length=100, null=True, default=None, help_text='ManufacturePNOld1')
    ManufacturePNOld2 = models.CharField('ManufacturePNOld2', max_length=100, null=True, default=None, help_text='ManufacturePNOld2')
    Dimension = models.CharField('Dimension', max_length=100, null=True, default=None, help_text='Dimension')
    MaterialSpecialTreatment = models.CharField('MaterialSpecialTreatment', max_length=100, null=True, default=None, help_text='MaterialSpecialTreatment')
    MPRemark = models.CharField('MPRemark', max_length=100, null=True, default=None, help_text='MPRemark')
    TechRemark = models.CharField('TechRemark', max_length=100, null=True, default=None, help_text='TechRemark')
    SupplierName = models.CharField('SupplierName', max_length=100, null=True, default=None, help_text='SupplierName')
    SurplusPoint = models.CharField('SurplusPoint', max_length=100, null=True, default=None, help_text='SurplusPoint')
    InstallQty = models.CharField('InstallQty', max_length=100, null=True, default=None, help_text='InstallQty')
    create_at = models.DateTimeField('create time', auto_now_add=True, help_text='create time')


    def __str__(self):
        return self.MaterialDescriptionZH

    class Meta:
        ordering = ['id']
        db_table = 't_material'

