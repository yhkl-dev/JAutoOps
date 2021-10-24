from rest_framework.routers import DefaultRouter
from .views import MaterialModelViewSet, MaterialGroupViewSet, PlantViewSet, TechnologyCodeViewSet, PurchaseTypeModelViewSet, HandoverTypeModelViewSet, ImportanceLevelModelViewSet, GICategoryModelViewSet


material_router = DefaultRouter()
material_router.register(r'material', MaterialModelViewSet, basename="material")
material_router.register(r'material_group', MaterialGroupViewSet, basename="material_group")
material_router.register(r'plant', PlantViewSet, basename='plant')
material_router.register(r'plant_tech', TechnologyCodeViewSet, basename='plant_tech')
material_router.register(r'purchase_type', PurchaseTypeModelViewSet, basename='purchase_type')
material_router.register(r'handover_type', HandoverTypeModelViewSet, basename='handover_type')
material_router.register(r'importance_level', ImportanceLevelModelViewSet, basename='importance_level')
material_router.register(r'gi_category', GICategoryModelViewSet, basename='gi_category')
