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
from django.conf import settings
from django.conf.urls.static import static
from core.api.viewsets import TouristSpotViewSet
from attractions.api.viewsets import AttractionViewSet
from localizations.api.viewsets import LocalizationViewSet
from comments.api.viewsets import CommentViewSet
from ratings.api.viewsets import RatingViewSet

router = routers.DefaultRouter()
router.register(r'touristspots', TouristSpotViewSet, basename='TouristSpot')
router.register(r'attractions', AttractionViewSet)
router.register(r'localizations', LocalizationViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'ratings', RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
