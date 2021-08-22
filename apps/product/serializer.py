from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import ProductModel

User = get_user_model()


class ProductModelSerializer(serializers.ModelSerializer):
    create_user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", label="create time", read_only=True,
                                            help_text="create time")
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", label="update time", read_only=True,
                                            help_text="update time")

    class Meta:
        model = ProductModel
        fields = '__all__'
