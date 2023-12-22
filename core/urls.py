"""
URL configuration for core project.

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
from django.contrib import admin
from django.urls import path

from museum.views import MenuAPIView
from museum.views import BannerAPIView
from museum.views import AboutAPIView
from museum.views import PartnerAPIView
from museum.views import ComicAPIView
from museum.views import Food_MenuAPIView
from museum.views import DrinkAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/menu', MenuAPIView.as_view()),
    path('api/v1/banners', BannerAPIView.as_view()),
    path('api/v1/about', AboutAPIView.as_view()),
    path('api/v1/partner', PartnerAPIView.as_view()),
    path('api/v1/comic', ComicAPIView.as_view()),
    path('api/v1/food_menu', Food_MenuAPIView.as_view()),
    path('api/v1/drink', DrinkAPIView.as_view()),
]
