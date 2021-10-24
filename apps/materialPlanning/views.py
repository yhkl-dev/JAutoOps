from rest_framework import viewsets
from Jauto.paginations import Pagination
from .models import PlanningStatusRuleModel, MaterialPlanningModel
from .serializer import MaterialPlanningModelSerializer, PlanningStatusRuleModelSerializer

class MaterialPlanningModelViewSet(viewsets.ModelViewSet):

    queryset = MaterialPlanningModel.objects.all()
    serializer_class = MaterialPlanningModelSerializer
    pagination_class = Pagination

class PlanningStatusRuleModelViewSet(viewsets.ModelViewSet):

    queryset = PlanningStatusRuleModel.objects.all()
    serializer_class = PlanningStatusRuleModelSerializer
    pagination_class = Pagination