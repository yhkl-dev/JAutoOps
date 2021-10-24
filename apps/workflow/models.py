from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

User = get_user_model()


class WorkflowTypeModel(models.Model):
    type_name = models.CharField('type name', max_length=100, null=True, default=None, help_text='type name')
    comment = models.CharField('comment', max_length=100, null=True, default=None, help_text='comment')
    create_at = models.DateTimeField('create time', auto_now_add=True, help_text='create time')

    def __str__(self):
        return self.type_name

    class Meta:
        ordering = ['id']
        db_table = 't_workflow_type'


class WorkFlowModel(models.Model):
    work_flow_name = models.CharField('work flow name', max_length=100, null=True, default=None,
                                      help_text='work flow name')
    work_flow_type = models.ForeignKey(WorkflowTypeModel, on_delete=models.CASCADE, null=False,
                                       verbose_name='work_flow_type_for_template',
                                       related_name='work_flow_type_for_template', help_text='负责人信息')
    create_at = models.DateTimeField('create time', auto_now_add=True, help_text='create time')
    update_at = models.DateTimeField('update time', auto_now_add=True, help_text='update time')
    create_user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, verbose_name='workflow_create_user',
                                    related_name='workflow_create_user', help_text='负责人信息')

    def __str__(self):
        return self.work_flow_name

    class Meta:
        ordering = ['id']
        db_table = 't_workflow'


class WorkFlowItemModel(models.Model):
    item_name = models.CharField('item name', max_length=100, null=True, default=None, help_text='item name')
    item_status = models.CharField('item status', max_length=100, null=True, default=None, help_text='item status')
    is_begin_or_end = models.BooleanField("is begin or end status", default=False, help_text="is begin or end status")
    item_last_status = models.CharField('item last status', max_length=100, null=True, default=None,
                                        help_text='item last status')
    item_next_status = models.CharField('item next status', max_length=100, null=True, default=None,
                                        help_text='item next status')
    audit_group = models.ForeignKey(Group, on_delete=models.CASCADE, null=False, verbose_name='audit group',
                                    related_name='audit_group', help_text='审批role')
    belong_work_flow = models.ForeignKey(WorkFlowModel, on_delete=models.CASCADE, null=False,
                                         verbose_name='belong work flow',
                                         related_name='belong_work_flow', help_text='belong work flow')

    def __str__(self):
        return self.item_name

    class Meta:
        ordering = ['id']
        db_table = 't_workflow_item'


class WorkFlowEntityModel(models.Model):
    '''
        work flow entity
   '''
    work_flow_name = models.CharField('work flow name', max_length=100, null=True, default=None,
                                      help_text='work flow name')
    work_flow_type = models.ForeignKey(WorkflowTypeModel, on_delete=models.CASCADE, null=False,
                                       verbose_name='work flow type for entity',
                                       related_name='work_flow_type_for_entity', help_text='work flow type')
    create_at = models.DateTimeField('create time', auto_now_add=True, help_text='create time')
    update_at = models.DateTimeField('update time', auto_now=True, help_text='update time')
    create_user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, verbose_name='workflow_entity_create_user',
                                    related_name='workflow_entity_create_user', help_text='create user')

    def __str__(self):
        return self.work_flow_name

    class Meta:
        ordering = ['id']
        db_table = 't_workflow_entity'


class WorkFlowItemEntityModel(models.Model):
    '''
     work flow item entity
    '''

    item_name = models.CharField('item_name', max_length=100, null=True, default=None, help_text='item name')
    item_status = models.CharField('item_status', max_length=100, null=True, default=None, help_text='item status')
    is_begin_or_end = models.BooleanField("is begin or end status", default=False, help_text="is begin or end status")
    item_last_status = models.CharField('item last status', max_length=100, null=True, default=None,
                                        help_text='item last status')
    item_next_status = models.CharField('item next status', max_length=100, null=True, default=None,
                                        help_text='item next status')
    belong_work_flow_template = models.ForeignKey(WorkFlowModel, on_delete=models.CASCADE, null=False,
                                                  verbose_name='belong_work_flow_template',
                                                  related_name='belong_work_flow_template',
                                                  help_text='belong work flow')
    belong_work_flow = models.ForeignKey(WorkFlowEntityModel, on_delete=models.CASCADE, null=False,
                                         verbose_name='belong_work_flow',
                                         related_name='belong_work_flow', help_text='belong work flow')

    def __str__(self):
        return self.item_name

    class Meta:
        ordering = ['id']
        db_table = 't_workflow_item_entity'
