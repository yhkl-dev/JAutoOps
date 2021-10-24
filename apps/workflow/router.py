from rest_framework.routers import DefaultRouter
from .views import WorkflowTypeModelViewSet, WorkFlowModelViewSet, WorkFlowItemModelViewSet, WorkFlowEntityModelViewSet,WorkFlowItemEntityModelViewSet

workflow_router = DefaultRouter()
workflow_router.register(r'workflow_type', WorkflowTypeModelViewSet, basename="workflow_type")
workflow_router.register(r'workflow_template', WorkFlowModelViewSet, basename="workflow_template")
workflow_router.register(r'workflow_template_item', WorkFlowItemModelViewSet, basename="workflow_template_item")
workflow_router.register(r'workflow_entity', WorkFlowEntityModelViewSet, basename="workflow_entity")
workflow_router.register(r'workflow_item_entity', WorkFlowItemEntityModelViewSet, basename="workflow_item_entity")
