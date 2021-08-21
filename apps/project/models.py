from django.contrib.auth import get_user_model
from django.db import models
from servers.models import ServerAliCloudInstanceModel
from django.contrib.auth.models import Group


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
    create_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='create user', null=False,
                                    related_name='create_user', help_text='create user')
    belong_group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name='belong group', null=False,
                                     related_name='belong_group', help_text='belong group')
    project_type = models.ForeignKey(ProjectType, on_delete=models.CASCADE, verbose_name='project type', null=False,
                                     related_name='project_type', help_text='project type')
    deployment_server_dev = models.ForeignKey(ServerAliCloudInstanceModel, on_delete=models.CASCADE, null=False, default=None,  verbose_name='deployment server dev',
                                     related_name='deployment_server_dev', help_text='deployment server dev')
    deployment_server_prod = models.ForeignKey(ServerAliCloudInstanceModel, on_delete=models.CASCADE, null=False, default=None,  verbose_name='deployment server prod',
                                     related_name='deployment_server_prod', help_text='deployment server prod')
    github_repo_url = models.CharField('github_repo_url', max_length=100, null=False, default=None,
                                       help_text='github repo url')
    create_time = models.DateTimeField('create time', auto_now_add=True, help_text='create time')
    update_time = models.DateTimeField('update time', auto_now=True, help_text='update time')

    def __str__(self):
        return str(self.project_name)

    class Meta:
        ordering = ['id']
        db_table = 't_project'
