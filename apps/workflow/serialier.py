from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import WorkflowTypeModel, WorkFlowModel, WorkFlowItemModel, WorkFlowEntityModel, WorkFlowItemEntityModel
User = get_user_model()

class WorkflowTypeModelSerializer(serializers.ModelSerializer):
    create_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", label="create time", read_only=True,
                                             help_text="create time")
    class Meta:
        model = WorkflowTypeModel
        fields = '__all__'

class WorkFlowModelSerializer(serializers.ModelSerializer):
    create_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", label="create time", read_only=True,
                                          help_text="create time")
    class Meta:
        model = WorkFlowModel
        fields = '__all__'

class WorkFlowItemModelSerializer(serializers.ModelSerializer):
    create_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", label="create time", read_only=True,
                                          help_text="create time")
    class Meta:
        model = WorkFlowItemModel
        fields = '__all__'

class WorkFlowEntityModelSerializer(serializers.ModelSerializer):
    create_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", label="create time", read_only=True,
                                          help_text="create time")
    class Meta:
        model = WorkFlowEntityModel
        fields = '__all__'

class WorkFlowItemEntityModelSerializer(serializers.ModelSerializer):
    create_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", label="create time", read_only=True,
                                          help_text="create time")
    class Meta:
        model = WorkFlowItemEntityModel
        fields = '__all__'