from rest_framework.routers import DefaultRouter
from .views import ServerAliCloudInstancesViewSet, ServerALiCloudUserModelViewSet

instance_router = DefaultRouter()
instance_router.register(r'instance', ServerAliCloudInstancesViewSet, basename="instance")
instance_router.register(r'instance_users', ServerALiCloudUserModelViewSet, basename="instance_users")
