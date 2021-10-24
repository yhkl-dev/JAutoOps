from rest_framework import serializers
from .models import  MaterialModel, MaterialGroup, Plant, TechnologyCode,PurchaseTypeModel, HandoverTypeModel, ImportanceLevelModel, GICategoryModel


class GICategoryModelSerializer(serializers.ModelSerializer):
    create_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", label="create time", read_only=True,
                                             help_text="create time")
    class Meta:
        model = GICategoryModel
        fields = '__all__'

class MaterialModelSerializer(serializers.ModelSerializer):
    create_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", label="create time", read_only=True,
                                          help_text="create time")
    class Meta:
        model = MaterialModel
        fields = '__all__'


class MaterialGroupSerializer(serializers.ModelSerializer):
    create_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", label="create time", read_only=True,
                                          help_text="create time")
    class Meta:
        model = MaterialGroup
        fields = '__all__'

class PlantSerializer(serializers.ModelSerializer):
    create_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", label="create time", read_only=True,
                                          help_text="create time")
    class Meta:
        model = Plant
        fields = '__all__'

class TechnologyCodeSerializer(serializers.ModelSerializer):
    create_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", label="create time", read_only=True,
                                          help_text="create time")
    class Meta:
        model = TechnologyCode
        fields = '__all__'

class PurchaseTypeModelSerializer(serializers.ModelSerializer):
    create_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", label="create time", read_only=True,
                                          help_text="create time")
    class Meta:
        model = PurchaseTypeModel
        fields = '__all__'


class HandoverTypeModelSerializer(serializers.ModelSerializer):
    create_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", label="create time", read_only=True,
                                          help_text="create time")
    class Meta:
        model = HandoverTypeModel
        fields = '__all__'

class ImportanceLevelModelSerializer(serializers.ModelSerializer):
    create_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", label="create time", read_only=True,
                                          help_text="create time")
    class Meta:
        model = ImportanceLevelModel
        fields = '__all__'