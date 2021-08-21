from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import ProjectType, ProjectModel
from servers.models import ServerAliCloudInstanceModel
from django.contrib.auth.models import Group


User = get_user_model()

class ProjectTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectType
        fields = '__all__'


class ProjectModelSerializer(serializers.ModelSerializer):

    create_user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", label="create time", read_only=True, help_text="create time")
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", label="update time", read_only=True, help_text="update time")

    def to_representation(self, instance):
        type_obj = ProjectType.objects.get(id=instance.project_type.id)
        deployment_server_dev =ServerAliCloudInstanceModel.objects.get(id=instance.deployment_server_dev.id)
        deployment_server_prod =ServerAliCloudInstanceModel.objects.get(id=instance.deployment_server_prod.id)
        group_obj = Group.objects.get(id=instance.belong_group.id)
        ret = super(ProjectModelSerializer, self).to_representation(instance)
        ret['project_type'] = type_obj.type_name
        ret['deployment_server_dev'] = deployment_server_dev.IpAddress
        ret['deployment_server_prod'] = deployment_server_prod.IpAddress
        ret['belong_group'] = group_obj.name
        return ret

    class Meta:
        model = ProjectModel
        fields = '__all__'