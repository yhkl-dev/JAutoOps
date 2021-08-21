from rest_framework import serializers
from .models import ServerAliCloudInstanceModel
from resources.models import Resource


class ServerAliCloudInstanceSerializer(serializers.ModelSerializer):
    LastUpdateTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", label="create time", read_only=True,
                                               help_text="last update time")
    CreationTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", label="create time", read_only=True,
                                             help_text="create time")
    StartTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", label="create time", read_only=True,
                                          help_text="start time")
    ExpiredTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", label="create time", read_only=True,
                                            help_text="expired time")

    def to_representation(self, instance):
        resource_obj = Resource.objects.get(id=instance.resource_name.id)
        ret = super(ServerAliCloudInstanceSerializer, self).to_representation(instance)
        ret['resource_name'] = resource_obj.resource_name
        return ret

    class Meta:
        model = ServerAliCloudInstanceModel
        fields = '__all__'
