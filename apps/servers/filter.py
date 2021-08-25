import django_filters

from .models import ServerAliCloudInstanceModel


class ServerAliCloudInstanceModelFilter(django_filters.rest_framework.FilterSet):
    """
    用户过滤类
    """
    resource_name = django_filters.NumberFilter(method='search_resource')

    def search_resource(self, queryset, name, value):
        return queryset.filter(resource_name_id=value)

    class Meta:
        model = ServerAliCloudInstanceModel
        fields = ['resource_name']
