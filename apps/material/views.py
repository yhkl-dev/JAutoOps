from rest_framework import viewsets
from Jauto.paginations import Pagination
from .models import  MaterialModel, MaterialGroup, Plant, TechnologyCode, PurchaseTypeModel, HandoverTypeModel, ImportanceLevelModel, GICategoryModel
from .serializer import MaterialModelSerializer, MaterialGroupSerializer, PlantSerializer, TechnologyCodeSerializer, PurchaseTypeModelSerializer, HandoverTypeModelSerializer, \
    ImportanceLevelModelSerializer, GICategoryModelSerializer


class GICategoryModelViewSet(viewsets.ModelViewSet):

    queryset = GICategoryModel.objects.all()
    serializer_class = GICategoryModelSerializer
    pagination_class = Pagination

class MaterialModelViewSet(viewsets.ModelViewSet):

    queryset = MaterialModel.objects.all()
    serializer_class = MaterialModelSerializer
    pagination_class = Pagination

class MaterialGroupViewSet(viewsets.ModelViewSet):

    queryset = MaterialGroup.objects.all()
    serializer_class = MaterialGroupSerializer
    pagination_class = Pagination


class PlantViewSet(viewsets.ModelViewSet):

    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    pagination_class = Pagination

class TechnologyCodeViewSet(viewsets.ModelViewSet):

    queryset = TechnologyCode.objects.all()
    serializer_class = TechnologyCodeSerializer
    pagination_class = Pagination

class PurchaseTypeModelViewSet(viewsets.ModelViewSet):

    queryset = PurchaseTypeModel.objects.all()
    serializer_class = PurchaseTypeModelSerializer
    pagination_class = Pagination

class HandoverTypeModelViewSet(viewsets.ModelViewSet):

    queryset = HandoverTypeModel.objects.all()
    serializer_class = HandoverTypeModelSerializer
    pagination_class = Pagination

class ImportanceLevelModelViewSet(viewsets.ModelViewSet):

    queryset = ImportanceLevelModel.objects.all()
    serializer_class = ImportanceLevelModelSerializer
    pagination_class = Pagination