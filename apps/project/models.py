from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db import models
from servers.models import ServerAliCloudInstanceModel
from product.models import ProductModel

User = get_user_model()


class ProjectType(models.Model):
    type_name = models.CharField('project type name', max_length=30, default=None, help_text='project type name')
    type_icon = models.CharField('project type icon', max_length=30, default=None, help_text='project type icon')

    def __str__(self):
        return self.type_name

    class Meta:
        ordering = ['id']
        db_table = 't_project_type'


class ProjectModel(models.Model):
    project_name = models.CharField('project name', max_length=50, null=False, unique=True, help_text='project name')

    belong_product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, verbose_name='belong product',
                                       null=False,
                                       related_name='belong_product', help_text='belong product')

    create_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='create user', null=False,
                                    related_name='create_user', help_text='create user')
    belong_group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='belong group', null=False,
                                     related_name='belong_group', help_text='belong group')
    project_type = models.ForeignKey(ProjectType, on_delete=models.CASCADE, verbose_name='project type', null=False,
                                     related_name='project_type', help_text='project type')
    deployment_server_dev = models.ForeignKey(ServerAliCloudInstanceModel, on_delete=models.CASCADE, null=False,
                                              default=None, verbose_name='deployment server dev',
                                              related_name='deployment_server_dev', help_text='deployment server dev')
    deployment_server_prod = models.ForeignKey(ServerAliCloudInstanceModel, on_delete=models.CASCADE, null=False,
                                               default=None, verbose_name='deployment server prod',
                                               related_name='deployment_server_prod',
                                               help_text='deployment server prod')
    github_repo_url = models.CharField('github_repo_url', max_length=100, null=False, default=None,
                                       help_text='github repo url')

    ops_users = models.ManyToManyField(User,
                                       verbose_name='ops users',
                                       blank=True,
                                       related_name="ops_users",
                                       help_text='ops users')
    dev_users = models.ManyToManyField(User,
                                       verbose_name='dev users',
                                       blank=True,
                                       related_name="dev_users",
                                       help_text='dev users')
    create_time = models.DateTimeField('create time', auto_now_add=True, help_text='create time')
    update_time = models.DateTimeField('update time', auto_now=True, help_text='update time')
    description = models.CharField('description', max_length=200, null=True, default=None, help_text='description')

    def __str__(self):
        return str(self.project_name)

    class Meta:
        ordering = ['id']
        db_table = 't_project'
