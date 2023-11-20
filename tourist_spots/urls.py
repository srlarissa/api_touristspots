"""
URL configuration for tourist_spots project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.contrib import admin
from rest_framework import routers
from django.conf.urls import include
from core.api.viewsets import TouristSpotsViewSet
from attractions.api.viewsets import AttractionsViewSet
from localizations.api.viewsets import LocalizationsViewSet
from comments.api.viewsets import CommentsViewSet
from ratings.api.viewsets import RatingsViewSet

router = routers.DefaultRouter()
router.register(r'touristspots', TouristSpotsViewSet)
router.register(r'attractions', AttractionsViewSet)
router.register(r'localizations', LocalizationsViewSet)
router.register(r'comments', CommentsViewSet)
router.register(r'ratings', RatingsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
