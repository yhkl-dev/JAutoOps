import django_filters
from .models import Resource


class ResourceFilter(django_filters.rest_framework.FilterSet):
    """
    资源过滤类
    """
    resource_name = django_filters.CharFilter(method='search_resource')
    resource_type = django_filters.NumberFilter(method='search_resource_type')


    def search_resource_type(self, queryset, name, value):
        return queryset.filter(resource_type__exact=value)

    def search_resource(self, queryset, name, value):
        return queryset.filter(resource_name__icontains=value)

    class Meta:
        model = Resource
        fields = ['resource_name', "resource_type"]