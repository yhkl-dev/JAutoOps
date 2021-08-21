from rest_framework import viewsets, status, mixins
from Jauto.paginations import Pagination
from .serializer import ServerAliCloudInstanceSerializer
from .models import ServerAliCloudInstanceModel

class ServerAliCloudInstancesViewSet(viewsets.GenericViewSet,mixins.ListModelMixin):

    queryset = ServerAliCloudInstanceModel.objects.all()
    serializer_class = ServerAliCloudInstanceSerializer
    pagination_class = Pagination

