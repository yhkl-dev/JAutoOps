from rest_framework import viewsets, mixins

from Jauto.paginations import Pagination
from .filter import ServerAliCloudInstanceModelFilter
from .models import ServerAliCloudInstanceModel, ServerALiCloudUserModel
from .serializer import ServerAliCloudInstanceSerializer, ServerALiCloudUserModelSerializer


class ServerAliCloudInstancesViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = ServerAliCloudInstanceModel.objects.all()
    serializer_class = ServerAliCloudInstanceSerializer
    pagination_class = Pagination
    filter_class = ServerAliCloudInstanceModelFilter
    filter_fields = ("resource_name",)


class ServerALiCloudUserModelViewSet(viewsets.ModelViewSet):
    queryset = ServerALiCloudUserModel.objects.all()
    serializer_class = ServerALiCloudUserModelSerializer
    pagination_class = Pagination
