from rest_framework import serializers
from .models import Menu
from .models import Banner
from .models import Comic
from .models import Partner
from .models import About
from .models import Food_Menu
from .models import Drink

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model=Menu
        fields = ['id','title','link']

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ['name','description','type','price','url','date','images','status']


class ComicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comic
        fields = ['first_name','last_name','bio','telegram','instagram','images']


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['name','url','images']

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['title','description','address','work_time','phone','messenger_url']

class Food_MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food_Menu
        fields = ['title','description','price']


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['title','description','price']