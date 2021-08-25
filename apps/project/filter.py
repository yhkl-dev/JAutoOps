import django_filters

from .models import ProjectModel


class ProjectModelFilter(django_filters.rest_framework.FilterSet):
    product_id = django_filters.NumberFilter(method='search_product')

    def search_product(self, queryset, name, value):
        return queryset.filter(belong_product_id_exact=value)

    class Meta:
        model = ProjectModel
        fields = ['belong_product']
