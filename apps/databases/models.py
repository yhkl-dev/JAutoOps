from django.db import models


class DatabaseTypeModel(models.Model):
    type_name = models.CharField('database type name', max_length=30, default=None, help_text='database type name')
    type_icon = models.CharField('database type icon', max_length=30, default=None, help_text='database type icon')

    def __str__(self):
        return self.type_name

    class Meta:
        ordering = ['id']
        db_table = 't_database_type'


class DatabaseModel(models.Model):
    db_name = models.CharField("database name", max_length=50, null=False, help_text='database name')
    db_host = models.GenericIPAddressField("database host", protocol="IPv4", help_text='database port')
    db_username = models.CharField("database username", max_length=50, null=False, help_text='database username')
    db_password = models.CharField("database password", max_length=50, null=False, help_text='database password')
    db_port = models.IntegerField("database port", null=False, help_text='database port')
    db_default_schema = models.CharField("database default schema", max_length=20, help_text='database default schema')
    create_time = models.DateTimeField('create time', auto_now_add=True, help_text='create time')
    update_time = models.DateTimeField('update time', auto_now=True, help_text='update time')
    description = models.CharField('description', max_length=200, null=True, default=None, help_text='description')

    def __str__(self):
        return self.db_name

    class Meta:
        ordering = ['id']
        db_table = 't_database'
