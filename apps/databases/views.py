from rest_framework import viewsets, mixins

from Jauto.paginations import Pagination
from .models import DatabaseTypeModel, DatabaseModel
from .serializer import DatabaseModelSerializer, DatabaseTypeModelSerializer


class DatabaseTypeModelViewSet(viewsets.ModelViewSet):
    queryset = DatabaseTypeModel.objects.all()
    serializer_class = DatabaseTypeModelSerializer
    pagination_class = Pagination


class DatabaseModelViewSet(viewsets.ModelViewSet):
    queryset = DatabaseModel.objects.all()
    serializer_class = DatabaseModelSerializer
    pagination_class = Pagination