from rest_framework import viewsets

from Jauto.paginations import Pagination
from .models import ProductModel
from .serializer import ProductModelSerializer


class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductModelSerializer
    pagination_class = Pagination
