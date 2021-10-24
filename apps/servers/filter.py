import django_filters

from .models import ServerAliCloudInstanceModel, ServerALiCloudUserModel


class ServerAliCloudInstanceModelFilter(django_filters.rest_framework.FilterSet):
    resource_name = django_filters.NumberFilter(method='search_resource')

    def search_resource(self, queryset, name, value):
        return queryset.filter(resource_name_id=value)

    class Meta:
        model = ServerAliCloudInstanceModel
        fields = ['resource_name']


class ServerAliCloudInstanceUserModelFilter(django_filters.rest_framework.FilterSet):
    belong_instance = django_filters.NumberFilter(method='search_instance')

    def search_instance(self, queryset, name, value):
        return queryset.filter(belong_instance_id=value)

    class Meta:
        model = ServerALiCloudUserModel
        fields = ['belong_instance']
