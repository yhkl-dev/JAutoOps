from rest_framework import serializers

from .models import DatabaseModel, DatabaseTypeModel


class DatabaseModelSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", label="create time", read_only=True,
                                            help_text="create time")
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", label="create time", read_only=True,
                                            help_text="create time")

    class Meta:
        model = DatabaseModel
        fields = '__all__'


class DatabaseTypeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatabaseTypeModel
        fields = '__all__'
