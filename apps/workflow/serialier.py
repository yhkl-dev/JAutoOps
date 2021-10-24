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
    create_user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    create_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", label="create time", read_only=True,
                                          help_text="create time")
    update_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", label="update time", read_only=True,
                                          help_text="update time")

    def to_representation(self, instance):
        workflow_type = instance.work_flow_type
        ret = super(WorkFlowModelSerializer, self).to_representation(instance)
        ret['work_flow_type'] = workflow_type.type_name
        return ret

    class Meta:
        model = WorkFlowModel
        fields = '__all__'

class WorkFlowItemModelSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        belong_work_flow_obj = instance.belong_work_flow
        audit_group_obj = instance.audit_group
        ret = super(WorkFlowItemModelSerializer, self).to_representation(instance)
        ret['audit_group_name'] = audit_group_obj.name
        ret['belong_work_flow_name'] = belong_work_flow_obj.work_flow_name
        return ret

    class Meta:
        model = WorkFlowItemModel
        fields = '__all__'

class WorkFlowEntityModelSerializer(serializers.ModelSerializer):
    create_user = serializers.HiddenField(default=serializers.CurrentUserDefault())
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