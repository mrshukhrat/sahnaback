from django.contrib import admin

from museum.models import Menu
from museum.models import Banner
from museum.models import Partner
from museum.models import Comic
from museum.models import About
from museum.models import Food_Menu
from museum.models import Drink
from museum.models import Drink_Category

admin.site.register(Menu)
admin.site.register(Comic)
admin.site.register(Banner)
admin.site.register(Partner)
admin.site.register(About)
admin.site.register(Food_Menu)
admin.site.register(Drink)
admin.site.register(Drink_Category)