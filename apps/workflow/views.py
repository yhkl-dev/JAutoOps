from rest_framework import viewsets
from Jauto.paginations import Pagination
from .models import WorkflowTypeModel, WorkFlowModel, WorkFlowItemModel, WorkFlowEntityModel, WorkFlowItemEntityModel
from .serialier import WorkflowTypeModelSerializer, WorkFlowModelSerializer, WorkFlowItemModelSerializer, WorkFlowEntityModelSerializer, WorkFlowItemEntityModelSerializer

class WorkflowTypeModelViewSet(viewsets.ModelViewSet):

    queryset = WorkflowTypeModel.objects.all()
    serializer_class = WorkflowTypeModelSerializer
    pagination_class = Pagination

class WorkFlowModelViewSet(viewsets.ModelViewSet):

    queryset = WorkFlowModel.objects.all()
    serializer_class = WorkFlowModelSerializer
    pagination_class = Pagination

class WorkFlowItemModelViewSet(viewsets.ModelViewSet):

    queryset = WorkFlowItemModel.objects.all()
    serializer_class = WorkFlowItemModelSerializer
    pagination_class = Pagination

class WorkFlowEntityModelViewSet(viewsets.ModelViewSet):
    queryset = WorkFlowEntityModel.objects.all()
    serializer_class = WorkFlowEntityModelSerializer
    pagination_class = Pagination

class WorkFlowItemEntityModelViewSet(viewsets.ModelViewSet):

    queryset = WorkFlowItemEntityModel.objects.all()
    serializer_class = WorkFlowItemEntityModelSerializer
    pagination_class = Pagination