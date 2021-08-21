from rest_framework.routers import DefaultRouter
from .views import ServerAliCloudInstancesViewSet

instance_router = DefaultRouter()
instance_router.register(r'instance', ServerAliCloudInstancesViewSet, basename="instance")
