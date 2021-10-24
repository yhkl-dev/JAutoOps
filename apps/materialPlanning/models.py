from django.db import models
from django.contrib.auth import get_user_model
from material.models import MaterialModel, MaterialGroup, Plant, ImportanceLevelModel, TechnologyCode, PurchaseTypeModel, ImportanceLevelModel, GICategoryModel
from workflow.models import WorkFlowEntityModel, WorkFlowModel


User = get_user_model()


class PlanningStatusRuleModel(models.Model):
    status_name = models.CharField('status name', max_length=100, null=True, default=None, help_text='status name')
    next_status_name = models.CharField('next status name', max_length=100, null=True, default=None, help_text='next status name')
    comment = models.DateTimeField('comment', auto_now_add=True, help_text='create time')

    def __str__(self):
        return f"Rule: {self.status_name}:{self.next_status_name}"

    class Meta:
        ordering = ['id']
        db_table = 't_material_planning_status'


class MaterialPlanningModel(models.Model):
    STATUS_CHOICE = (
        (1, 'Start'),
        (2, 'Waiting'),
        (3, 'MRHConfirming'),
        (4, 'Pending'),
        (5, 'MRHConfirmed'),
        (6, 'STRConfirming'),
        (7, 'STRConfirmed'),
        (8, 'STRBalanced'),  # pass -> STRFinished / reject STRConfirmed
        (9, 'STRFinished'),
        (10, 'OTBCollection'),
        (11, 'PRProcessing'),
        (12, 'OrderCreating'),
        (13, 'OrderConfirming'),
        (14, 'OrderConfirmed'),
        (15, 'Producing'),
        (16, 'Delivery'),
        (17, 'GoodsReady'),
        (18, 'GoodsReceived'),
        (19, 'Invoice'),
        (20, "Cancel")
    )
    material_number = models.ForeignKey(MaterialModel, on_delete=models.CASCADE, null=False,
                                            verbose_name='material_basic_info',
                                            related_name='material_basic_info', help_text='零件号')
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, null=False,
                                            verbose_name='plant_info',
                                            related_name='plant_info', help_text='工厂代码')
    material_group_name = models.ForeignKey(MaterialGroup, on_delete=models.CASCADE, null=False, verbose_name='material_group_name',
                                     related_name='material_group_name', help_text='Material Group')

    engineer_user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, verbose_name='EngineerUser',
                                    related_name='EngineerUser', help_text='维修计划负责人')

    plant_tech_code = models.ForeignKey(TechnologyCode, on_delete=models.CASCADE, null=False, verbose_name='plant_tech_code_info',
                                      related_name='plant_tech_code_info', help_text='Technology Code')

    purchase_type = models.ForeignKey(PurchaseTypeModel, on_delete=models.CASCADE, null=False, verbose_name='purchase_type_info',
                                      related_name='purchase_type_info', help_text='采购类型')

    importance_level = models.ForeignKey(ImportanceLevelModel, on_delete=models.CASCADE, null=False, verbose_name='importance_level',
                                     related_name='importance_level', help_text='采购类型')

    gi_category = models.ForeignKey(GICategoryModel, on_delete=models.CASCADE, null=False, verbose_name='gi_category',
                                     related_name='gi_category', help_text='GI类别')

    workflow_template = models.ForeignKey(WorkFlowModel, on_delete=models.CASCADE, null=False, verbose_name='workflow template',
                                     related_name='workflow_template', help_text='workflow template')

    workflow_entity = models.ForeignKey(WorkFlowEntityModel, on_delete=models.CASCADE, null=False, verbose_name='workflow entity',
                                     related_name='workflow_entity', help_text='workflow entity')

    planning_status = models.CharField("current status",choices=STATUS_CHOICE, max_length=100, null=False, default="Start", help_text="Planning status")

    storage_location = models.CharField('存储库位', max_length=100, null=True, default=None, help_text='Storage Location')
    part_description_zh = models.CharField('零件描述(中文)', max_length=100, null=True, default=None, help_text='Part Description Zh')
    part_description_en = models.CharField('零件描述(英文)', max_length=100, null=True, default=None, help_text='Part Description EN')
    dimension = models.CharField('技术数据', max_length=100, null=True, default=None, help_text='Dimension')
    min_stock = models.CharField('安全库存', max_length=100, null=True, default=None, help_text='Min Stock')
    max_stock = models.CharField('最大库存量', max_length=100, null=True, default=None, help_text='Max Stock')
    handover_stock = models.CharField('初始移交库存', max_length=100, null=True, default=None, help_text='Handover Stock')
    unit = models.CharField('计量单位', max_length=100, null=True, default=None, help_text='Unit')
    manufacturer_name = models.CharField('制造商名称', max_length=100, null=True, default=None, help_text='Manufacturer Name')
    manufacturer_model = models.CharField('制造商的规格型号', max_length=100, null=True, default=None, help_text='Manufacturer Model')
    manufacturer_part_number = models.CharField('制造商的订货号', max_length=100, null=True, default=None, help_text='Manufacturer Part Number')
    supplier_code = models.CharField('供应商编码', max_length=100, null=True, default=None, help_text='Supplier Code')
    supplier_name = models.CharField('供应商名称', max_length=100, null=True, default=None, help_text='Supplier Name')
    supplier_model = models.CharField('供应商的规格型号', max_length=100, null=True, default=None, help_text='Supplier Model')
    supplier_part_number = models.CharField('供应商的订货号', max_length=100, null=True, default=None, help_text='Supplier Part Number')
    supplier_contact_person = models.CharField('供应商联系人', max_length=100, null=True, default=None, help_text='Supplier Contact Person')
    supplier_contact_phone = models.CharField('供应商联系电话', max_length=100, null=True, default=None, help_text='Supplier Contact Phone')
    supplier_email = models.CharField('供应商邮箱', max_length=100, null=True, default=None, help_text='Supplier Email')
    fc_no = models.CharField('框架协议号码', max_length=100, null=True, default=None, help_text='FCNo')
    unit_price = models.CharField('单价', max_length=100, null=True, default=None, help_text='Unit Price')
    currency = models.CharField('货币', max_length=100, null=True, default=None, help_text='Currency')
    equipment_name = models.CharField('设备名称', max_length=100, null=True, default=None, help_text='Equipment Name')
    repairable = models.CharField('可修理的零件', max_length=100, null=True, default=None, help_text='Repairable')
    calibration = models.CharField('校准件', max_length=100, null=True, default=None, help_text='Calibration')
    drawing = models.CharField('图纸号', max_length=100, null=True, default=None, help_text='Drawing')
    installation_quantity = models.CharField('安装数量', max_length=100, null=True, default=None, help_text='Installation Quantity')
    part_special_treatment = models.CharField('零件特殊处理', max_length=100, null=True, default=None, help_text='PartSpecial Treatment')
    surplus_stock = models.CharField('剩余库存', max_length=100, null=True, default=None, help_text='Surplus Stock')
    create_at = models.DateTimeField('create time', auto_now_add=True, null=True, help_text='create time')
    update_at = models.DateTimeField('update time', auto_now=True, help_text='update time')

    def __str__(self):
        return self.part_description_zh

    class Meta:
        ordering = ['id']
        db_table = 't_material_planning'


