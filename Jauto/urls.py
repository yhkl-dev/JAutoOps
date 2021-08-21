"""Jauto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from groups.router import group_router
from menu.router import menu_router
from permissions.router import permission_router
from project.router import project_router
from resources.router import resource_router
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from servers.router import instance_router
from users.router import user_router

router = DefaultRouter()
router.registry.extend(user_router.registry)
router.registry.extend(group_router.registry)
router.registry.extend(menu_router.registry)
router.registry.extend(permission_router.registry)
router.registry.extend(resource_router.registry)
router.registry.extend(instance_router.registry)
router.registry.extend(project_router.registry)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^docs/', include_docs_urls("J Auto Devops")),
]
