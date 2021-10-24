from rest_framework import serializers
from .models import PlanningStatusRuleModel, MaterialPlanningModel


class MaterialPlanningModelSerializer(serializers.ModelSerializer):
    create_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", label="create time", read_only=True,
                                             help_text="create time")
    class Meta:
        model = MaterialPlanningModel
        fields = '__all__'


class PlanningStatusRuleModelSerializer(serializers.ModelSerializer):
    create_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", label="create time", read_only=True,
                                          help_text="create time")
    class Meta:
        model = PlanningStatusRuleModel
        fields = '__all__'
