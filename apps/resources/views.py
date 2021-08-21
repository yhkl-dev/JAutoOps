from rest_framework import viewsets, status, mixins
from rest_framework.response import Response

from Jauto.paginations import Pagination
from .common import get_instance_list, get_tencent_instance_info
from .filter import ResourceFilter
from .models import Resource, ResourceType
from .serializer import ResourceSerializer, ResourceTypeSerializer


class ResourceTypeViewSet(viewsets.ModelViewSet):
    """
            retrieve:
            返回指定资源类型信息
            list:
            返回资源类型列表
            update:
            更新资源类型信息
            destroy:
            删除资源类型记录
            create:
            创建资源类型
            partial_update:
            更新部分字段
    """

    queryset = ResourceType.objects.all()
    serializer_class = ResourceTypeSerializer
    pagination_class = Pagination


class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    pagination_class = Pagination
    filter_class = ResourceFilter
    filter_fields = ("resource_name", "resource_type", "service_id", "server_purpose")

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class UpdateResourceInstanceInfo(viewsets.ViewSet, mixins.CreateModelMixin):
    queryset = Resource.objects.all()

    def create(self, request, *args, **kwargs):
        for q in self.queryset:
            print(q.access_key, q.access_secret, q.resource_name, q.resource_type.type_name)
            if q.resource_type.type_name == '腾讯云':
                get_tencent_instance_info(q.access_key, q.access_secret, resource=q.id)
            elif q.resource_type.type_name == '阿里云':
                get_instance_list(q.access_key, q.access_secret, resource=q.id)

        return Response(status=status.HTTP_201_CREATED)

    def perform_update(self, serializer):
        serializer.save()
