from rest_framework.routers import DefaultRouter
from .views import ResourceTypeViewSet, ResourceViewSet, UpdateResourceInstanceInfo


resource_router = DefaultRouter()
resource_router.register(r'resource', ResourceViewSet, basename="resource")
resource_router.register(r'resource_type', ResourceTypeViewSet, basename="resourceType")
resource_router.register(r'update_resource_server', UpdateResourceInstanceInfo, basename='updateResourceServer')
