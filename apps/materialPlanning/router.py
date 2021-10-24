from rest_framework.routers import DefaultRouter
from .views import MaterialPlanningModelViewSet, PlanningStatusRuleModelViewSet


material_planning_router = DefaultRouter()
material_planning_router.register(r'material_planning', MaterialPlanningModelViewSet, basename="material_planning")
material_planning_router.register(r'material_planning_status', PlanningStatusRuleModelViewSet, basename="material_planning_status")
