from modeltranslation.translator import register, TranslationOptions

from museum.models import Menu
from museum.models import Banner
from museum.models import About
from museum.models import Comic
from museum.models import Drink
from museum.models import Food_Menu


@register(Menu)
class MenuTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(Banner)
class TopBannerTranslationOptions(TranslationOptions):
        fields = ('name','description','type')

@register(About)
class AboutTranslationOptions(TranslationOptions):
        fields = ('title','description','address')

@register(Comic)
class ComicTranslationOptions(TranslationOptions):
        fields = ('first_name','last_name','bio')


@register(Food_Menu)
class Food_MenuTranslationOptions(TranslationOptions):
        fields = ('title','description')


@register(Drink)
class DrinkTranslationOptions(TranslationOptions):
        fields = ('title','description')