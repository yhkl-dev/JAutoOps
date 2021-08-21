from rest_framework.routers import DefaultRouter
from .views import ProjectModelViewSet, ProjectTypeViewSet


project_router = DefaultRouter()
project_router.register(r'project', ProjectModelViewSet, basename="project")
project_router.register(r'project_type', ProjectTypeViewSet, basename="project_type")
