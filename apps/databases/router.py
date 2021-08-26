from rest_framework.routers import DefaultRouter
from .views import DatabaseModelViewSet, DatabaseTypeModelViewSet

database_router = DefaultRouter()
database_router.register(r'database', DatabaseModelViewSet, basename="database")
database_router.register(r'database_type', DatabaseTypeModelViewSet, basename="database_type")
