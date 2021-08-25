from rest_framework.routers import DefaultRouter
from .views import ProductModelViewSet


product_router = DefaultRouter()
product_router.register(r'product', ProductModelViewSet, basename="product")
