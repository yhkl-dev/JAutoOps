from django.db import models
from resources.models import Resource


class ServerAliCloudInstanceModel(models.Model):
    resource_name = models.ForeignKey(Resource, on_delete=models.CASCADE, null=True, verbose_name='resource info',
                                      related_name='t_resource_name', help_text='resource name')

    InstanceName = models.CharField('实例名称', max_length=100, null=True, default=None, help_text='InstanceName')
    SerialNumber = models.CharField('实例序列号', max_length=100, null=True, unique=True, default=None,
                                    help_text='SerialNumber')
    CreationTime = models.DateTimeField('实例创建时间', default=None, null=True, help_text='CreationTime')
    Status = models.CharField('实例状态', max_length=20, default=None, null=True, help_text='Status')
    OSNameEn = models.CharField('实例操作系统的英文名称', max_length=100, null=True, default=None, help_text='OSNameEn')
    InstanceNetworkType = models.CharField('InstanceNetworkType', max_length=100, null=True, default=None,
                                           help_text='InstanceNetworkType')
    Memory = models.CharField('Memory', max_length=10, default=None, null=True, help_text='Memory(MB)')
    Cpu = models.CharField('Cpu', max_length=10, default=None, null=True, help_text='Cpu')
    HostName = models.CharField('HostName', max_length=100, default=None, null=True, help_text='Cpu')
    IpAddress = models.CharField('IpAddress', max_length=39, default=None, null=True, help_text='IpAddress')
    OSType = models.CharField('OSType', max_length=40, default=None, null=True, help_text='OSType')
    RegionId = models.CharField('RegionId', max_length=40, default=None, null=True, help_text='RegionId')
    StartTime = models.DateTimeField('StartTime', null=True, help_text='start time')
    ExpiredTime = models.DateTimeField('ExpiredTime', null=True, help_text='expired time')
    LastUpdateTime = models.DateTimeField('last update datetime', auto_now=True, help_text='last update time')
    is_origin = models.BooleanField("is synced from cloud or not", default=True, help_text='is synced from cloud or not')

    def __str__(self):
        return self.IpAddress

    class Meta:
        ordering = ['id']
        db_table = 't_server'


class ServerALiCloudUserModel(models.Model):

    belong_instance = models.ForeignKey(ServerAliCloudInstanceModel, on_delete=models.CASCADE, null=True, verbose_name='belong instance',
                                      related_name='belong_instance', help_text='belong instance')
    server_username = models.CharField("server username", max_length=50, null=False, help_text='server username')
    server_password = models.CharField("server password", max_length=100, null=True, default=None, help_text='server_password')
    server_private_key = models.TextField("server private key", null=True, default=None, help_text='server private key')
    has_sudo_perm = models.BooleanField("has sudo permission", default=False, help_text='has sudo permission')
    create_time = models.DateTimeField('create time', auto_now_add=True, help_text='create time')
    update_time = models.DateTimeField('update time', auto_now=True, help_text='update time')
    description = models.CharField('description', max_length=200, null=True, default=None, help_text='description')

    def __str__(self):
        return self.server_username

    class Meta:
        ordering = ['id']
        db_table = 't_server_user'