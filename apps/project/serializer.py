from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import serializers
from servers.models import ServerAliCloudInstanceModel

from .models import ProjectType, ProjectModel
from product.models import ProductModel

User = get_user_model()


class ProjectTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectType
        fields = '__all__'


class ProjectModelSerializer(serializers.ModelSerializer):
    create_user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", label="create time", read_only=True,
                                            help_text="create time")
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", label="update time", read_only=True,
                                            help_text="update time")

    def to_representation(self, instance):
        type_obj = ProjectType.objects.get(id=instance.project_type.id)
        deployment_server_dev = ServerAliCloudInstanceModel.objects.get(id=instance.deployment_server_dev.id)
        deployment_server_prod = ServerAliCloudInstanceModel.objects.get(id=instance.deployment_server_prod.id)
        group_obj = Group.objects.get(id=instance.belong_group.id)
        product_obj = ProductModel.objects.get(id=instance.belong_product.id)
        users_obj_list = instance.ops_users.all()
        ops_user_list = [{'id': user.id, "username": user.username} for user in users_obj_list]
        dev_users_obj = instance.dev_users.all()
        dev_users_list = [{'id': user.id, "username": user.username} for user in dev_users_obj]
        ret = super(ProjectModelSerializer, self).to_representation(instance)
        ret['project_type'] = type_obj.type_name
        ret['project_type_id'] = type_obj.id
        ret['project_type_icon'] = type_obj.type_icon
        ret['deployment_server_dev'] = deployment_server_dev.IpAddress
        ret['deployment_server_dev_id'] = deployment_server_dev.id
        ret['deployment_server_prod'] = deployment_server_prod.IpAddress
        ret['deployment_server_prod_id'] = deployment_server_prod.id
        ret['belong_group'] = group_obj.name
        ret['belong_group_id'] = group_obj.id
        ret['dev_users_list'] = dev_users_list
        ret['ops_users_list'] = ops_user_list
        ret['belong_product_id'] = product_obj.id
        ret['belong_product'] = product_obj.product_name
        return ret

    class Meta:
        model = ProjectModel
        fields = '__all__'
