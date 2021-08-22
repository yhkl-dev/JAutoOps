from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Resource, ResourceType


User = get_user_model()

class ResourceTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ResourceType
        fields = '__all__'


class ResourceSerializer(serializers.ModelSerializer):

    belong_user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    create_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", label="create time", read_only=True, help_text="create time")
    update_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", label="create time", read_only=True, help_text="update time")

    def to_representation(self, instance):
        resource_type_obj = instance.resource_type
        user_obj = instance.belong_user
        ret = super(ResourceSerializer, self).to_representation(instance)
        ret['access_key'] = "*" * 12
        ret['access_secret'] = "*" * 12
        ret['ram_password'] = "*" * 12
        ret['type_name'] = resource_type_obj.type_name
        ret['type_icon'] = resource_type_obj.type_icon
        ret['belong_user'] = user_obj.username
        return ret

    class Meta:
        model = Resource
        fields = '__all__'