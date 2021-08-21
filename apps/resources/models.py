from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class ResourceType(models.Model):
    type_name = models.CharField('resource type name', max_length=30, default=None, help_text='resource type name')
    type_icon = models.CharField('resource type icon', max_length=30, default=None, help_text='resource type icon')

    def __str__(self):
        return self.type_name

    class Meta:
        ordering = ['id']
        db_table = 't_resource_type'


class Resource(models.Model):
    resource_name = models.CharField('resource name', max_length=50, default=None, db_index=True, unique=True,
                                     help_text='resource name')
    resource_type = models.ForeignKey(ResourceType, on_delete=models.CASCADE, null=True, verbose_name='resource type',
                                      related_name='resource_type', help_text='resource type')
    belong_user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, verbose_name='belong user',
                                    related_name='belong_user', help_text='belong user')
    access_key = models.CharField('access key', max_length=100, null=False, default=None, help_text='access key')
    access_secret = models.CharField('access secret', max_length=100, null=False, default=None,
                                     help_text='access secret')
    main_account = models.CharField('main account', max_length=100, null=True, default=None,
                                    help_text='main account for tencent')
    ram_username = models.CharField('ram_user', max_length=100, null=False, default=None, help_text='ram user')
    ram_password = models.CharField('ram_password', max_length=100, null=False, default=None,
                                    help_text='ram user password')
    create_at = models.DateTimeField('create time', auto_now_add=True, help_text='create time')
    update_at = models.DateTimeField('update time', auto_now=True, help_text='update time')
    description = models.CharField('description', max_length=200, default=None, blank=True, help_text='description')

    def __str__(self):
        return self.resource_name

    class Meta:
        ordering = ['id']
        db_table = 't_resource'
