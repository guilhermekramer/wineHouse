"""
URL configuration for apiWine project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.contrib import admin
from django.urls import include, path
from apiWine.views import wineView
from rest_framework import routers

from apiWine.views.userView import UserViewSet

router = routers.DefaultRouter()
router.register("user", UserViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("createWine/", wineView.create_wine),
    path("wines/", wineView.wine_list),
    path("wines/<int:id>/", wineView.wine_detail),
    path("findWine/", wineView.find_wine),
    path("updateWine/<int:id>/", wineView.update_wine),
    path("deleteWine/<int:id>/", wineView.delete_wine),
    path("", include(router.urls)),
]
