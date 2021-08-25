from rest_framework import viewsets

from Jauto.paginations import Pagination
from .models import ProjectModel, ProjectType
from .serializer import ProjectTypeSerializer, ProjectModelSerializer
from .filter import ProjectModelFilter


class ProjectTypeViewSet(viewsets.ModelViewSet):
    queryset = ProjectType.objects.all()
    serializer_class = ProjectTypeSerializer
    pagination_class = Pagination


class ProjectModelViewSet(viewsets.ModelViewSet):
    queryset = ProjectModel.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = Pagination
    filter_class = ProjectModelFilter
    filter_fields = ("belong_product",)
