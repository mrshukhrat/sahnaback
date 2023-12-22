from rest_framework import  generics
from django.shortcuts import render

# Create your views here.
from .serializers import MenuSerializer
from .serializers import BannerSerializer
from .serializers import AboutSerializer
from .serializers import PartnerSerializer
from .serializers import ComicSerializer
from .serializers import Food_MenuSerializer
from .serializers import DrinkSerializer

from museum.models import Menu
from museum.models import Banner
from museum.models import Partner
from museum.models import Comic
from museum.models import About
from museum.models import Food_Menu
from museum.models import Drink

class MenuAPIView(generics.ListAPIView):
    queryset=Menu.objects.all()
    serializer_class=MenuSerializer


class BannerAPIView(generics.ListAPIView):
    queryset=Banner.objects.all()
    serializer_class=BannerSerializer


class AboutAPIView(generics.ListAPIView):
    queryset=About.objects.all()
    serializer_class=AboutSerializer


class PartnerAPIView(generics.ListAPIView):
    queryset=Partner.objects.all()
    serializer_class=PartnerSerializer


class ComicAPIView(generics.ListAPIView):
    queryset=Comic.objects.all()
    serializer_class=ComicSerializer


class Food_MenuAPIView(generics.ListAPIView):
    queryset=Food_Menu.objects.all()
    serializer_class=BannerSerializer


class DrinkAPIView(generics.ListAPIView):
    queryset=Drink.objects.all()
    serializer_class=DrinkSerializer

